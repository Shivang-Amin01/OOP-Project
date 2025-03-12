from app import db, create_app
from app.models import Vehicle

app = create_app()
with app.app_context():
    db.create_all()
    print("Database created successfully!")
