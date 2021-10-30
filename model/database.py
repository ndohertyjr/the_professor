# Database controller class
# API will check if DB exists, if not it will create DB and required tables

import sqlite3
from sqlite3 import Error

# db path
DATABASE_NAME = "theProfessor.db"


# Check if local system has a database and create if needed:
def create_connection():
    db = None

    try:
        db = sqlite3.connect(DATABASE_NAME)
        print(sqlite3.version)
    except Error as e:
        print(e + " Connection to DB failed!")
    finally:
        if db:
            db.close()


# Create tables if they don't exist
def create_user_table():
    try:
        db = sqlite3.connect(DATABASE_NAME)
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT,
                role TEXT,
                points INTEGER
            )    
        ''')
        db.commit()
        print("USER TABLE EXISTS!")

    except Error as e:
        print(e)
    finally:
        if db:
            db.close()


# create jokes table if it doesn't exist
def create_jokes_table():
    try:
        db = sqlite3.connect(DATABASE_NAME)
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jokes(
                id INTEGER PRIMARY KEY,
                joke TEXT
            )
        ''')
        db.commit()
        print("JOKES TABLE CREATED")

    except Error as e:
        print(e, "***JOKE TABLE FAILED TO BE BORN***")

    finally:
        if db:
            db.close()


# Returns db connection for controllers
def get_db():
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        return connection
    except Error as e:
        print(e)



