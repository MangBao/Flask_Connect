import os
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
# DEBUG = True
# # Connect to the database
# SQLALCHEMY_DATABASE_URI = 'your psycopg2 URI connection'
# # Turn off the Flask-SQLAlchemy event system and warning
# SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)