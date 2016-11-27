#! /usr/bin/env python

from minions import app, db
from minions.models import Tracker
from flask_script import Manager, Server, prompt_bool

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0'))


@manager.command
def initdb():
    db.create_all()
    db.session.add(Tracker(name="Bob", color="Yellow", age=2))
    db.session.add(Tracker(name="Kevin", color="Yellow", age=7))
    db.session.add(Tracker(name="Stuart", color="Yellow", age=5))
    db.session.commit()
    print 'Initialized the database'


@manager.command
def dropdb():
    if prompt_bool(
            "Are you sure you want to lose all your data"):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()
