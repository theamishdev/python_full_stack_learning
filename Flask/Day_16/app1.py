
from flask import Flask, render_template, redirect

app=Flask(__name__)


# integer
@app.route('/blog/<int:id>')

# string

@app.route('/<id>')

def home(id):
    # return f"The dynamic route data is : {id}"

    return render_template("dynamic.html", id=id)

# float
@app.route('/price/<float:paisa>')
def price(paisa):
    return render_template("paisa.html", paisa=paisa)

# path
@app.route('/pat/<path:file>')
def path(file):
    return render_template("path.html", file=file)



app.run(debug="True")
