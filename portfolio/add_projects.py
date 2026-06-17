from app import app
from models import *

with app.app_context():

    db.session.add(
        Project(
            title="AI Image Classification",
            description="CNN based image classification system using Python, OpenCV and TensorFlow.",
            image="/static/images/projects/AI image classifier.jpg",
            github_link="https://github.com/shashashashu413-ops"
        )
    )

    db.session.add(
        Project(
            title="Spoken English Learning App",
            description="Application designed to improve English communication skills through practice exercises and learning modules.",
            image="/static/images/projects/spoken english.jpg",
            github_link="https://github.com/shashashashu413-ops"
        )
    )

    db.session.add(
        Project(
            title="Student Management System",
            description="Web-based student management system developed using Flask and SQLite.",
            image="/static/images/projects/student management system.jpg",
            github_link="https://github.com/shashashashu413-ops"
        )
    )

    db.session.commit()

    print("Projects Added Successfully!")