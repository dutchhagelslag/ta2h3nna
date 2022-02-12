"""
This file contains some common MongoDB code.
"""
import os
# import json
import pymongo as pm


db_nm = "tattooDB"


def get_client():
    """
    This provides a uniform way to get the client across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    """
    global client
    global db_tattoo
    client = pm.MongoClient("mongodb+srv://tattoo:tattoo101@cluster0.tattm."
                            "mongodb.net/myFirstDatabase?retryWrites=true&w"
                            "=majority")

    db_tattoo = client[db_nm]

    if os.environ.get("LOCAL_MONGO", False):
        client = pm.MongoClient()
    return client


# def fetch_all(collect_nm):
#     """
#     Fetch collection given a collection name
#     """
#     return db_tattoo[collect_nm].find()

    # all_docs = []
    # for doc in db_tattoo[collect_nm].find({},{"_id":0,"name":1}):
    #     print(doc)
    #     all_docs += doc["name"]
    # return all_docs
