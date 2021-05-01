import pymongo

dburl = 'vipi.local'
myclient = pymongo.MongoClient(dburl)
#help(myclient)
print(myclient.database_names())
mydb = myclient['testdb']

def testinsert():
    mycol = mydb["customers"]
    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)

def getdocuments(dbname):
    db = myclient[dbname]
    print(db.collection_names())
    for i in db.collection_names()[1:]:
        for j in db[i].find():
            print(j)

getdocuments('testdb')

def insertitem(itemname, locationname, quantity=1):
    mycol = mydb['storage']
    dict = {'name': itemname, }
