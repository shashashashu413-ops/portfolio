from app import app
from models import *

with app.app_context():

    Experience.query.delete()

    db.session.commit()

    print("Experience Cleared")