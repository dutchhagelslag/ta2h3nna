import pymongo as pm

client = pm.MongoClient()
print(client)
db = client["DesignsDB"]
print(db)
