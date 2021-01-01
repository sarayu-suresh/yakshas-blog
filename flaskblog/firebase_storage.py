import pyrebase
from os import environ
from boto.s3.connection import S3Connection


firebaseConfig = {
    "apiKey": S3Connection(environ.get('apiKey')),
    "authDomain": S3Connection(environ.get('authDomain')),
    'databaseURL': S3Connection(environ.get('databaseURL')),
    "projectId": "yakshas-blog",
    "storageBucket": S3Connection(environ.get('storageBucket')),
    "messagingSenderId": S3Connection(environ.get('messagingSenderId')),
    "appId": S3Connection(environ.get('appId')),
    "measurementId": S3Connection(environ.get('measurementId'))
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