import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')  #pushed to environment variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')    #good practice to keep
                                                        #it in environment variables
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  #set environmental variables
    MAIL_PASS = os.environ.get('EMAIL_PASS')
