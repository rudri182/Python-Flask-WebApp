'''import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from Flask_Blogs import  db, bcrypt, mail
from flask import  create_app
from Flask_Blogs.models import User, Post
from Flask_Blogs.Form import (Registration, Login, UpdateAccount, PostForm,
                              RequestReset, ResetPassword)
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
'''
