from flask import*

app = Flask(__name__)

@app.route("/user/<uname>")
def message(uname):
    return render_template('message2.html',name=uname)
if __name__=='__main__':
    app.run(debug=True)