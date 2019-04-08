# this file tells Flask_Blogs that this is a package
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '21056357ae1b621308f371ab32061f55'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Flask_Blogs import routes
