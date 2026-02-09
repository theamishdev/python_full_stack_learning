from flask import Flask
app = Flask(__name__)
""" @app.route("/")
def hoho():
    name = "" """

@app.route("/")
def home():
    return "<h1>Hello Flask</h1>"

@app.route("/about")
def about():
    return "<h1>About page</h1>"

@app.route("/contact")
def contact():
    return "<h1>This is contact page</h1>"

@app.route("/signup")
def signup(): 
    return "Sign up Successful", 201


app.run(debug=True)
