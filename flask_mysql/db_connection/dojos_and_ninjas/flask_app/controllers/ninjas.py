from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

from flask import render_template, redirect, request


@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_dojos()
    return render_template('ninja.html', dojos = dojos)

@app.route('/ninja/create',methods=['POST'])
def create_ninja():
    # adding a new user to DB
    Ninja.create(request.form)
    dict = request.form
    for key in dict:
        print (f'key : ',key)
    #print(request.form)
    return redirect('/')

