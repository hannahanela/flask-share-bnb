from app import app
import os
from dotenv import load_dotenv
from models import db, Listing

load_dotenv()

L1_IMG_KEY = os.environ['L1_IMG_KEY']
L2_IMG_KEY = os.environ['L2_IMG_KEY']
L3_IMG_KEY = os.environ['L3_IMG_KEY']
L4_IMG_KEY = os.environ['L4_IMG_KEY']
L5_IMG_KEY = os.environ['L5_IMG_KEY']


db.drop_all()
db.create_all()

l1 = Listing(
    title="Pool-side Oasis",
    img_key=f"{L1_IMG_KEY}",
    description="Escape to a beautiful pool-side oasis away from the city.",
    price=190.00,
    zipcode="94118",
)

l2 = Listing(
    title="Rustic Patio",
    img_key=f"{L2_IMG_KEY}",
    description="Enjoy this rustic patio nestled in one of SF's hottest neighborhoods!",
    price=125.00,
    zipcode="94117",
)

l3 = Listing(
    title="Large Yard",
    img_key=f"{L3_IMG_KEY}",
    description="A large yard for events.",
    price=35.00,
    zipcode="95811",
)

l4 = Listing(
    title="Perfect Patio",
    img_key=f"{L4_IMG_KEY}",
    description="The perfect patio for your next family event.",
    price=75.00,
    zipcode="94110",
)

l5 = Listing(
    title="Pool",
    img_key=f"{L5_IMG_KEY}",
    description="Great pool for parties. Screened.",
    price=68.00,
    zipcode="95833",
)

# TODO: seed data
db.session.add_all([l1, l2, l3, l4, l5])
db.session.commit()
