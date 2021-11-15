# MongoDB controller class

from pymongo import errors
from model.mongoModel import get_mongo_connection
from model.schemas import user_schema

# Load env data
from dotenv import load_dotenv
import os
db = os.getenv("DB_NAME")
connection = get_mongo_connection(db)
user_col = connection.users


"""
Controls access to the user table in the database
"""


'''
CREATE FUNCTION
'''


def add_user_mongo(user_id, username, points):

    user = user_schema(user_id, username, points)

    # Validate if user is in DB.  If not, add them.
    if user_col.find_one({"discord_ID":user_id}):
        print("exists")

    else:
        try:
            user_col.insert_one(user)
            print("Success")
        except errors as e:
            print(e, "Add user failed!")


'''
READ FUNCTIONS
'''


# Get user id from username
def get_user_id(username):

    user = user_col.find_one({"name": username})

    if user:
        user_id = user['discord_ID']
        return user_id

    else:
        print("No user found")


# Get user id from username
def get_username(user_id):
    user = user_col.find_one({"discord_ID": user_id})

    if user:
        username = user['name']
        return username

    else:
        print("No user found")

# Gets all usernames and returns sorted array
def get_all_usernames():
    cursor = user_col.find().sort("name")

    all_users = []

    for document in cursor:
        all_users.append(document['name'])

    cursor.close()
    return all_users

# Gets user points for user id
def get_user_points(user_id):
    user = user_col.find_one({"discord_ID": user_id})
    points = user['points']

    return points

# Gets user roles for user id
def get_user_roles(user_id):
    user = user_col.find_one({"discord_ID": user_id})
    roles = user['roles']

    return roles

'''
UPDATE FUNCTIONS
'''


# updates the username associated with user id
def update_user_name(user_id, new_username):
    query = {"discord_ID": user_id}
    new_name = { "$set": {"name": new_username}}

    try:
        user_col.update_one(query, new_name)
        print("Username changed for user", user_id, "to", new_username)
    except errors as e:
        print(e, "  ***Update username query failed***")


# updates the points associated with user id
def update_user_points(user_id, new_points):
    query = {"discord_ID": user_id}
    new_point_total = {"$set": {"points": new_points}}

    try:
        user_col.update_one(query, new_point_total)
        print("Points changed for user", user_id, "to", new_points)
    except errors as e:
        print(e, "  ***Update points query failed***")


# Adds a new role to the user profile
def add_new_user_role(user_id, new_role_id, new_role_name):
    query = {"discord_ID": user_id}
    added_role = {"$push": {"roles": {"role_id": new_role_id, "role_name": new_role_name}}}

    try:
        user_col.update_one(query, added_role)
        print("Role added to user", user_id, "of", new_role_name, "with ID", new_role_id)
    except errors as e:
        print(e, "  ***Update points query failed***")


'''
DELETE FUNCTIONS
'''


# Delete user record by querying id
def delete_user(user_id):
    query = {"discord_ID": user_id}

    try:
        user_col.delete_one(query)
        print("User deleted!")
    except errors as e:
        print(e, "Delete failed!")


# Delete user role by querying id
def delete_user_role(user_id, role_id):
    query = {"discord_ID": user_id}
    role_remove = {"$pull": {"roles": {"role_id": role_id}}}

    try:
        user_col.update_one(query, role_remove)
        print("Role deleted!")
    except errors as e:
        print(e, "Role delete failed!")


'''
TERTIARY FUNCTIONS
'''

'''
def increment_points(user_id):
    query = {"discord_ID": user_id}
    new_point_total = {"$set": {"points": new_points}}

    try:
        cursor.execute(update_query, (user_id,))
        db.commit()
        print("Incremented points by 1")
    except Error as e:
        print(e, "Increment failed!")
    finally:
        if db:
            db.close()



'''
