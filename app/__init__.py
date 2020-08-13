
# TODO:
# - fix location form, same size for boxes
# - resizing description field resizes map
# - make map remember the last zoom and position and supply on reload
# https://www.isa.org/intech-home/2019/march-april/features/rami-4-0-reference-architectural-model-for-industr

# 

from flask import Flask

# from flask_debugtoolbar import DebugToolbarExtension

from flask_sqlalchemy import SQLAlchemy

# initialize extensions right after the application instance
app = Flask(__name__)

# config can happen here in dict style
# app.config['SECRET_KEY'] = 'you-will-never-guess'

from config import Config
app.config.from_object(Config)

# run 'flask db init'
# set 'export FLASK_APP=app.py'
db = SQLAlchemy(app)

# helper for database migration and change management
# migrate = Migrate(app, db)

# simple initialization
# from yourapplication import db
# db.create_all()


# no login needed
# from flask_login import LoginManager
# login = LoginManager(app)
# login.login_view = 'login' # endpoint

# the toolbar is only enabled in debug mode:
# app.debug = True

# toolbar = DebugToolbarExtension(app)

from app import routes, models

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True, port=8080) #run app in debug mode on port 5000




