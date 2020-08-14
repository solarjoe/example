from app import app

from flask import render_template,request, flash, redirect
from flask import url_for, jsonify
from app.forms import AssetForm

from app.models import Asset

from app.my_lambda_function import handler

from flask import request
from werkzeug.urls import url_parse
import requests

from app import db

import uuid

import logging
logger = logging.getLogger()

debug = False
if logger.level == logging.DEBUG:
    debug = True

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @login_required # needs to be inner decorator
def index():
 
    form = AssetForm()

    if debug:
        flash('flashing() works.')

    # get all assets from database, 
    assets = Asset.query.all()

    # always false on GET request
    if form.validate_on_submit():

        # TODO: data is sanitized? of what? https://wtforms.readthedocs.io/en/2.2.1/fields/
        new_thing = Asset(name=form.name.data,
                          owner=form.owner.data,
                          properties=form.properties.data,
                          services=form.services.data,
                          events=form.events.data)

        db.session.add(new_thing)
        db.session.commit()
        flash('New thing submitted, reloading...?')
        return redirect(url_for('index'))

    return render_template('index_holygrail.html', title='Home',
                                                  assets=assets,
                                                  form=form)


@app.route("/lambda", methods=['GET', "POST"])
def route_lambda():

    class FakeAWSContext(object):
        aws_request_id = str(uuid.uuid4())

    return jsonify(**handler(None, FakeAWSContext()))


@app.route('/rami', methods=['GET', 'POST'])
def route_rami():
 
    if debug:
        flash('flashing() works.')

    return render_template('rami_holygrail.html', title='AWS Lambda')


@app.route('/iot', methods=['GET', 'POST'])
def route_iot():
 
    if debug:
        flash('flashing() works.')

    return render_template('iot_holygrail.html', title='IoT')

@app.route('/contact', methods=['GET', 'POST'])
def route_contact():
 
    if debug:
        flash('flashing() works.')

    return render_template('contact_holygrail.html', title='IoT')    