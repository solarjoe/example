import logging

# logger here, say we want to log to file and console

# formatter = logging.Formatter(fmt="%(asctime)s %(name)s.%(levelname)s: %(message)s", datefmt="%Y.%m.%d %H:%M:%S")

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# handler = logging.FileHandler(os.path.dirname(os.path.realpath("__file__")) + '/webserver.log')

# handler.setFormatter(formatter)
# handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)

# handler2 = logging.StreamHandler(stream=sys.stdout)
# handler2.setFormatter(formatter)
# handler2.setLevel(logging.DEBUG)
# logger.addHandler(handler2)

from flask import Flask, render_template,request

from app import app, db

if __name__ == '__main__':

    # run app in debug mode on port 5000
    # maybe this comment is not needed in clean code :)
    app.run(host='127.0.0.1', debug=True, port=5000) 




