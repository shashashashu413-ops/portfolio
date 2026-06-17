from app import app
from models import *

with app.app_context():

    db.session.add(
        Experience(
            company="Hitachi",
            role="Quality Checker",
            duration="6 Months"
        )
    )

    db.session.commit()

    print("Experience Added")