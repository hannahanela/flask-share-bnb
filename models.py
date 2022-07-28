"""Models for Share BnB app."""

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

############################# Classes ##########################################

######## The One in "One-Many"
class Listing(db.Model):
    """
    Creates a ... instance.
    Class Methods:
    """

    __tablename__ = "listings"

    # id
    # listing_name or title
    # listing_url
    # user foreign key
    # price
    # description
    # location
    # zipcode
    # availability (booking status?)

# Always check that Column is uppercase. Common bug.
# Primary key auto sets nullable = False, & unique=True
    id = db.Column(
        db.Integer,
        autoincrement=True,
        primary_key=True,
    )

    title = db.Column(
        db.String(30),
        nullable=False,
        unique=True,
    )

    img_key = db.Column(
        db.String,
        nullable=False,
        unique=True,
        # TODO: default would be great!
    )

    description = db.Column(
        db.Text,
        nullable=False,
        )

    price = db.Column(
        db.Integer,
        # db.Numeric,
        nullable=False,
        )

    zipcode = db.Column(
        db.String(5),
        nullable=False,
    )

    def serialize(self):
        """Serialize to dictionary."""

        return { 
            "id": self.id,
            "title": self.title,
            "img_key": self.img_key,
            "description": self.description,
            "price": self.price,
            "zipcode": self.zipcode,
        }

#############   Class methods; cls is the self equivalent of Classes. ##########
# Example register a user. Called on the Class instance.
#     @classmethod
#     def register(cls, username, password, email, first_name, last_name):
#         """
#         Register user w/hashed password & return user.
#         Returns a new user instance
#         """

#         hashed = bcrypt.generate_password_hash(password).decode('utf8')

#         # return instance of user w/username and hashed pwd
#         return cls(
#             username=username,
#             password=hashed,
#             email=email,
#             first_name=first_name,
#             last_name=last_name)

# #       Example Authentication of user.
#     @classmethod
#     def authenticate(cls, username, password):
#         """
#         Validate that a user exists and that the password matches stored
#         hashed value in database.
#         Accepts username,password.
#         Returns User Instance
#         """

#         user = cls.query.filter_by(username=username).one_or_none()

#         if user and bcrypt.check_password_hash(user.password, password):
#             return user
#         else:
#             return False

# ################### Example foreign Key/ backref relationship ###############
# # The Many in "One-Many"
# class ModelNameMany...(db.Model):
#     """
#     Creates a ... instance.
#     """

#     __tablename__ = "B..."

#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#         autoincrement=True)
#     owner = db.Column(
#         db.String(20),
#         db.ForeignKey('A.column_name_2'))

#     users = db.relationship('ModelNameOne...', backref='B')

# ####################################################################
