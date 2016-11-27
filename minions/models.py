from minions import db


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
