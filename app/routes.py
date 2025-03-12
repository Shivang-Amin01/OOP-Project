from flask import Blueprint, request, jsonify
from .models import db, Vehicle, Booking
from datetime import datetime

# Define the Blueprint for routes. Blueprints help organize the application into modules
api = Blueprint('api', __name__)

# Test route to check if the app is working
@api.route('/test', methods=['GET'])
def test():
    # Returns a JSON response to confirm the API is running
    return jsonify({"message": "Car Rental System API is running!"})

# Add a new vehicle to the inventory
@api.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    # Get the data from the request (expects JSON format)
    data = request.get_json()

    # Create a new Vehicle object using the data
    new_vehicle = Vehicle(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        price_per_day=data['price_per_day']
    )

    # Add the new vehicle to the database and commit the transaction
    db.session.add(new_vehicle)
    db.session.commit()

    # Return a success message in JSON format
    return jsonify({"message": "Vehicle added successfully!"}), 201

# Get all vehicles from the database
@api.route('/vehicles', methods=['GET'])
def get_vehicles():
    # Query all vehicles from the Vehicle model
    vehicles = Vehicle.query.all()
    
    # Create a list of dictionaries for each vehicle
    vehicles_list = [{"id": v.id, "make": v.make, "model": v.model, "year": v.year, "price_per_day": v.price_per_day} for v in vehicles]

    # Return the list of vehicles in JSON format
    return jsonify(vehicles_list)

# Create a booking for a vehicle
@api.route('/create_booking', methods=['POST'])
def create_booking():
    # Get the data from the request (expects JSON format)
    data = request.get_json()

    # Find the vehicle by its ID
    vehicle = Vehicle.query.get(data['vehicle_id'])
    
    # Check if the vehicle is available
    if not vehicle or not vehicle.availability:
        return jsonify({"message": "Vehicle not available!"}), 400

    # Calculate the total price based on the dates provided in the request
    start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
    total_price = (end_date - start_date).days * vehicle.price_per_day

    # Create a new booking entry in the database
    new_booking = Booking(
        vehicle_id=vehicle.id,
        user_name=data['user_name'],
        start_date=start_date,
        end_date=end_date,
        total_price=total_price
    )

    # Mark the vehicle as unavailable (since it's booked)
    vehicle.availability = False
    
    # Add the booking to the database and commit the transaction
    db.session.add(new_booking)
    db.session.commit()

    # Return a success message in JSON format
    return jsonify({"message": "Booking created successfully!"}), 201

# Home route, serves as the root of the API
@api.route('/')
def home():
    # Returns a simple welcome message
    return "Welcome to the Car Rental System!"
