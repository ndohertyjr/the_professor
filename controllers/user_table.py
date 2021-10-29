# Database controller class

from model.database import get_db
from sqlite3 import Error


"""
Controls access to the user table in the database
"""


# Verify user does not exist in table, then add user
def add_user(user_id, username, role, points):

    db = get_db()
    query = ''' INSERT INTO users(id,username,role,points)
                VALUES(?,?,?,?) '''
    user = (user_id, username, role, points)
    cursor = db.cursor()

    if user_exists(cursor, user_id):
        print("User already exists")
    else:
        try:
            cursor.execute(query, user)
            print("Added!")
            db.commit()
        except Error as e:
            print(e, "Failed to add user to DB")

    db.close()


# Validation function to confirm if user exists in DB
def user_exists(cursor, user_id):
    query = ''' SELECT id FROM users WHERE id=? '''
    cursor.execute(query, (user_id,))
    results = cursor.fetchone()
    if results:
        return True
    else:
        return False


# Get user id from username
def get_user_id(username):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT id FROM users WHERE username=? '''
    cursor.execute(query, (username,))
    user_id = cursor.fetchone()[0]
    print(user_id)
    db.close()

    return user_id


# Return all the usernames in the table sorted alphabetically
def get_all_usernames():
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT username FROM users ORDER BY username ASC'''
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


# Get user role by querying users unique id
def get_user_role(user_id):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT role FROM users WHERE id=?'''
    cursor.execute(query, (user_id,))
    role = cursor.fetchone()[0]
    db.close()

    return role


# Get user's current participation points based on query of their unique id
def get_user_points(user_id):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT points FROM users WHERE id=?'''
    cursor.execute(query, (user_id,))
    points = cursor.fetchone()[0]
    db.close()

    return points

# FIXME update user name needed?
def update_user_name(user_id):
    pass


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
        db.close()


# Delete user record by quering id
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
        db.close()








