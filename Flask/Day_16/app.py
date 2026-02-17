
# from flask import Flask, render_template, request, url_for

# app= Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():

#     data_incoming=""
#     if request.method=="POST":
#         # data_incoming=request.args.get
#         data_incoming=request.form.get("input_name")
#         data_incoming=request.form.get("input_email")
#         data_incoming=request.form.get("input_password")
#         print(data_incoming)
#     return render_template("index.html", data_incoming=data_incoming)

# app.run(debug=True, port=8000)


# if app=="__main__":
#     app.run(debug=True)





# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():

#     name = ""
#     email = ""
#     password = ""
#     data_incoming=""

#     if request.method == "POST":
#         name = request.form.get("input_name")
#         email = request.form.get("input_email")
#         password = request.form.get("input_password")
#         data_incoming=request.form.get("data_incoming")

#         print(name, email, password)

#     return render_template(
#         "index.html",
#         name=name,
#         email=email,
#         password=password
#     )


# if __name__ == "__main__":
#     app.run(debug=True, port=8000)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    name = ""
    email = ""
    password = ""
    error = None

    if request.method == "POST":
        name = request.form.get("input_name")
        email = request.form.get("input_email")
        password = request.form.get("input_password")

        print("Name:", name)
        print("Email:", email)
        print("Password:", password)

        # Hardcoded Admin Check
        if name == "admin" and password == "password":
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid Username or Password"

    return render_template(
        "index.html",
        name=name,
        email=email,
        password=password,
        error=error
    )
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
