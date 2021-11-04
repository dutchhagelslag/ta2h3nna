"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import os

DEMO_HOME = os.path.abspath(os.curdir)

ROOMS_DB = f"{DEMO_HOME}/db/rooms.json"


def get_test_image_url(word):
    """
    A function to return path to image to use when testing the API
    """
    # check word or something later idk probably will pivot anyways idc
    if True:
        return f"{DEMO_HOME}/db/hmm.jpg"
