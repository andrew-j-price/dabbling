import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config[
    'SECRET_KEY'] = '~t\x86\xf5i<\x18\x0c\xfe\xd8n\xcc\x08\x17$D(a\x12\x85\x00A\xd3\x15\xc0\xf9j'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'tracker.db')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models
import views
