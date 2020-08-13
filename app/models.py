from app import db
from datetime import datetime

class Asset(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    owner = db.Column(db.String(100))
    
    properties = db.Column(db.String(1200))
    # alternative name operations?
    services = db.Column(db.String(1200))
    events = db.Column(db.String(1200))

    def __repr__(self):
        return '<Asset {}>'.format(self.body)
