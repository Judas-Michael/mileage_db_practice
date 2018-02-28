import mileage
import sqlite3
from unittest import TestCase

class TestMileageDB(TestCase):

	test_db_url = 'test_miles.db'
	
	def setUp(self):
	
		mileage.db_url = self.test_db_url
	
		conn = sqlite3.connect(self.test_db_url)
		conn.execute('DELETE FROM miles')
		conn.commit()
		conn.close()
	
	def test_add_new_vehicle(self):
		mileage.add_miles('Blue Car', 100)
		expected = {'Blue Car': 100}
		self. compare_db_to_expected(expected)
		
		mileage.add_miles('Green Car', 50)
		expected ['Green Car'] = 50
		self.compare_db_to_expected(expected)
		
	def test_increase_miles_for_vehicle(self):
		mileage.add_miles('Red Car', 100)
		expected = {'Red Car' : 100}
		self.compare_db_to_expected(expected)
		
		mileage.add_miles('Red Car', 50)
		expected['Red Car'] = 100+50
		self.compare_db_to_expected(expected)
		
	def compare_db_to_expected(self, expected):
		
		conn = sqlite3.connect(self.test_db_url)
		cursor = conn.cursor()
		all_data = cursor.execute('SELECT * FROM MILES').fetchall()
		
		self.assertEqual(len(expected.keys()), len(all_data))
		
		for row in all_data:
			self.assertIn(row[0], expected.keys())
			self.assertEqual(expected[row[0]], row[1])
			
		conn.close()
		
		
	def test_vehicle_name(self):
	
	mileage.add_miles('Blue Car', 100)
		expected = {'BLUE CAR': 100}
		self. compare_db_to_expected(expected)
		
	