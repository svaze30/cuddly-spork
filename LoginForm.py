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
    
class CommentForm(FlaskForm):
    Text=TextAreaField('Add a Comment',validators=[DataRequired(),length(min=1,max=256)])
    submit=SubmitField('Post Comment')
    
class PostForm(FlaskForm):
    Text=TextAreaField('Post Body',validators=[DataRequired(),length(min=1,max=256)])
    submit=SubmitField('Post')
    
class interestForm(FlaskForm):
    inter1=StringField('',validators=[length(max=20)])
    inter2=StringField('',validators=[length(max=20)])
    inter3=StringField('',validators=[length(max=20)])
    bio=StringField('Bio',validators=[length(min=5,max=256)])
    submit=SubmitField('Update')