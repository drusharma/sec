from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dot = db.Column(db.String(20))
    address = db.Column(db.String(200))
    policies = db.relationship('Policy', backref='applicant', cascade="all, delete-orphan")

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'))
    business_lines = db.Column(db.String(100))
    policy_no = db.Column(db.String(100))
    effective_date = db.Column(db.Date)
    expiration_date = db.Column(db.Date)
    documents = db.relationship('PolicyDocument', backref='policy', cascade="all, delete-orphan")

class PolicyDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'))
    document_name = db.Column(db.String(200))
    document_path = db.Column(db.String(300))
