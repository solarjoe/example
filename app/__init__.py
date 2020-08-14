import logging
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

import sys

# logger here, say we want to log to the console and file
# TODO: link the logger level and the app config
formatter = logging.Formatter(fmt="%(asctime)s %(name)s.%(levelname)s: %(message)s", datefmt="%Y.%m.%d %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# handler = logging.FileHandler(os.path.dirname(os.path.realpath("__file__")) + '/webserver.log')

# handler.setFormatter(formatter)
# handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)

handler2 = logging.StreamHandler(stream=sys.stdout)
handler2.setFormatter(formatter)
handler2.setLevel(logging.DEBUG)
logger.addHandler(handler2)

# TODO:
# - fix form, same size for boxes
# - resizing description field resizes map

# initialize extensions right after the application instance
app = Flask(__name__)

# config can happen here in dict style
# app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config.from_object(Config)

# run 'flask db init'
# set 'export FLASK_APP=app.py'
db = SQLAlchemy(app)

# helper for database migration and change management
# migrate = Migrate(app, db)

# simple initialization
# from yourapplication import db
# db.create_all()

# login not used in this demo
# from flask_login import LoginManager
# login = LoginManager(app)
# login.login_view = 'login' # endpoint

# the toolbar is only enabled in debug mode:
# app.debug = True

# toolbar = DebugToolbarExtension(app)


# all the view functions (with route() decorator) have to be imported 
# in the __init__.py file after the application object is created.
from app import routes, models

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True, port=8080) #run app in debug mode on port 5000
