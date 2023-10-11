from flask_app import app
from flask_app.models.user import User
from flask import render_template , request, redirect, session

@app.route('/')
def log_reg():
    return render_template('login.html')

@app.route('/register')
def register_user():
    return render_template('register.html')

@app.route('/register_user', methods = ['POST'])
def register():
    data = request.form
    print(data)
    if User.validate_register(data):
        User.create(data)

    return redirect('/')

@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        print (f'getting the user by email for the login : ')
        user = User.get_by_email(data)
        print("CORRECT!!!" , data)
        session["user_id"] = user.id
        return render_template("dashboard.html",user = user)
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')