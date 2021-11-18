from flask import Blueprint, render_template,request, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('/home.html')

@views.route('/note')
def note():
    return render_template('note.html')