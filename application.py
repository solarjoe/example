from app import app, db

if __name__ == '__main__':

    # run app in debug mode on port 5000
    # maybe this comment is not needed in clean code :)
    app.run(host='127.0.0.1', debug=True, port=5000) 
