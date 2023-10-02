from flask import Flask , render_template, session, request, redirect


app = Flask(__name__)
app.secret_key = "oli;ku,jnyhbtgvfdsfghjk"

@app.route('/')
def index():
    return render_template('index.html')

@app.route ('/process',methods=['POST'])
def process():
    
    # if session.get('info') == None :
    #     session['info'] =[]
    # session['info'].append(request.form)
    # print(f"After: {session.get('info')}")
    # return render_template('result.html')

    if session.get('session_list') is None:
        print("Session is empty")
        session['session_list'] = []
    
    print(f"Before: {session.get('session_list')}")
    session['session_list'].append(dict(request.form))
    session.modified = True  # Mark the session as modified
    print(f"After: {session.get('session_list')}")
    return redirect('/result')



@app.route('/result')
def result():
    return render_template('result.html',session_list = session.get('session_list'))

if __name__ == '__main__':
    app.run(debug=True)