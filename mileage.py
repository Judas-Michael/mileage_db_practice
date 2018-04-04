import sqlite3
db_url = 'mileage.db' #need tables miles

def add_miles(vehicle, new_miles):

	vehicle = vehicle.upper() #puts vehicle variable to uppercase

	if not vehicle:
		raise Exception('Provide a vehicle name') #if the vehicle doesn't exist throw exception 
	if isinstance(new_miles, float) or new_miles < 0: #if the miles added are negative of a float throw exception. We only want positive round numbers
		raise Exception('Provide a positive number for new miles')
		
	conn = sqlite3.connect(db_url) #connects to database
	cursor = con.cursor() #assigns cursor for database
	rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle)) #finds rows to nmodify
	if rows_mod.rowcount == 0: #if there aren't any rows to modify
		cursor.execute('INSERT INTO MILES VALUES (?,?)', (vehicle, new_miles)) #add vehicle + miles to database if they don't exist
		
	conn.commit() #changes
	conn.close() #closes db
	
	
def search_vehicle(vehicle):
	vehicle = vehicle.upper() # puts vehichle variable to uppercase
	if not vehicle:
		raise Exception('Provide a vehicle name') #looks for valid vehicle name

	conn = sqlite3.connect(db_url) #connects db
	cursor = con.cursor()#connects cursor
	rows_mod = cursor.execute('PRINT MILES SET total_miles WHERE vehicle = ?', (vehicle)) #looks for conditions
	if rows_mod.rowcount == 0: #if conditions are not met
		print("Car does not exist") #car doesn't exist
		
	conn.close() #close db
	
def main():
	while True: 
		vehicle = input('Enter vehicle name or enter to quit') #gets vehicle name
		if not vehicle:
			break #breaks if the name is wrong/ doesn't exist
		miles = float(input('Enter new miles for %s' % vehicle)) #Do input validation??
	
		add_miles(vehicle,miles) #adds vehicle and miles