from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',defaults={'x':4,'y':4,'color1':'black','color2':'red'})
@app.route('/<int:x>',defaults={'y':4,'color1':'black','color2':'red'})
@app.route('/<int:x>/<int:y>',defaults={'color1':'black','color2':'red'})
@app.route('/<int:x>/<int:y>/<string:color1>',defaults={'color2':'red'})
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def index(x,y,color1,color2):
    return render_template('index.html',x=x ,y=y ,color1=color1 ,color2=color2)


if __name__ == '__main__':
    app.run(debug=True)