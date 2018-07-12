from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index_lulu():
    if request.method == "GET":
        return render_template('userinfo_lulu.html')
    else:
        if request.form["price"]=="CS":
            return render_template('index.html')
        if request.form["price"]=="PUBG":
            return render_template('index1.html')

if __name__ == "__main__":
    app.debug=False
    app.run(host='0.0.0.0')
