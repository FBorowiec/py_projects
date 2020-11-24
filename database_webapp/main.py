from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/database_webapp/templates/input", methods=["POST"])
def input():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]
    return render_template("input.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
