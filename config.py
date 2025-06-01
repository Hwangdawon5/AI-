# config.py

import firebase_admin
from firebase_admin import credentials, db

def firebase_connect():
    cred = credentials.Certificate("firebase_credentials.json")

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://ai-tools-pathfinder-default-rtdb.firebaseio.com'
    })

    return db
