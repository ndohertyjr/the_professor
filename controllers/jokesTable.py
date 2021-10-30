# Joke table controller class

from model.database import get_db
from sqlite3 import Error
import random
import json

'''
Controls access to the jokes table in the database
'''

'''
CREATE functions
'''


def add_jokes():

    db = get_db()
    cursor = db.cursor()
    query = ''' INSERT INTO jokes(id,joke)
                VALUES(?,?) '''

    joke_file = open('data/jokes.json', "r")
    jokes_dict = json.load(joke_file)

    for joke_id in jokes_dict:
        joke = jokes_dict[joke_id]
        joke_object = joke_id, joke

        if joke_exists(cursor, joke):
            print("Joke already exists")
        else:
            try:
                cursor.execute(query, joke_object)
                print("Added joke!")
                db.commit()
            except Error as e:
                print(e, "Failed to add joke to DB")

    db.close()


'''
READ FUNCTIONS
'''


# Get all jokes
def get_all_jokes():
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT joke FROM jokes '''
    cursor.execute(query)

    all_jokes = []
    for joke in cursor.fetchall():
        all_jokes.append(joke[0])

    db.close()

    return all_jokes


# Get one joke
def get_random_joke():
    db = get_db()
    cursor = db.cursor()
    query = ''' SELECT joke FROM jokes WHERE id = ? '''

    num_of_jokes = len(get_all_jokes())
    random_id = random.randrange(1, num_of_jokes, 1)
    cursor.execute(query, (random_id,))

    joke = cursor.fetchone()[0]

    return joke


'''
UPDATE FUNCTIONS
'''


# Update a joke
def update_one_joke(joke_id, joke):
    db = get_db()
    cursor = db.cursor()

    update_query = ''' UPDATE jokes SET joke = ? WHERE id = ? '''
    updated_joke = joke, joke_id

    try:
        cursor.execute(update_query, updated_joke)
        db.commit()
        print("Joke changed for id", joke_id, "to", joke)
    except Error as e:
        print(e, "  ***Update joke query failed***")
    finally:
        db.close()


'''
DELETE FUNCTIONS
'''


# Delete a joke
def delete_joke(joke_id):
    db = get_db()
    cursor = db.cursor()

    delete_query = ''' DELETE FROM jokes WHERE id = ? '''
    try:
        cursor.execute(delete_query, (joke_id,))
        db.commit()
        print("Joke deleted!")
    except Error as e:
        print(e, "Delete failed!")
    finally:
        db.close()


'''
TERTIARY FUNCTIONS
'''


# Validation function to confirm if joke exists in DB
def joke_exists(cursor, joke):
    query = ''' SELECT joke FROM jokes WHERE joke=? '''
    cursor.execute(query, (joke,))
    results = cursor.fetchone()
    if results:
        return True
    else:
        return False

