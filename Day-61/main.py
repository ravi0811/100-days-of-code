from flask import Flask, render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms import validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5



app = Flask(__name__)

Bootstrap= Bootstrap5(app)

class MyForm(FlaskForm):
    email= StringField('Email',[
        validators.Length(min=6,message=('Little short for an email address')),
        validators.Email(message=('That\'s not a valid email address.')),
        validators.Length(max=30,message=("To long for an email"))
    ])
    password= PasswordField('Password',[
        validators.Length(min=6,message=("To short for a password")),
        validators.Length(max=30,message=("To long for a password"))
    ])
    submit= SubmitField(label="Log In")

app.secret_key="my super secret key"
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=['GET','POST'])
def login():
    form= MyForm()
    t_mail='admin@gmail.com'
    t_password="123456789"
    
    if form.validate_on_submit():
        
        if form.email.data== t_mail and form.password.data== t_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html",form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
