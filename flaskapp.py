from flask import Flask, render_template, url_for, flash, redirect
from flask_mail import Mail, Message

'''Import all the forms classes from forms.py'''
from forms import RegistrationForm, LoginForm, HomePageForm

app = Flask(__name__)
mail=Mail(app)

'''Set up config for mail'''

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sppugan2019@gmail.com'
app.config['MAIL_PASSWORD'] = 'nitish123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#Secret Key required for hidden_tag() and some security reasons
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

home_legend = 'Please provide the details below'

about_text = ''

with open("./static/about.txt") as about:
	about_text = about.read()

'''Create Route for the Home Page'''
@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
	
	form = HomePageForm()

	gan_input_text = form.description.data

	victim_name = form.name.data
	crime = 'Crime to Report : '+form.crime_type.data
	report_text = 'Incident Report :'+str(form.incident_report.data)

	if form.validate_on_submit():
		flash('Incident Report Submitted Successfully', 'success')
		msg = Message('Incident Report -'+victim_name, sender = 'sppugan2019@gmail.com', recipients = ['anuraglkatakkar@gmail.com'])
		msg.body = victim_name + '\n' + crime + '\n' + report_text
		mail.send(msg)

		return redirect(url_for('home'))
	
	return render_template('home.html', title = 'Home Page', legend=home_legend, form=form)

'''Create Route for the About Page'''
@app.route("/about")
def about():
	return render_template('about.html', title = 'About Page', text=about_text)

'''Create Route for the Register Page'''
@app.route("/register")
def register():
	form  = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

'''Create Route for the Login Page'''
@app.route("/login", methods=['GET','POST'])
def login():
	form  = LoginForm()
	return render_template('login.html', title='Login', form=form)

'''To be able to run this from the terminal'''
if __name__  == '__main__' :
	app.run(debug = True)