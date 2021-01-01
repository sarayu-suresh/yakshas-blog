import pyrebase
from os import environ


firebaseConfig = {
    'apiKey': "AIzaSyA84q6tGmLOqchjRTXvQa9nI8-OhbkJsHk",
  'authDomain': "yakshas-blog.firebaseapp.com",
  'databaseURL': "https://yakshas-blog-default-rtdb.firebaseio.com",
  'projectId': "yakshas-blog",
  'storageBucket': "yakshas-blog.appspot.com",
  'messagingSenderId': "499297033450",
  'appId': "1:499297033450:web:da142bca0fbcbc20ff0b93",
  'measurementId': "G-BY2TP5GBGK"
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