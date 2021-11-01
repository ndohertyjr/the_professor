# Database controller class

from model.database import get_db
from sqlite3 import Error


"""
Controls access to the user table in the database
"""


'''
CREATE FUNCTION
'''


# Verify user does not exist in table, then add user
def add_user(user_id, username, role, points):

    db = get_db()
    cursor = db.cursor()

    query = ''' INSERT INTO users(id,username,role,points)
                VALUES(?,?,?,?) '''
    user = (user_id, username, role, points)

    if user_exists(cursor, user_id):
        print("User already exists")
    else:
        try:
            cursor.execute(query, user)
            print("User added!")
            db.commit()
        except Error as e:
            print(e, "Failed to add user to DB")

    if db:
        db.close()


'''
READ FUNCTIONS
'''


# Get user id from username
def get_user_id(username):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT id FROM users WHERE username= ? '''
    cursor.execute(query, (username,))
    user_id = cursor.fetchone()[0]
    print(user_id)
    db.close()

    return user_id


# Return all the usernames in the table sorted alphabetically
def get_all_usernames():
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT username FROM users ORDER BY username COLLATE NOCASE ASC'''
    cursor.execute(query)
    all_users = []
    for username in cursor.fetchall():
        all_users.append(username[0])
    db.close()

    return all_users


# Get username by querying the users unique id
def get_username(user_id):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT username FROM users WHERE id=?'''
    cursor.execute(query, (user_id,))
    username = cursor.fetchone()[0]
    db.close()

    return username


# Get user's current participation points based on query of their unique id
def get_user_points(user_id):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT points FROM users WHERE id=?'''
    print(user_id, "in get_user_points")
    cursor.execute(query, (user_id,))
    points = cursor.fetchone()[0]
    db.close()

    return points


'''
UPDATE FUNCTIONS
'''


# updates the username associated with user id
def update_user_name(user_id, new_username):
    db = get_db()
    cursor = db.cursor()

    update_query = ''' UPDATE users SET username = ? WHERE id = ? '''
    updated_info = new_username, user_id

    try:
        cursor.execute(update_query, updated_info)
        db.commit()
        print("Username changed for user", user_id, "to", new_username)
    except Error as e:
        print(e, "  ***Update username query failed***")
    finally:
        if db:
            db.close()


# Update user points based on a value change
def update_user_points(user_id, points_val_change):
    db = get_db()
    cursor = db.cursor()

    current_points = get_user_points(user_id)
    current_points += points_val_change

    update_query = ''' UPDATE users SET points = ? WHERE id = ? '''
    update_values = current_points, user_id
    try:
        cursor.execute(update_query, update_values)
        db.commit()
        print("Point value updated!")
    except Error as e:
        print(e, "Update failed!")
    finally:
        if db:
            db.close()


def increment_points(user_id):
    db = get_db()
    cursor = db.cursor()

    update_query = ''' UPDATE users SET points = points + 1 WHERE id = ? '''

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
DELETE FUNCTION
'''


# Delete user record by querying id
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()

    delete_query = ''' DELETE FROM users WHERE id = ? '''
    try:
        cursor.execute(delete_query, (user_id,))
        db.commit()
        print("User deleted!")
    except Error as e:
        print(e, "Delete failed!")
    finally:
        if db:
            db.close()


'''
TERTIARY FUNCTIONS
'''


# Validation function to confirm if user exists in DB
def user_exists(cursor, user_id):
    query = ''' SELECT id FROM users WHERE id=? '''
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False








