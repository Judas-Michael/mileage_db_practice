import mileage
import sqlite3
from unittest import TestCase

class TestMileageDB(TestCase):

	test_db_url = 'test_miles.db'
	
	def setUp(self):
	
		mileage.db_url = self.test_db_url #assigns name
	
		conn = sqlite3.connect(self.test_db_url) #connects db
		conn.execute('DELETE FROM miles') #deletes miles AKA clears db
		conn.commit() #save
		conn.close() #close db
	
	def test_add_new_vehicle(self):
		mileage.add_miles('Blue Car', 100) #adds 100 miles to blue car
		expected = {'BLUE CAR': 100} #should be uppercase + 100
		self. compare_db_to_expected(expected) #compares
		
		mileage.add_miles('Green Car', 50) #adds 50 miles to green car
		expected ['GREEN CAR'] = 50 #green car is equal to 50
		self.compare_db_to_expected(expected) #compares
		
	def test_increase_miles_for_vehicle(self):
		mileage.add_miles('Red Car', 100) #add miles to red car
		expected = {'RED CAR' : 100} #expected input
		self.compare_db_to_expected(expected) #compare
		
		mileage.add_miles('Red Car', 50) #add more miles to red car
		expected['RED CAR'] = 100+50 #expected to add miles together not overwrite
		self.compare_db_to_expected(expected) #compare
		
	def compare_db_to_expected(self, expected): #this is a helper method to be called from tests 
		
		conn = sqlite3.connect(self.test_db_url) #connects db
		cursor = conn.cursor() #cursor
		all_data = cursor.execute('SELECT * FROM MILES').fetchall() #gets everything from the miles area
		
		self.assertEqual(len(expected.keys()), len(all_data)) #the length of your expected is the same as all your data
		
		for row in all_data:
			self.assertIn(row[0], expected.keys()) #checks each row for expected
			self.assertEqual(expected[row[0]], row[1]) #makes sure amounts are equal
			
		conn.close()
		
		
	def test_vehicle_name(self):
	
	mileage.add_miles('Blue Car', 100) #adds 100 to blue car
		expected = {'BLUE CAR': 100}
		self. compare_db_to_expected(expected) #makes sure blue car is BLUE CAR
		
	