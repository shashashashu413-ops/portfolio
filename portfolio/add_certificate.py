from app import app
from models import *

with app.app_context():

    Certificate.query.delete()

    db.session.add(
        Certificate(
            name="Hackathon Certificate",
            file="hackthon_certificate.jpg"
        )
    )

    db.session.add(
        Certificate(
            name="Java Certificate",
            file="java_certificate.jpg"
        )
    )

    db.session.add(
        Certificate(
            name="Udemy Certificate",
            file="udemy_certificate.jpg"
        )
    )

    db.session.commit()

    print("Certificates Added Successfully!")