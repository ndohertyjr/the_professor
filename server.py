# Script that creates server for bot to remain online.

from flask import Flask
from threading import Thread

app = Flask('')


# Response to all server requests
@app.route('/')
def home():
    return "I am online."

# TODO Add CRUD for the database


def run():
    # TODO Potentially add reloader to refresh updates without manually restarting the server
    app.run(host='0.0.0.0', port=8080)


def keep_online():
    t = Thread(target=run)
    t.start()

