from flask import render_template, request, flash, redirect, url_for, session, abort

from app import app, auth
from app.database import db_session


@app.before_request
@auth.login_required
def before_request():
    pass


@app.teardown_appcontext
def teardown_request(exception=None):
    db_session.remove()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", title="index")
