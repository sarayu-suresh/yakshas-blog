import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail, firebase_storage
#import pyrebase


# firebaseConfig = {
#     "apiKey": "AIzaSyA84q6tGmLOqchjRTXvQa9nI8-OhbkJsHk",
#     "authDomain": "yakshas-blog.firebaseapp.com",
#     'databaseURL': "https://yakshas-blog-default-rtdb.firebaseio.com/",
#     "projectId": "yakshas-blog",
#     "storageBucket": "yakshas-blog.appspot.com",
#     "messagingSenderId": "499297033450",
#     "appId": "1:499297033450:web:da142bca0fbcbc20ff0b93",
#     "measurementId": "G-BY2TP5GBGK"
#     }
#
# firebase = pyrebase.initialize_app(firebaseConfig)
# storage = firebase.storage()


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    #output_size = (125, 125)
    #i = Image.open(form_picture)
    #i.thumbnail(output_size)

    storage = firebase_storage.storage()
    storage.child("images/" + picture_fn).put(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{ url_for('users.reset_token', token=token, _external=True) }

If you did not make this request then please ingnore this mail.
'''
    mail.send(msg)