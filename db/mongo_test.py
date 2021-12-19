import pymongo as pm

client = pm.MongoClient()

# do something about hardcoded password later
# client = pm.MongoClient("mongodb+srv://tattoo:tattoo101@cluster0.tattm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

DB_NAME = 'tattooDB'
DESIGN  = 'sample_mflix'
FONTS = 'fonts'

print(f"{client=}")

designCollection = client[DB_NAME][DESIGN]

insert_ret = designCollection.insert_one({'fld':'value'})
print(f"{insert_ret=}")

doc = designCollection.find()

for doc in doc:
    print(f"{doc=}")

remove = designCollection.delete_one({'fld':'value'})
print(f"{remove=}")
