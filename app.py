"""Flask app for Share BnB API."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

# TODO: update w/ db name
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
@app.get("/")
@app.route[]