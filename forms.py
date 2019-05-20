from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, ValidationError, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User

class SignupForm(FlaskForm):#SignUps froms data
    first = StringField('First', validators=[DataRequired()])
    last = StringField('Last', validators=[DataRequired()])
    username = StringField('UserName', validators=[DataRequired(), Length(min=6,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('ComfirmPassword', validators=[DataRequired(),EqualTo('password')])
    campus = StringField('campus', validators=[DataRequired()])
    description = TextAreaField('description')
    submit = SubmitField('Signup')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Please use another username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email address already exist in the system.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('remember')
    submit = SubmitField('login')
    
class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submitPost = SubmitField('Post')
    
class ButtonForm(FlaskForm):
    like = SubmitField('like')
    shocked = SubmitField('shocked')
    laugh = SubmitField('laugh')

class SelectForm(FlaskForm):
    start = DateField('start', validators=[DataRequired()])
    end = DateField('end', validators=[DataRequired()])
    search = SubmitField('search')

class SearchForm(FlaskForm):
    keywords = StringField('keywords', validators=[DataRequired()])
    search = SubmitField('search')

class CommentForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired()])
    submitComm = SubmitField('Post')

class UpdateFrom(FlaskForm):
    new_title = StringField('new_titile', validators=[DataRequired])
    new_content = TextAreaField('new_content', validators=[DataRequired])
    update = SubmitField('Update')