# Map That

Map That is a simple web app that scrapes EXIF data from uploaded images and then plots them on a leaflet map. This is intended to be used as a tool for presenting findings for site visits or other applications where images and locations of those images can be combined to create a more wholestic view for the audience than the images alone.

This project does **not** require any GIS library or specific database.
Map data are stored in simple JSON fields.

**USE PYTHON 3.7**

#### Step 1 - Clone and Install Dependencies:
`git clone https://github.com/connorivy/GBScheduler.git`

** Optional - create virtual environment `py -3.7 -m venv venv` `venv\Scripts\activate.bat` **

`pip install -r requirements.txt`

#### Step 2 - Run the Server:
`python manage.py runserver`

#### Step 3 - Upload Images:
![upload_files](https://user-images.githubusercontent.com/43247197/165401495-412a10cb-b394-43b4-9fbd-d06214a38a3b.gif)

#### Step 4 - Open Built KML:
![open_kml](https://user-images.githubusercontent.com/43247197/165402073-734963dc-ea35-492d-8f8b-c0495deb2b9f.gif)

#### Step 5 - Present:
Replace your boring slideshow of images with 'Map That' to give a more dynamic and wholistic presentation of site information.

![usage](https://user-images.githubusercontent.com/43247197/165402754-78aa6d39-4793-4a1a-8bde-9dbe11a7dbb6.gif)








