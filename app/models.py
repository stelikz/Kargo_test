from app import db
from sqlalchemy.orm import relationship
import sqlalchemy


class Jobs(db.Model):
    __tablename__ = 'jobs'

    job_id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(), nullable=False)
    destination = db.Column(db.String(), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    shipment_date = db.Column(db.DateTime)
    distance = db.Column(db.Integer, nullable=False)

    # bidsJ = db.relationship('Bids', backref='job', primaryjoin='Jobs.job_id==Bids.job_id', lazy='joined')

    def __init__(self,job_id, origin, destination, budget, shipment_date, distance):
        self.job_id = job_id
        self.origin = origin
        self.destination = destination
        self.budget = budget
        self.shipment_date = shipment_date
        self.distance = distance

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'job_id': self.job_id, 
            'origin': self.origin,
            'Destination': self.destination,
            'budget': self.budget,
            'shipment_date': self.shipment_date,
            'distance': self.distance
        }

class Bids(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.job_id"), nullable=False)
    transporter_name = db.Column(db.String(), nullable=False)
    transporter_rating = db.Column(db.Float)
    price = db.Column(db.Integer, nullable=False)
    vehicle_name = db.Column(db.String(), nullable=False)

    jobsB = relationship('Jobs', backref='bids')

    def __init__(self, id, job_id, transporter_name, transporter_rating, price, vehicle_name):
        self.job_id = job_id
        self.transporter_name = transporter_name
        self.transporter_rating = transporter_rating
        self.price = price
        self.vehicle_name = vehicle_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'job_id': self.job_id,
            'transporter_name': self.transporter_name,
            'transporter_rating': self.transporter_rating,
            'price': self.price,
            'vehicle_name': self.vehicle_name
        }