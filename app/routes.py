from app import app

from flask import render_template,request, flash, redirect
from flask import url_for
from app.forms import AssetForm

from app.models import Asset

from flask import request
from werkzeug.urls import url_parse

from app import db

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @login_required # needs to be inner decorator
def index():
 
    # posts = [ {'site': str(_)}  for _ in range(2)]
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

