import imp
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/hello')
def hello():

    return "<h1>hello</h1>"

@views.route('/', methods=['GET', 'POST'])
def home():
    text = request.form.get('text')
    if request.method == 'POST':
        flash('Message POST!', category='info')
        return render_template("views/home.html" , post_text="post ok "+str(text) )
    elif request.method == 'GET':
        flash('Message GET!', category='info')
        return render_template("views/home.html" , get_text="get ok "+str(text) )
    else :
        return render_template("views/home.html", name="audrey")

@views.route('/user', methods=['POST','GET'])
@login_required
def user_homepage():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) >= 1 :
            # add new note in db to current user
            db.session.add(Note(note=note, user_id=current_user.id))
            db.session.commit()
            flash('Note added successfully!', category='success')
            
    return render_template("views/user.html", user=current_user)