from flask import Blueprint

bp = Blueprint("test", __name__)

from app.blueprints.test import routes
