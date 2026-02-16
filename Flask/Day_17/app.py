
# from flask import Flask, render_template, request

# app=Flask(__name__)

# @app.route("/", methods=["GET", "POST"])

# def home():
#     name="" 
#     email=""
#     password=""

#     if request.method=="POST":
#         name=request.form.get("name")
#         email=request.form.get("email")
#         password=request.form.get("password")

#         return render_template("index.html", name=name, email=email, password=password)
    
#     if __name__ == "__main__":
#         app.run(debug=True)




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    email = ""
    password = ""

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

    return render_template("index.html", name=name, email=email, password=password)


if __name__ == "__main__":
    app.run(debug=True)

    


