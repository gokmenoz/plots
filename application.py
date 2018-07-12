from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index_lulu():
    if request.method == "GET":
        return render_template('CS.html')
    else:
        if request.form["userinfoform"]=="Counter Strike":
            return render_template('CS.html')
        if request.form["userinfoform"]=="Player Unknown":
            return render_template('gmap1.html')

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(os.path.join('static', path))        

if __name__ == "__main__":
    app.debug=False
    app.run(host='0.0.0.0')
