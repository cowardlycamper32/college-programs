from flask import Flask, request, render_template
from markupsafe import escape
import sqlite3 as db
import requests

secretFile = open("secret.scrt")
secret = secretFile.read()
secretFile.close()

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
import flask_bootstrap

app = Flask(__name__)
app.secret_key = secret
@app.route('/')
def index():
    firstname = request.args.get('LName')
    return render_template('index.html', last_name=escape(firstname), fav_color=escape(request.args.get('colour')),)


@app.route("/hello")
def hello():
    req = request.args.get("q")
    if req is None or req == "" or req == " ":
        return f'Add a search term'
    return f"you searched for {escape(req)}"

@app.route("/user/<userid>")
def viewUser(userid):
    with db.connect("userCache.db") as uc:
        ucc = uc.cursor()
        try:
            result = ucc.execute("SELECT * FROM users WHERE id = ?", (userid,))
            export = result.fetchone()
            print(export)
            return f'Hello, {escape(export[0])}'
        except TypeError as e:
            print(e)
            return f'User with id "{userid}" was not found'
        finally:
            uc.close()
@app.route("/post/<int:id>")
def viewPost(id):
    return f"GET {id}"

@app.route("/register")
def register():
    form = RegisterForm()
    message = ""
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        rPassword = form.repeatPassword.data

        with db.connect("userCache.db") as database:
            cur = database.cursor()
            currentUsers = cur.execute("SELECT username FROM users")
            print(currentUsers)

    return render_template("index.html")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(10, 40)])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 200)])
    repeatPassword = PasswordField("Repeat Password", validators=[DataRequired(), Length(8, 200)])

    submit = SubmitField("Submit")

if __name__ == '__main__':
    app.run(debug=True)