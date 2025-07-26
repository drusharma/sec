from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dot = db.Column(db.String(50))
    address = db.Column(db.String(200))
    policies = db.relationship('Policy', backref='applicant', cascade='all, delete-orphan')

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicants_id = db.Column(db.Integer, db.ForeignKey('applicant.id'))
    bussiness_lines = db.Column(db.String(100))
    policy_no = db.Column(db.String(100))
    effective_date = db.Column(db.String(20))
    expiration_date = db.Column(db.String(20))