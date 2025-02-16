## run.py
from app import app, db
from models import User, Contact

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

