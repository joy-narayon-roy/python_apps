#pymongo.errors.ConfigurationError: Resolver configuration could not be read or specified no nameservers
'''
import pymongo

url38 = "mongodb+srv://MyDataBase1:njo2011njo2011@cluster0.yiali.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


urlw = "mongodb://MyDataBase1:njo2011njo2011@cluster0-shard-00-00.yiali.mongodb.net:27017,cluster0-shard-00-01.yiali.mongodb.net:27017,cluster0-shard-00-02.yiali.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-10q3rb-shard-0&authSource=admin&retryWrites=true&w=majority"
myclient = pymongo.MongoClient(url38)

print(myclient)
'''





import pymongo
from pprint import pprint
client = pymongo.MongoClient("mongodb+srv://MyDataBase1:njo2011njo2011@cluster0.yiali.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


print(dir(client))