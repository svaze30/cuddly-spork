from wtforms import *
from wtforms.validators import *
from flask_wtf import *

class SignUpForm(FlaskForm):
    Username=StringField('Username',validators=[DataRequired(),length(min=5,max=20)])
    Password=PasswordField('Password',validators=[DataRequired(),length(min=5,max=20)])
    ConfirmPassword=PasswordField('Confirm Password',validators=[DataRequired(),length(min=5,max=20),EqualTo('Password')])
    profilePic=FileField('Profile Picture',validators=[DataRequired()])
    submit=SubmitField('Sign Up')
    
    
    
class LogInForm(FlaskForm):
    Username=StringField('Username',validators=[DataRequired(),length(min=5,max=20)])
    Password=PasswordField('Password',validators=[DataRequired(),length(min=5,max=20)])
    submit=SubmitField('Log In')