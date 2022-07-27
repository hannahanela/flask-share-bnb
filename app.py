"""Flask app for Share BnB API."""

from pickle import GET
from webbrowser import get
from flask import Flask, url_for, render_template, redirect, flash, jsonify, request

import boto3
s3 = boto3.resource('s3')

from flask_debugtoolbar import DebugToolbarExtension

# TODO: Database
from models import db, connect_db
# from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

# TODO: update w/ db name
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

# RESTful Routes for Listings
# GET all
    # GET /listings
    # LISTINGS_MODEL.query.all()
    # [{listing}, ...] listing as {username, img, description, price}
# GET one
    # GET /listings/<listing_id?>
    # LISTINGS_MODEL.query.get_or_404(id?)
    # {username, img, descr, price}
# POST
    # POST /listings
    # make sure not a duplicate listing validation
    # AWS happens here****is this successful?
    # listings_model.create
    # resp 201 CREATED {username, img, descr, price}
# DELETE
    # DELETE /listings/<listing_id?>
    # query.get_or_404(listing_id?)
    # AWS remove happens here****
    # .delete(listing)
    # return success message
# PATCH
    # PATCH /listings/<listing_id?>
    # query.get_or_404(id?)
    # get form inputs --> does this inlude a new img?
        # if img, AWS remove old, add new
    # request.json.get("descr")
        # update db
    # return success msg & {username, img, descr, price}
# request sent from browser
# query db
# return data as JSON
# @app.get("/")
# @app.route('path',methods=["get"])


# TODO:A running file.
# Right now the file has many un instantiated variables and will crash

# TODO:Post route work

# TODO: After running file able to make an insomnia request to route.







# TODO: to /api??
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

    return '/api/listings'


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
# FIXME: listings? Or listing?
@app.route("/api/listings",methods=["POST"])
def listing_create():
    """
    Creates a listing instance with username, img, description, price and adds
    to db.
    # Takes username, img, description, price.
    Returns with JSON:
        {listing: {username,img, description, price}}
    """

    print ('###################################################',request)
    print ('request.files[file] = ',request.files["file"])

    file_to_upload = request.files["file"]

    # c-sharebnb-r26

    # Upload a new file
    # data = open('test.jpg', 'rb')
    resp = s3.Bucket('c-sharebnb-r26').put_object(Key='test.jpg', Body=file_to_upload)

    print ('resp = ',resp)

    # FOR REFERENCE
    ###################################################
    # <Request 'http://localhost:5001/results' [POST]>
    # request.files[file] =  <FileStorage: 'testCat.jpeg' ('image/jpeg')>
    # resp =  s3.Object(bucket_name='c-sharebnb-r26', key='test.jpg')

    # TODO: request.files

    # # TODO:
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

    return "(POST) /api/listings"

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





