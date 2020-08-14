from app import app

from flask import render_template,request, flash, redirect
from flask import url_for
from app.forms import AssetForm

from app.models import Asset

from flask import request
from werkzeug.urls import url_parse
import requests

from app import db

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @login_required # needs to be inner decorator
def index():
 
    form = AssetForm()

    flash('flashing() works.')

    # get all assets from database, 
    assets = Asset.query.all()

    for p in assets:
        print(p.id, p.name, p.owner, p.properties, p.services, p.events)

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


@app.route('/websocket', methods=['GET', 'POST'])
# @login_required # needs to be inner decorator
def route_websocket():
 
    flash('flashing() works.')

    return render_template('websocket_holygrail.html', title='Websocket')


@app.route('/api-gateway', methods=['GET', 'POST'])
def route_api():
 
    flash('flashing() works.')

    return render_template('api_holygrail.html', title='API Gateway')


@app.route('/aws-lambda', methods=['GET', 'POST'])
def route_lambda():
 
    flash('flashing() works.')

    return render_template('lambda_holygrail.html', title='AWS Lambda')


@app.route('/rami', methods=['GET', 'POST'])
def route_rami():
 
    flash('flashing() works.')

    return render_template('rami_holygrail.html', title='AWS Lambda')


@app.route('/iot', methods=['GET', 'POST'])
def route_iot():
 
    flash('flashing() works.')

    return render_template('iot_holygrail.html', title='IoT')