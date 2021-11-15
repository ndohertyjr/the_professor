# Roles collection controller class

from pymongo import errors
from model.mongoModel import get_mongo_connection
from model.schemas import role_schema

# Load env data
from dotenv import load_dotenv
import os
db = os.getenv("DB_NAME")
connection = get_mongo_connection(db)
role_col = connection.roles

'''
Controls access to the roles table in the database
'''


'''
CREATE functions
'''


def add_role(role_id, role_name, role_max_pts):

    role = role_schema(role_id, role_name, role_max_pts)

    if role_col.find_one({'role_id': role_id}):
        print('exists')
    else:
        try:
            role_col.insert_one(role)
            print('success')
        except errors as e:
            print(e, "Failed to add role to DB")


'''
READ FUNCTIONS
'''


# Get role by querying role's unique id
def get_role_name(role_id):

    role = role_col.find_one({"role_id": role_id})

    if role:
        role_name = role['role_name']
        return role_name
    else:
        print('Role not found')


# Get role id by querying role's name
def get_role_id(role_name):

    role = role_col.find_one({"role_name": role_name})

    if role:
        role_id = role['role_id']
        return role_id
    else:
        print('Role not found')


# Get all roles
def get_all_roles():
    cursor = role_col.find().sort("role_name")

    all_roles = []

    for document in cursor:
        all_roles.append(document['role_name'])

    cursor.close()
    return all_roles


# Get role max points by querying role's unique id
def get_role_max_pts(role_id):
    role = role_col.find_one({"role_id": role_id})

    if role:
        max_pts = role['max_pts']
        return max_pts
    else:
        print('Points not found')


'''
UPDATE FUNCTIONS
'''


# updates the role name associated with role id
def update_role(role_id, new_name):
    query = {"role_id": role_id}
    new_role_name = { "$set" : {"role_name": new_name}}

    try:
        role_col.update_one(query, new_role_name)
        print("Role name changed for ID", role_id, "to", new_name)
    except errors as e:
        print(e, " *** Update role name query failed ***")


def update_max_pts(role_id, new_pts):
    query = {"role_id": role_id}
    new_max_pts = {"$set": {"max_pts": new_pts}}

    try:
        role_col.update_one(query, new_max_pts)
        print("Max pts changed for ID", role_id, "to", new_pts)
    except errors as e:
        print(e, " *** Update max pts query failed ***")


# deletes role based on role id
def delete_role(role_id):
    query = {"role_id": role_id}

    try:
        role_col.delete_one(query)
        print("Role deleted!")
    except errors as e:
        print(e, "Delete failed!")


