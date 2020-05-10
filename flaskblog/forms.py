from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_wtf.file import FileField,FileAllowed
from flaskblog.models import User
from flask_login import current_user

#inherit from FlaskForm
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),
                            Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[
                                        DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Oops! That doesnt seem to be unique')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('You Already have an Account, Please Login!')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),
                        Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),
                            Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError("Oops! That doesn't seem to be unique")
        
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Email is already taken by someone else!')
        
class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        if email.data:
            user = User.query.filter_by(email = email.data).first()
            print(user)
            if user is None:
                raise ValidationError('This email is not Registered!')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[
                                        DataRequired(),EqualTo('password')])
    submit = SubmitField('Change Password') 