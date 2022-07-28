"""Flask app for Share BnB API."""
import os
from dotenv import load_dotenv

from flask_cors import CORS

# from pickle import GET
# from webbrowser import get
from flask import Flask, url_for, render_template, redirect, flash, jsonify, request

import uuid

import boto3
s3 = boto3.resource('s3')

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Listing
# from forms import AddPetForm, EditPetForm

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
# db.drop_all()
# db.create_all()


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
    # # TODO: Internal route logic
    listing = Listing.query.get_or_404(listing_id)
    serialize = listing.serialize()

    return jsonify(listing=serialize)

    # return "/api/listings/<int:listing_id>"

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

    # TODO: Allowed file extensions

    file_to_upload = request.files["file"]
    print ('###################################################',request.files)
    print ('request.files[file] = ',request.files["file"])
    print('file_to_upload.filename = ',file_to_upload.filename)
    file_proper = file_to_upload.filename
    file_extension = file_proper.split(".")[1]
    print ("THE FILE EXTENSION!!! = ", file_extension)

    # We have the file extension
    id = uuid.uuid4()

    #
    # "Unique identifer" + "." + "file_extension"

    url = f'{AWS_BASE_URL}{id}.{file_extension}'
    print('url = ',url)



    # Put in 2 places
    # 1. new_listing = Listing(img_key="Unique identifer" + "." + "file_extension"
    # 2. s3.Bucket(AWS_BUCKET).put_object(Key="Unique identifer" + "." + "file_extension"




    # FIXME: FORM DATA CONNECTED TO TEMPLATE
    # form_data = request.form
    # # print("Form_Data = ",form_data)

    # title = form_data["title"]
    # description = form_data["description"]
    # price = int(form_data["price"])
    # zipcode = form_data["zipcode"]


    # TODO: API REQUEST FROM REACT
    request_data = request.json
    print ("************request_data=", request_data)
    title = request_data["title"]
    description = request_data["description"]
    price = int(request_data["price"])
    zipcode = request_data["zipcode"]

    print ("request data =", title, description, price, zipcode)

    return jsonify("woo!", 206)



    # basic async, method POST data = React formData
    # url localhost:5000 (.env) 

    # print ('############## ',title,img_key,description,price,zipcode)

    # REQUEST TO AWS TO PUT IN BUCKETY
    resp = s3.Bucket(AWS_BUCKET).put_object(Key=f"{id}.{file_extension}", Body=file_to_upload)



    # FIXME: Review if changed from current to API.
    # flavor = request.json["flavor"]
    # size = request.json["size"]
    # rating = request.json["rating"]
    # image = request.json.get("image")
    # image = image if image else None

    # # alternate method
    # # image = request.get_json()["image"]


    new_listing = Listing(
        title=title,
        img_key=f'{id}.{file_extension}',
        description=description,
        price=price,
        zipcode=zipcode,
        )


    # FIXME: PUT IN DATABASE
    db.session.add(new_listing)
    db.session.commit()

    # # TODO:
    # serialized = new_cupcake.serialize()

    # # TODO:
    # return (jsonify(cupcake=serialized), 201)

    # TODO: Return the url for the file!
    # redirect('https://c-sharebnb-r26.s3.us-west-1.amazonaws.com/')
    return render_template('file_input.html',url=url)
    # return render_template('file_input.html')


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





