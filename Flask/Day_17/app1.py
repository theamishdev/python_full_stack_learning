
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>Home Page</h2>"


@app.route("/crash")
def crash():
    # This will trigger 500 error
    return 1 / 0


# 404 Error Handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# 500 Error Handler
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=False)  # IMPORTANT: Set False to test 500 page
