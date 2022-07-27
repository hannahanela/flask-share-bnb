"""Models for Share BnB API."""
from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt()

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
