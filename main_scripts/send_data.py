from pymongo import MongoClient # import mongo client to connect  

def sendDb(emplid,location,time):
	client = MongoClient('mongodb://192.168.0.126:27017')  
	print ("connected to db")
	# Creating database  
	db = client.db4  
	employee = {"emp_id": emplid,  
	"location": location,  
	"time": time,  
	}  
	# Creating document  
	print (employee)
	employees = db.sample  
	# Inserting data  
	employees.insert(employee)  
	# Fetching data  
	print ("data inserted")
	print (employees.find())

if __name__ == '__main__':
    sendDb(34234,"tower1","5:00")
