# import os
# import pymongo as pm
import db.db_connect as dbc

# TATTOO_HOME = os.environ["TATTOO_HOME"]
# TEST_MODE = os.environ.get("TEST_MODE", 0)

# if TEST_MODE:
#     DB_DIR = f"{TATTOO_HOME}/db/test_dbs"
# else:
#     DB_DIR = f"{TATTOO_HOME}/db"

# FONTS_COLLECTION = f"{DB_DIR}/fonts.json"
# DESIGNS_COLLECTION = f"{DB_DIR}/designs.json"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

# #we'll begin cutting over to mongo!
# if os.environ.get("LOCAL_MONGO", False):
# else:
#     client = pm.MongoClient()
# print(client)

client = dbc.get_client()

if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)

db_tattoo = client.tattooDB


def upload_design_meta(data):
    """
    Upload designs info
    """
    db_tattoo["designs"].insert_one(data)


def get_designs():
    """
    Returns collection of designs
    """
    return db_tattoo["designs"]


# def get_artists():
#     """
#     Returns collection of artists
#     """
#     return db_tattoo["artists"]


# def design_exists(name):
#     """
#     See if design exists in DB
#     Returns True of False.
#     """
#     rec = dbc.fetch_one("designs", filters={"name": name})
#     return rec is not None
