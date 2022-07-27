"""Flask app for Share BnB API."""
import os
from dotenv import load_dotenv

from pickle import GET
from webbrowser import get
from flask import Flask, url_for, render_template, redirect, flash, jsonify, request

import boto3
s3 = boto3.resource('s3')

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db
# from forms import AddPetForm, EditPetForm

load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_ECHO'] = True

AWS_BUCKET = os.environ['AWS_BUCKET']
AWS_BASE_URL = os.environ['AWS_BASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///listings"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.drop_all()
db.create_all()


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/api/listings', methods=["GET"])
def get_Listings():
    """
    Get list of all listings and their data. Returns with JSON:
        {listings:[{listing}, ...]}
            listing as {username, img, description, price}
    """

    # # TODO: Create Listing Object
    # listings = Listing.query.all()
    # # TODO: What is serializing again?
    # serialized = [cupcake.serialize() for cupcake in cupcakes]

    # # TODO:
    # return jsonify(listings=serialized)

    return render_template("file_input.html")

@app.route("/api/listings/<int:listing_id>", methods=["GET"])
def get_listing(listing_id):
    """
    Get data about a single listing. Returns with JSON:
        {listing: {username, img, description, price}}
    """
    # # TODO: Internal route logic
    # listing = Listing.query.get_or_404(listing_id)
    # serialize = listing.serialize()

    # return jsonify(listing=serialize)

    return "/api/listings/<int:listing_id>"

# ######################################################################### POST

@app.route("/api/listings",methods=["POST"])
def listing_create():
    """
    Creates a listing instance with username, img, description, price and adds
    to db.
    # Takes username, img, description, price.
    Returns with JSON:
        {listing: {username,img, description, price}}
    """

    # print ('###################################################',request)
    # print ('request.files[file] = ',request.files["file"])

    file_to_upload = request.files["file"]
    form_data = request.form
    print("Form_Data = ",form_data)

    title = form_data["title"]
    # TODO: Way to create Unique key for file naming
    #   Should occur in post route logic, not via form input.
    img_key = form_data["img_key"]
    description = form_data["description"]
    price = form_data["price"]
    zipcode = form_data["zipcode"]

    print ('############## ',title,img_key,description,price,zipcode)

    resp = s3.Bucket(AWS_BUCKET).put_object(Key='test7.jpg', Body=file_to_upload)

    url = f'{AWS_BASE_URL}{resp.key}'
    print('url = ',url)



    # FIXME: Review if changed from current to API.
    # flavor = request.json["flavor"]
    # size = request.json["size"]
    # rating = request.json["rating"]
    # image = request.json.get("image")
    # image = image if image else None

    # # alternate method
    # # image = request.get_json()["image"]

    # # TODO:
    # new_cupcake = Cupcake(
    #     flavor=flavor,
    #     size=size,
    #     rating=rating,
    #     image=image)

    # # TODO:
    # db.session.add(new_cupcake)
    # db.session.commit()

    # # TODO:
    # serialized = new_cupcake.serialize()

    # # TODO:
    # return (jsonify(cupcake=serialized), 201)

    # TODO: Return the url for the file!
    # redirect('https://c-sharebnb-r26.s3.us-west-1.amazonaws.com/')
    return render_template('file_input.html',url=url)

# ######################################################################## PATCH


@app.route('/api/listings/<int:listing_id>',methods=["PATCH"])
def listing_update_values(listing_id):
    """
    Update a listing by id. Any value(s) can be updated
    TODO: Confirm what can be updated.
    Updates instance and commits update to database.
    Returns JSON:
        {listing: {username,img, description, price}}
    """

    # text = silly_story.generate(request.args)

    # # TODO:
    # cupcake = Cupcake.query.get_or_404(cupcake_id)

    # # TODO:
    # flavor = request.json.get("flavor")
    # if flavor:
    #     cupcake.flavor = flavor

    # size = request.json.get("size")
    # if size:
    #     cupcake.size = size

    # rating = request.json.get("rating")
    # if rating:
    #     cupcake.rating = rating

    # image = request.json.get("image")
    # if image:
    #     cupcake.image = image

    # # TODO: Question on variable attributes:
    # # possible_updates = ['flavor','size','rating','image']

    # # for update in possible_updates:
    # #     if update:
    # #         cupcake.(update)

    # db.session.commit()

    # # TODO: Why dont we re-initialize cupcake after commit?
    # # cupcake = Cupcake.query.get(cupcake_id)
    # serialize = cupcake.serialize()
    # # TODO:
    # return (jsonify(cupcake=serialize))

    return '(Patch) /api/listings/<int:listing_id>'


@app.route('/api/listings/<int:listing_id>',methods=["DELETE"])
def listing_delete(listing_id):
    """
    Delete a listing instance and remove from db via id.
    Takes JSON listing ID.
    returns JSON {deleted: [listing-id]}
    """

    # # TODO:
    # cupcake = Cupcake.query.get_or_404(cupcake_id)

    # # TODO:
    # db.session.delete(cupcake)
    # db.session.commit()

    # # TODO:
    # return {"deleted":cupcake_id}

    return '(DELETE) /api/listings/<int:listing_id>'





