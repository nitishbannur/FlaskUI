from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	login = SubmitField('Login')

class HomePageForm(FlaskForm):
	name = StringField('Victim Name', validators=[DataRequired()])
	crime_type = SelectField('Crime to Report', choices=[('theft','Theft'),('assault','Assault'),('gta','Grand Theft Auto'),('sha','Sexual Harrassment'),('other', 'Other')])
	description = StringField('Facial Features of Suspect', widget=TextArea())
	generate_img = SubmitField('Generate Images')
	incident_report = TextAreaField('Incident Report')
	submit_report = SubmitField('Submit Report')
	select_img=BooleanField()