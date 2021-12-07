import pymongo as pm
import bson


client = pm.MongoClient()
print(client)
db = client["DesignsDB"]
print(db)
