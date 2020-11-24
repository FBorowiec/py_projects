from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from email_sender import EmailSender


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:@localhost/height_webapp_db"
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/database_webapp/templates/input", methods=["POST"])
def input():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]

        es = EmailSender(email, height)

        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            return render_template("input.html")
        return render_template(
            "index.html", text="Your email address is already stored!"
        )


if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run()
