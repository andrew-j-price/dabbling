from flask import flash, jsonify, redirect, render_template, request, url_for
import socket

from minions import app, db
from forms import TrackerFormToInsert, TrackerFormToDelete
from models import Tracker


@app.route('/')
@app.route('/index', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/add', strict_slashes=False, methods=['GET', 'POST'])
def add():
    form = TrackerFormToInsert()
    if form.validate_on_submit():
        name = form.name.data
        color = form.color.data
        age = form.age.data
        record = Tracker(name=name, color=color, age=age)
        db.session.add(record)
        db.session.commit()
        flash("Stored '{}'".format(name))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/delete', strict_slashes=False, methods=['GET', 'POST'])
def delete():
    form = TrackerFormToDelete()
    if form.validate_on_submit():
        uuid = form.uuid.data
        Tracker.query.filter_by(id=uuid).delete()
        db.session.commit()
        flash("Stored '{}'".format(uuid))
        return redirect(url_for('index'))
    return render_template('delete.html', form=form)


@app.route('/view', strict_slashes=False, methods=["GET"])
def view():
    records = Tracker.query.order_by(Tracker.name).all()
    for i in records:
        print i.name
    return render_template('view.html', records=records)


@app.route("/host", strict_slashes=False, methods=["GET"])
@app.route("/hostname", strict_slashes=False, methods=["GET"])
def api_root():
    return socket.gethostname() + '\n'


@app.route("/ip", strict_slashes=False, methods=["GET"])
def api_ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route('/ping', strict_slashes=False, methods=["GET"])
def api_ping():
    return jsonify(ping='pong')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500
