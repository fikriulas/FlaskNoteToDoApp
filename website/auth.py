from flask import Blueprint, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.widgets import PasswordInput
from wtforms.validators import DataRequired, Length, ValidationError, Email, email_validator, EqualTo 
#email_validator için "pip install email_validator"

auth = Blueprint('auth', __name__)

class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired('This Field Is Required'),Length(min=3,max=30)])
    email = StringField('email', validators=[DataRequired('This Field Is Required'),Email('This field requires a valid email address'),Length(min=3,max=40)])
    emailConfirm = StringField('emailConfirm', validators=[DataRequired('This Field Is Required'),EqualTo('email',message="E-Mail Field does not match.")])
    password = StringField('password', validators=[DataRequired('This Field Is Required'),Length(min=7,max=15)],widget=PasswordInput(hide_value=False))
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired('This Field Is Required'),Email('This field requires a valid email address'),Length(min=3,max=40)])
    password = StringField('password', validators=[DataRequired('This Field Is Required'),Length(min=7,max=15)],widget=PasswordInput(hide_value=False))
    
@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')
            flash('Giriş İşlemi Başarılı',category='success')
        else:
            flash('Kontrol Edip Tekrar Deneyin',category='error')
            return render_template('login.html',form = form)      
        
        
        
    return render_template('login.html',form = form)

@auth.route("/logout")
def logout():
    return "logout"

@auth.route("/sign-up",methods=['GET','POST'])
def sign_up():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get('name')
            email = request.form.get('email')
            emailConfirm = request.form.get('emailConfirm')
            password = request.form.get('password')        
            flash('Kayıt İşlemi Başarılı', category='success')      
        else:
            flash('Kontrol Edip Tekrar Deneyin', category='error')
            return render_template('sign-up.html',form = form)    
    return render_template('sign-up.html',form = form)           
   
    #flash('basarili', category='success') 
    