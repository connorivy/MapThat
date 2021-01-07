import unittest
from GenerateKML import KMLifyer
class TestGenerateKML(unittest.TestCase):

	def test_example(self):
		try:
			coords = [['-97.739565','30.293239'], ['-97.737633', '30.290525',]]
			km = KMLifyer('./example.kml')
			km.extract('./test_images/DSCN0010.jpg')
			km.extract('./test_images/Canon_PowerShot_S40.jpg')
			km.gen_kml()
		except:
			self.fail("Test Failed to Execute")
if __name__ == '__main__':
	unittest.main()