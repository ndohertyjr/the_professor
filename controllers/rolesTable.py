# Roles table controller class

from model.database import get_db
from sqlite3 import Error

'''
Controls access to the jokes table in the database
'''


'''
CREATE functions
'''


def add_role(role_id, role_name):
    db = get_db()
    cursor = db.cursor()

    query = ''' INSERT INTO roles(id, role)
                VALUES(?,?) '''

    role_data = role_id, role_name

    if role_exists(cursor, role_id):
        print("Role already exists")
    else:
        try:
            cursor.execute(query, role_data)
            print("Role added!")
            db.commit()
        except Error as e:
            print(e, "Failed to add role to DB")

    if db:
        db.close()


'''
READ FUNCTIONS
'''


# Get role by querying role's unique id
def get_role_name(role_id):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT role FROM roles WHERE id = ? '''
    cursor.execute(query, (role_id,))
    role = cursor.fetchone()[0]
    db.close()

    return role


# Get role id by querying role's name
def get_role_id(role_name):
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT id FROM roles WHERE role = ? '''
    cursor.execute(query, (role_name,))
    role_id = cursor.fetchone()[0]
    db.close()

    return role_id


# Get role by querying role's unique id
def get_all_roles():
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT * FROM roles'''
    cursor.execute(query)

    all_roles = cursor.fetchall()

    db.close()

    return all_roles


'''
UPDATE FUNCTIONS
'''


# updates the role associated with role id
def update_role(role_id, new_role):
    db = get_db()
    cursor = db.cursor()

    update_query = ''' UPDATE roles SET role = ? WHERE id = ? '''
    updated_info = new_role, role_id

    try:
        cursor.execute(update_query, updated_info)
        db.commit()
        print("Role changed for ID", role_id, "to", new_role)
    except Error as e:
        print(e, " *** Update role query failed ***")
    finally:
        if db:
            db.close()


'''
DELETE FUNCTIONS
'''


# deletes role based on role id
def delete_role(role_id):
    db = get_db()
    cursor = db.cursor()

    delete_query = ''' DELETE FROM roles WHERE id = ?'''

    try:
        cursor.execute(delete_query, (role_id,))
        db.commit()
        print("Role deleted!")
    except Error as e:
        print(e, "Delete failed!")
    finally:
        if db:
            db.close()


'''
TERTIARY FUNCTIONS
'''


def role_exists(cursor, role_id):
    query = ''' SELECT id FROM roles WHERE id = ? '''
    cursor.execute(query, (role_id,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
