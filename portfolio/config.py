from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    description = db.Column(db.Text)

    github_link = db.Column(db.String(300))

    image = db.Column(db.String(300))


class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200))

    file = db.Column(db.String(300))


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    percentage = db.Column(db.Integer)


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    degree = db.Column(db.String(200))

    college = db.Column(db.String(200))

    year = db.Column(db.String(50))


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    company = db.Column(db.String(200))

    role = db.Column(db.String(200))

    duration = db.Column(db.String(100))


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    message = db.Column(db.Text)

class Config:
    SECRET_KEY = "portfolio-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "static/uploads"
