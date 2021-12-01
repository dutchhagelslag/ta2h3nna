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

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


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


def get_test_image_url(word):
    """
    A function to return path to image to use when testing the API
    """
    # check word or something later idk probably will pivot anyways idc
    if True:
        return f"{TATTOO_HOME}/hmm.png"
