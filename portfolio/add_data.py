from app import app
from models import *

with app.app_context():

    db.session.add(
        Skill(
            name="Python",
            percentage=90
        )
    )

    db.session.add(
        Skill(
            name="Flask",
            percentage=85
        )
    )

    db.session.add(
        Skill(
            name="HTML/CSS",
            percentage=80
        )
    )

    db.session.commit()

    print("Skills added successfully!")