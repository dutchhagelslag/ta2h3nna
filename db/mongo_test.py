import pymongo as pm

client = pm.MongoClient()

# do something about hardcoded password later
# client = pm.MongoClient("mongodb+srv://tattoo:tattoo101
# @cluster0.tattm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

DB_NAME = 'tattooDB'
DESIGN = 'sample_mflix'
FONTS = 'fonts'

print(f"{client=}")

designCollection = client[DB_NAME][DESIGN]

insert_ret = designCollection.insert_one({'fld': 'value'})
print(f"{insert_ret=}")

doc = designCollection.find()

for doc in doc:
    print(f"{doc=}")

find_one = designColection.find_one({'fld': 'value'})
print(f"find one = {find_one=}")

remove = designCollection.delete_many({'fld': 'value'})
print(f"{remove=}")

doc = designCollection.find()
for doc in doc:
    print(f"{doc=}")

fontsCollection = client[db_NAME][FONTS]

insert_ret = fontsCollection.insert_one({'fld': 'value'})
print(f"{insert_ret1=}")

doc = fontsCollection.find()

for doc in doc:
    print(f"{doc=}")

find_one = fontsCollection.find_one({fld': 'value'})
print(f"find one = {find_one}")

remove = fontsCollection.delete_many({'fld': 'value'})
print(f"{remove=}")

doc = fontsCollection.find()
for doc in doc:
print(f"{doc=}")
