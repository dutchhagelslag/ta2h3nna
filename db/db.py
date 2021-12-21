import os
import pymongo as pm
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


def get_designs():
    """
    Returns list of the types of artists
    """
    names = []

    collection = dbc.fetch_all("designs")
    for x in collection:
        names.append(x['name'])

    return names


def get_artists():
    """
    Returns list of the types of artists
    """
    names = []

    collection = dbc.fetch_all("artists")
    for x in collection:
        names.append(x['name'])
    return names


def get_fonts():
    """
    Returns list of the types of fonts
    """
    names = []

    collection = dbc.fetch_all("fonts")
    for x in collection:
        names.append(x['name'])

    return names




def font_exists(name):
    """
    See if font exists in DB
    Returns True of False.
    """
    rec = dbc.fetch_one("fonts", filters={"name": name})
    print(rec)
    return rec is not None


def design_exists(name):
    """
    See if design exists in DB
    Returns True of False.
    """
    rec = dbc.fetch_one("designs", filters={"name": name})
    print(rec)
    return rec is not None

