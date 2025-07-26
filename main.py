import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from models import db, Applicant, Policy, PolicyDocument
from forms import ApplicantForm, PolicyForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    applicants = Applicant.query.all()
    return render_template("index.html", applicants=applicants)

@app.route("/add_applicant", methods=["GET", "POST"])
def add_applicant():
    form = ApplicantForm()
    if form.validate_on_submit():
        data = form.data.copy()
        data.pop('csrf_token', None)
        applicant = Applicant(**data)
        db.session.add(applicant)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("applicant_form.html", form=form)

@app.route("/edit_applicant/<int:applicant_id>", methods=["GET", "POST"])
def edit_applicant(applicant_id):
    applicant = Applicant.query.get_or_404(applicant_id)
    form = ApplicantForm(obj=applicant)
    if form.validate_on_submit():
        form.populate_obj(applicant)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("applicant_form.html", form=form)

@app.route("/add_policy/<int:applicant_id>", methods=["GET", "POST"])
def add_policy(applicant_id):
    form = PolicyForm()
    form.applicants_id.data = applicant_id
    if request.method == 'POST' and form.validate_on_submit():
        data = form.data.copy()
        data.pop('csrf_token', None)
        policy = Policy(**data)
        db.session.add(policy)
        db.session.commit()

        # File Upload Handling
        if 'document' in request.files:
            file = request.files['document']
            if file and file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                document = PolicyDocument(
                    policy_id=policy.id,
                    document_name=filename,
                    document_path=file_path
                )
                db.session.add(document)
                db.session.commit()

        return redirect(url_for("index"))

    return render_template("policy_form.html", form=form)

@app.route("/edit_policy/<int:policy_id>", methods=["GET", "POST"])
def edit_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    form = PolicyForm(obj=policy)

    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(policy)
        db.session.commit()

        # File upload on edit (optional)
        if 'document' in request.files:
            file = request.files['document']
            if file and file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                document = PolicyDocument(
                    policy_id=policy.id,
                    document_name=filename,
                    document_path=file_path
                )
                db.session.add(document)
                db.session.commit()

        return redirect(url_for("index"))

    return render_template("policy_form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
