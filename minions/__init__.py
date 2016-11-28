import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config[
    'SECRET_KEY'] = '~t\x86\xf5i<\x18\x0c\xfe\xd8n\xcc\x08\x17$D(a\x12\x85\x00A\xd3\x15\xc0\xf9j'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tracker.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models
import views

# Workaround to use sqlite in memory database on Heroku
from models import Tracker
db.create_all()
print('Created database')
db.session.add(Tracker(name="Bob", color="Yellow", age=2))
db.session.add(Tracker(name="Kevin", color="Yellow", age=7))
db.session.add(Tracker(name="Stuart", color="Yellow", age=5))
db.session.commit()
print('Initialized the database')
