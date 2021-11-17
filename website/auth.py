from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    return render_template('login.html')

@auth.route("/logout")
def logout():
    return "logout"

@auth.route("/sign-up",methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        emailConfirm = request.form.get('emailConfirm')
        password = request.form.get('password')        
        flash('İsim alanı 4 karakterden az olamaz.', category='error')      
    
        
    return render_template('sign-up.html')    
           
   
    #flash('basarili', category='success') 
    