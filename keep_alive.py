from flask import Flask
from threading import Thread

"""
Purpose: create a web site that can be pinged to ensure the repl service stays active
"""

app = Flask('')


@app.route('/')
def home():
    return "Hello! I am alive"


def run():
    app.run(host='0.0.0.0', port=8000)


def keep_alive():
    t = Thread(target=run)
    t.start()
