from app import app
from models import db, Cupcake

db.drop_all()
db.create_all()

# TODO: seed data
# db.session.add_all()
# db.session.commit()
