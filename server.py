# Script that creates server for bot to remain online.

from flask import Flask
from threading import Thread
from dotenv import load_dotenv
import os

app = Flask('')
IP_ADDRESS = os.getenv("IP")


# Response to all server requests
@app.route('/')
def home():
    return "I am online."

# TODO Add CRUD for the database


def run():
    # TODO Potentially add reloader to refresh updates without manually restarting the server, fix IP
    print(IP_ADDRESS)
    app.run(host=IP_ADDRESS, port=8080)


def keep_online():
    t = Thread(target=run)
    t.start()

