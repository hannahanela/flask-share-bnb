"""Flask app for Share BnB API."""
import os
from dotenv import load_dotenv

from flask_cors import CORS
from flask import Flask, url_for, render_template, redirect, flash, jsonify, request

import uuid

import boto3
s3 = boto3.resource('s3')

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Listing

load_dotenv()
app = Flask(__name__)
# TODO: Cors Config restrict Origins to only LH3000
CORS(app)


app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_ECHO'] = True

AWS_BUCKET = os.environ['AWS_BUCKET']
AWS_BASE_URL = os.environ['AWS_BASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///share_bnb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/api', methods=["GET"])
def get_form():
    """
    Display form for creating a listing.

    """

    return render_template("file_input.html")


@app.route('/api/listings', methods=["GET"])
def get_Listings():
    """
    Get list of all listings and their data. Returns with JSON:
        {listings:[{listing}, ...]}
            listing as {username, img, description, price}
    """

    listings = Listing.query.all()
    serialized = [listing.serialize() for listing in listings]

    return jsonify(listings=serialized)


@app.route("/api/listings/<int:listing_id>", methods=["GET"])
def get_listing(listing_id):
    """
    Get data about a single listing. Returns with JSON:
        {listing: {username, img, description, price}}
    """

    listing = Listing.query.get_or_404(listing_id)
    serialize = listing.serialize()

    return jsonify(listing=serialize)


# ######################################################################### POST

@app.route("/api/listings",methods=["POST"])
def listing_create():
    """
    Creates a listing instance with title, img_key, description, price and zipcode
    to db.

    Accepts 1 file via request.files, makes a put_object request to AWS
    Stores the file in AWS bucket. Sets file extension and stores file extension
    in database as img_key.

    TODO: add other form data in docstring

    Returns with JSON:
       TODO:  {listing: {username,img, description, price}}
    """

    # TODO: Only allowed file extensions
    file_to_upload = request.files['file']
    file_proper = file_to_upload.filename

    file_extension = file_proper.split(".")[1]

    id = uuid.uuid4()

    # "Unique identifer" + "." + "file_extension"
    url = f'{AWS_BASE_URL}{id}.{file_extension}'

    # Put id + file_extension in 2 places:
    # 1. new_listing = Listing(img_key="Unique identifer" + "." + "file_extension"
    # 2. s3.Bucket(AWS_BUCKET).put_object(Key="Unique identifer" + "." + "file_extension"




    # TODO: Review how FOrmData JS is passing this to request.form in Flask.
    form_data = request.form

    title = form_data["title"]
    description = form_data["description"]
    price = int(form_data["price"])
    zipcode = form_data["zipcode"]

    # REQUEST TO AWS TO PUT IN BUCKET
    resp = s3.Bucket(AWS_BUCKET).put_object(Key=f"{id}.{file_extension}", Body=file_to_upload)

    # Creating instance of Listing Model to add to db.
    new_listing = Listing(
        title=title,
        img_key=f'{id}.{file_extension}',
        description=description,
        price=price,
        zipcode=zipcode,
        )

    db.session.add(new_listing)
    db.session.commit()

    serialize = new_listing.serialize()

    # TODO: add status code
    return jsonify(listing=serialize)

    # Alternate with Flask forms.
    # return render_template('file_input.html',url=url)


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





