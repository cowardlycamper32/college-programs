from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import sqlite3 as db

app = Flask(__name__)

@app.route("/")
def index():
    session["username"] = "admin"
    return render_template("index.html", siteName="Flask 02", pageName="index", loggedInUsername=session["username"])

@app.route("/about")
def about():
    return f"urgay"

@app.route("/contact")
def contact():
    return f"urreallygay"


@app.route("/error")
def error():
    err = request.args.get("err")
    back = request.args.get("back")
    match err:
        case _:
            error = "An unknown error occurred"

    return render_template("error.html", error=error, back=back)


if __name__ == "__main__":
    app.run(debug=True)