# Needed setting secret key, email and psswd
class Config:
    SECRET_KEY = 'qwertyuiop'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'yakshas2k19.23@gmail.com'
    MAIL_PASSWORD = 'Cserit2k19'
