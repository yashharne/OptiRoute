import functools

from flask import (
    Blueprint, flash, g, redirect, request, session, url_for , jsonify, Response
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=(['POST']))
def register():
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        db = get_db()
        error = None

        if not email:
            error = 'email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                res = db.table("btp_user").insert({'email':email , 'name':name , 'password':generate_password_hash(password) }).execute()
                return jsonify(res.data)
            except:
                error = f"User {email} is already registered."
                return Response(error, status=401)
        else:
            return Response(error, status=401)




@bp.route('/login', methods=(['POST']))
def login():
        data=request.get_json()
        print(data)
        email = data.get('email')
        password = data.get('password')
        db = get_db()
        error = None

        user = db.table('btp_user').select('*').eq('email' , email).execute().data[0]

        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return jsonify(user)
        
        return Response(error , status=401)



@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    db = get_db()
    if user_id is None:
        g.user = None
    else:
        g.user = db.table('btp_user').select('*').eq('id' , user_id).execute().data[0]


@bp.route('/logout')
def logout():
    if session.get('user_id') is not None:
        session.clear()
        return Response("Logged Out" , status=200)
    return Response("Login first to log out" , status=400)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return Response("Unauthorized", status=401)

        return view(**kwargs)

    return wrapped_view

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response