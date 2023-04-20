from flask1 import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first_flask():
    return "This is my first flask program"

@app.route("/flask_2")
def second_flask():
    return "Python is fun"

@app.route("/index")
def first_webpage():

    name = "Flask"
    return render_template("index.html",index_variable=name)

app.run(debug=True)