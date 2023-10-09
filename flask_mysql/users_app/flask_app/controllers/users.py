from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request



@app.route('/')
@app.route('/', methods=['POST'])
def index():
    # redering the list of existing users 
    users = User.get_users()
    return render_template('users.html', users = users)

@app.route('/add_user')
def add_user():
    return render_template('add_user.html')

@app.route('/user/create',methods=['POST'])
def create_user():
    # adding a new user to DB
    User.create(request.form)
    dict = request.form
    for key in dict:
        print (f'key : ',key)
    #print(request.form)
    return redirect('/')

@app.route('/user/<int:id>')
def show_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('update_user.html', user=user)

@app.route('/user/show/<int:id>')
def user_details(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('user.html', user = user)

@app.route('/user/delete/<int:id>')
def user_delete(id):
    data = {'id': id}
    user = User.delete(data)
    return redirect('/')

@app.route('/user/update_user/<int:id>', methods=['POST'])
def user_update(id):
    data = request.form
    User.update(data)
    return redirect("/")