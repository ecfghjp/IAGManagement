from pymongo import MongoClient

#initialise mongo client
client = MongoClient('localhost', 27017)
db_emp = client['iagemployee']
db=db_emp.employee

#retrieve al employees
def getAllEmployees():
    results = db.find()
    final = [result for result in results]
    return final

#create employees
def createEmployee(employee):
    try:
        result = db.insert_one(employee)
        return 'Ok' 
    except:
         return "Problem in saving Employee" 

#delete employees
def deleteEmployee(aid):
    result = db.delete_one({"aid":aid})
    print(result)
    return result
#update employees



#retrieve single employee
def getEmployee(aid):
    return db.find_one({"aid":aid})