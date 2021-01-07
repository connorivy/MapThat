from fastkml import kml
import shapely.geometry as sh
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os

class KMLifyer():
	def __init__(self):
		self.k = kml.KML()
		self.d = kml.Document('{http://www.opengis.net/kml/2.2}')
		self.Placemarks = []
		self.image_collection = []
		self.count = 0

	def create_pm(self, lat, lon, img_file):
		self.count +=1
		name = f'Image {self.count}'
		lat = float(lat)
		lon = float(lon)

		point = sh.Point(lat, lon, 0)
		img_file = "documents/" + img_file[2:]
		pm = kml.Placemark('{http://www.opengis.net/kml/2.2}', str(self.count),name, f'<img style="max-width:300px;" src="http://127.0.0.1:8000/{img_file}">'.encode(encoding='UTF-8',errors='strict'))
		pm.geometry = point
		self.Placemarks.append(pm) 

	def gen_kml(self):
		fol = kml.Folder()
		for place in self.Placemarks:
			fol.append(place)
		self.d.append(fol)
		self.k.append(self.d)
		kml_string = self.k.to_string(prettyprint=True)

		return kml_string
		# with open(self.file, 'w') as f:
		# 	f.write(kml_string)

	# Returns a dictionary of all exif data
	def get_exif_data(self, image):
	    exif_data = {}
	    info = image._getexif()

	    if info:
	        for tag, value in info.items():
	            decoded = TAGS.get(tag, tag)
	            if decoded == "GPSInfo":
	                gps_data = {}
	                for t in value:
	                    sub_decoded = GPSTAGS.get(t, t)
	                    gps_data[sub_decoded] = value[t]

	                exif_data[decoded] = gps_data
	            else:
	                exif_data[decoded] = value

	    return exif_data

	def _get_if_exist(self, data, key):
	    if key in data:
	        return data[key]

	    return None

	def _convert_to_degress(self, value):
	    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
	    d0 = value[0][0]
	    d1 = value[0][1]
	    d = float(d0) / float(d1)

	    m0 = value[1][0]
	    m1 = value[1][1]
	    m = float(m0) / float(m1)

	    s0 = value[2][0]
	    s1 = value[2][1]
	    s = float(s0) / float(s1)

	    return d + (m / 60.0) + (s / 3600.0)

	# Returns latitude and longitude
	def get_lat_lon(self, exif_data):
	    lat = None
	    lon = None

	    if "GPSInfo" in exif_data:
	        gps_info = exif_data["GPSInfo"]

	        gps_latitude = self._get_if_exist(gps_info, "GPSLatitude")
	        gps_latitude_ref = self._get_if_exist(gps_info, 'GPSLatitudeRef')
	        gps_longitude = self._get_if_exist(gps_info, 'GPSLongitude')
	        gps_longitude_ref = self._get_if_exist(gps_info, 'GPSLongitudeRef')

	        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
	            lat = self._convert_to_degress(gps_latitude)
	            if gps_latitude_ref != "N":
	                lat = 0 - lat

	            lon = self._convert_to_degress(gps_longitude)
	            if gps_longitude_ref != "E":
	                lon = 0 - lon

	    return lat, lon

	def extract(self, filepath):
		# filepath = '.' + filepath
		# filepath = os.path.abspath(filepath)
		# filepath = filepath.replace('\\', '/')
		self.image_collection.append(filepath)
		image = Image.open(filepath)
		exif_data = self.get_exif_data(image)
		lon, lat = self.get_lat_lon(exif_data)
		self.create_pm(lat, lon, filepath)