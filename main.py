'''This tells Flask to run the app with debugging enabled, so you can easily see errors in the terminal while developing.
'''
from app import create_app  # Import the create_app function from the app package

app = create_app()  # Create an instance of the Flask app

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for easier development
