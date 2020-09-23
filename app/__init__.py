import os

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    os.getenv("ADMIN_LOGIN"): generate_password_hash(os.getenv("ADMIN_PASS")),
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


from app.blueprints.test import bp as test_bp
app.register_blueprint(test_bp, url_prefix="/test")

from app import routes, models, forms
