from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask import render_template, redirect, request


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    # redering the list of existing users 
    dojos = Dojo.get_dojos()
    return render_template('dojos.html', dojos = dojos)

@app.route('/dojo/create',methods=['POST'])
def create_dojo():
    # adding a new user to DB
    Dojo.create(request.form)
    dict = request.form
    for key in dict:
        print (f'key : ',key)
    #print(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def dojo_details(id):
    data = {'id': id}
    dojo = Dojo.get_one(data)
    ninjas = Ninja.get_dojo_by_id(data)
    print (ninjas)
    return render_template('dojo_detail.html', ninjas = ninjas, dojo = dojo)
