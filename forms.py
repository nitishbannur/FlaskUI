from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, TextAreaField
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
	description = TextAreaField('Facial Features of Suspect')
	generate_img = SubmitField('Generate Images')
	incident_report = TextAreaField('Incident Report')
	submit_report = SubmitField('Submit Report')
	
	select_img1 = BooleanField()
	select_img2 = BooleanField()
	select_img3 = BooleanField()
	select_img4 = BooleanField()
	select_img5 = BooleanField()
	select_img6 = BooleanField()
	select_img7 = BooleanField()
	select_img8 = BooleanField()
