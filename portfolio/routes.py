from flask import render_template

from app import app

from models import *

@app.route("/")
def home():

    projects = Project.query.all()
    skills = Skill.query.all()
    certificates = Certificate.query.all()
    education = Education.query.all()
    experience = Experience.query.all()

    print("Certificates:", certificates)

    return render_template(
        "index.html",
        projects=projects,
        skills=skills,
        certificates=certificates,
        education=education,
        experience=experience
    )