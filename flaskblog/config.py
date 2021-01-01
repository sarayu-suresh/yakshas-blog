# Needed setting secret key, email and psswd
from os import environ
from boto.s3.connection import S3Connection
class Config:
    SECRET_KEY = S3Connection(environ.get('SECRET_KEY'))
    SQLALCHEMY_DATABASE_URI = S3Connection(environ.get('DATABASE_URL')) or 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = S3Connection(environ.get('USER'))
    MAIL_PASSWORD = S3Connection(environ.get('password'))
