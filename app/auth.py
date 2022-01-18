from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import json

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        pswd = request.form.get('pswd')

        user = User.query.filter_by(name=name).first()
        if user :
            if check_password_hash(user.pswd, pswd) :
                flash('Login successfull', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.user_homepage'))
            else:
                flash('Login failed', category='error')
        else:
            flash('Login failed', category='error')
    else :
        return render_template("auth/login.html")

@auth.route('/logout')
@login_required
def logout():
    return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        # getting form data
        name = request.form.get('name')
        pswd = request.form.get('pswd')
        # checking if user name already exist in db
        user = User.query.filter_by(name=name).first()
        if user :
            flash('Alias unavailable!', category='error')
            return render_template("auth/signup.html")
        else :
            # add new user in db
            db.session.add(User(name=name, pswd=generate_password_hash(pswd, method='sha256')))
            db.session.commit()
            # message for user
            flash('Account successfully created', category='success')
            # redirection to login page
            return redirect(url_for('auth.login'))
    else :
        return render_template("auth/signup.html")

@auth.route('/delete_note', methods=['POST'])
@login_required
def delete_note():
    # Recupere l'id de la note dans le body de la requete
    note = json.loads(request.data)
    note_id = note['noteId']
    # Recupere la note dans la db
    note = Note.query.get(note_id)
    # Verifie si la note appartient au current user
    if note :
        if note.user_id == current_user.id :
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
    