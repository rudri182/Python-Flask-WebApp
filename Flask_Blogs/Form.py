from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Flask_Blogs.models import User, Post

class Registration(FlaskForm):  #imported from FlaskForm
    username = StringField('Username' , validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email' , validators = [DataRequired(), Email() ] )
    password = PasswordField('Password' , validators = [DataRequired()])
    confirm_pass = PasswordField('Conform Password', validators = [DataRequired(), EqualTo('password') ])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()   #first occurrence of this username
        if user:
            raise ValidationError("This username is already taken. Please chose another one. ")

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()   #first occurrence of this username
        if user:
            raise ValidationError("This email is already taken. Please chose another one. ")

class Login(FlaskForm):  #imported from FlaskForm
    email = StringField('Email' , validators = [DataRequired(), Email() ] )
    password = PasswordField('Password' , validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UpdateAccount(FlaskForm):  #imported from FlaskForm
    username = StringField('Username' , validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email' , validators = [DataRequired(), Email() ] )
    profile_picture = FileField('Update profile picture', validators= [FileAllowed(['png' , 'jpg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()   #first occurrence of this username
            if user:
                raise ValidationError("This username is already taken. Please chose another one. ")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()   #first occurrence of this username
            if user:
                raise ValidationError("This email is already taken. Please chose another one. ")

class PostForm(FlaskForm):
    title = StringField('Title' , validators = [DataRequired()])
    content = TextAreaField('Content' , validators= [DataRequired()])
    submit = SubmitField('Post')
