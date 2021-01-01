import pyrebase
from os import environ


firebaseConfig = {
    "apiKey": environ.get('apiKey'),
    "authDomain": environ.get('authDomain'),
    'databaseURL': environ.get('databaseURL'),
    "projectId": "yakshas-blog",
    "storageBucket": environ.get('storageBucket'),
    "messagingSenderId": environ.get('messagingSenderId'),
    "appId": environ.get('appId'),
    "measurementId": environ.get('measurementId')
    }


def storage():
    firebase = pyrebase.initialize_app(firebaseConfig)
    fstore = firebase.storage()
    return fstore


def prof_pic(current_user):
    firebase = pyrebase.initialize_app(firebaseConfig)
    fstore = firebase.storage()
    url = fstore.child('images/'+current_user).get_url(None)
    return url


def prof_img(current_user):
    if current_user.is_authenticated:
        pic = prof_pic(current_user.image_file)
    else:
        pic = None
    return pic