from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase ="hello", times =5)

@app.route('/play',defaults={'count':3, 'color':'aqua'})
@app.route('/play/<int:count>',defaults={'color':'aqua'})
@app.route('/play/<int:count>/<string:color>')
def play(count, color):
    return render_template('play.html', count = count, color = color )









if __name__ == '__main__':
    app.run(debug=True)
