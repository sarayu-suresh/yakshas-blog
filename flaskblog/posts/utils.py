import os
import secrets
from PIL import Image
from flask import current_app
from flaskblog import firebase_storage


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/pictures', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    storage = firebase_storage.storage()
    storage.child("images/" + picture_fn).put(picture_path)

    return picture_fn
