import sqlite3
db_url = 'mileage.db' #need tables miles

def add_miles(vehicle, new_miles):

	vehicle = vehicle.upper

	if not vehicle:
		raise Exception('Provide a vehicle name')
	if isinstance(new_miles, float) or new_miles < 0:
		raise Exception('Provide a positive number for new miles')
		
	conn = sqlite3.connect(db_url)
	cursor = con.cursor()
	rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
	if rows_mod.rowcount == 0:
		cursor.execute('INSERT INTO MILES VALUES (?,?)', (vehicle, new_miles))
		
	conn.commit()
	conn.close()
	
	
def search_vehicle(vehicle):
	vehicle = vehicle.upper
	if not vehicle:
		raise Exception('Provide a vehicle name')

	conn = sqlite3.connect(db_url)
	cursor = con.cursor()
	rows_mod = cursor.execute('PRINT MILES SET total_miles WHERE vehicle = ?', (vehicle))
	if rows_mod.rowcount == 0:
		print("Car does not exist")
		
	conn.close()
	
def main():
	while True: 
		vehicle = input('Enter vehicle name or enter to quit')
		if not vehicle:
			break
		miles = float(input('Enter new miles for %s' % vehicle)) #Do input validation??
	
		add_miles(vehicle,miles)