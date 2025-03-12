# This will define your database models 
# We’ve created the db object, which will be used to interact with the database in our app.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)


    def __repr__(self):
        return f'<Vehicle {self.make} {self.model}>'

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    vehicle = db.relationship('Vehicle', backref='bookings', lazy=True)

    def __repr__(self):
        return f'<Booking {self.id} for {self.user_name}>'

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)

    booking = db.relationship('Booking', backref='payments', lazy=True)

    def __repr__(self):
        return f'<Payment {self.id} for Booking {self.booking_id}>'


'''Explanation of Models:
Vehicle Model: Represents a car with attributes like make, model, year, price per day, and availability.
Booking Model: Represents a booking for a vehicle. It stores the user name, rental start and end dates, total price, and the vehicle being rented.
Payment Model: Stores payment information for each booking, including the amount and the date of the payment.'''

