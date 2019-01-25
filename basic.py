from flask import Flask, render_template
from flask_mail import Mail, Message
app =Flask(__name__)
mail=Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



#@app.route("/")
#def index():
  # return render_template("index.html")

@app.route("/")
def index():
   msg = Message('Hello', sender = 'sender email id', recipients = ['write receiver email'])
   msg.body = "HI THIS IS A SAMPLE MAIL"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)

