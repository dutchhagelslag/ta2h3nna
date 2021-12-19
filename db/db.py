"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

TATTOO_HOME = os.environ["TATTOO_HOME"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    DB_DIR = f"{TATTOO_HOME}/db/test_dbs"
else:
    DB_DIR = f"{TATTOO_HOME}/db"

FONTS_COLLECTION = f"{DB_DIR}/fonts.json"
DESIGNS_COLLECTION = f"{DB_DIR}/designs.json"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

# #we'll begin cutting over to mongo!
# if os.environ.get("LOCAL_MONGO", False):
# else:
#     client = pm.MongoClient()
# print(client)


def write_collection(perm_version, mem_version):
    """
    Write out the in-memory data collection in proper DB format.
    """
    with open(perm_version, 'w') as f:
        json.dump(mem_version, f, indent=4)


def read_collection(perm_version):
    """
    A function to read a colleciton off of disk.
    """
    try:
        with open(perm_version) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print(f"{perm_version} not found.")
        return None


def get_fonts():
    """
    List all types of fonts
    """
    return read_collection(FONTS_COLLECTION)


def get_designs():
    """
    A function to return a dictionary of all designs.
    """
    return read_collection(DESIGNS_COLLECTION)
    # return client[DB_NAME][ROOMS].to_json()


def design_exists(design_name):
    designs = get_designs
    return design_name in designs


def del_design(design_name):
    """
    Delete design from the db.
    """
    if not design_exists(design_name):
        return NOT_FOUND
    return OK


# def add_design(design_name):
#     """
#     Add a room to the room database.
#     Until we are using a real DB, we have a potential
#     race condition here.
#     """
#     designs = get_designs()
#     if designs is None:
#         return NOT_FOUND
#     elif design_name in designs:
#         return DUPLICATE
#     else:
#         designs[design_name] = {"": 0}
#         write_collection(DESIGNS_COLLECTION, designs)
#         return OK
