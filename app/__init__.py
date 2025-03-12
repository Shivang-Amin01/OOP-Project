from flask import Flask
from flask_cors import CORS
from .models import db

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow cross-origin requests

    # Configure the app for the database (SQLite for now)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_rental.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)  # Initialize the app with the db

    # Import and register routes (inside the function)
    from .routes import api
    app.register_blueprint(api)

    return app

'''Here, we initialize the Flask app, configure the database, and allow cross-origin requests (useful when connecting a frontend).
We also set up SQLAlchemy (which is the library we will use to interact with the database).'''