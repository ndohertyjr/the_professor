from pymongo import MongoClient
from pymongo import errors

# FIXME Set server db
client = MongoClient('localhost', 27017)


def get_mongo_connection(collection):
    if client:
        print("Mongo Client Connected")
        try:
            db = client[collection]
            return db
        except errors as e:
            print(e, "Mongo collection failed to connect!")




