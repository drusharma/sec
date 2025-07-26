from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class ApplicantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    dot = StringField('DOT', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])

class PolicyForm(FlaskForm):
    applicants_id = HiddenField(validators=[DataRequired()])
    bussiness_lines = StringField('Business Lines', validators=[DataRequired()])
    policy_no = StringField('Policy Number', validators=[DataRequired()])
    effective_date = StringField('Effective Date', validators=[DataRequired()])
    expiration_date = StringField('Expiration Date', validators=[DataRequired()])