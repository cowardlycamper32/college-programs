from flask import Flask, request, render_template, redirect
from flask_wtf.file import FileAllowed
from markupsafe import escape
import sqlite3 as db
import requests
from flask_wtf import FlaskForm, CSRFProtect, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired, Length, EqualTo
import flask_bootstrap
import flask_argon2 as ar2
app = Flask(__name__)
secretFile = open('secret.scrt', 'r')
app.secret_key = secretFile.read()
secretFile.close()

@app.route("/")
def index():
    return render_template("index.html")

class Product:
    def __init__(self, name, price, description, id, image):
        self.name = name
        temp = price / 100
        self.price = "$" + str(temp)
        self.description = description
        self.id = "/product/" + str(id)
        if image == "none" or image is None:
            self.imageLocation = "images/placeholder.png"
        else:
            self.imageLocation = "images" + image

@app.route("/search")
def search():
    query = request.args.get("q")
    products = []
    with db.connect("database.db") as database:
        cur = database.cursor()
        if query is None:
            results = cur.execute("SELECT * FROM Products").fetchall()
        else:
            results = cur.execute("SELECT * FROM Products WHERE instr(UPPER(Title), UPPER(?)) > 0 OR instr(UPPER(Description), UPPER(?)) > 0", (escape(query),escape(query))).fetchall()
        print(products)
        for product in results:
            imageID = product[4]
            imageURL = cur.execute("SELECT * FROM Images WHERE ImageID = ?", (imageID,)).fetchone()[1]
            products.append(Product(product[1], product[3], product[2], product[0], imageURL))



    return render_template("search.html", products=products)

@app.route("/product/<id>")
def product(id):
    with db.connect("database.db") as database:
        cur = database.cursor()
        product = cur.execute("SELECT * FROM Products WHERE ID = ?", (id,)).fetchone()
        productImage = cur.execute("SELECT location FROM Images WHERE ImageID = ?", (str(product[4]))).fetchone()
    try:
        prod = Product(product[1], product[3], product[2], product[0], productImage[0])
        print(product)
        return render_template("product.html", product=prod)
    except TypeError:
        return redirect("/error?err=ProductNotExist")

@app.route("/error")
def error():
    error = request.args.get("err")
    match error:
        case "ProductNotExist":
            err = "Product not found."
        case _:
            err = "An unknown error occured"

    return render_template("error.html", error=err)

@app.route("/about")
def about():
    return f"UNDER CONSTRUCTION ASSHAT"

@app.route("/contact")
def contact():
    return "SERIOUSLY FUCK OFF ASSHOLE"

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email Address")
    password = PasswordField("Password", validators=[DataRequired()])
    repeatPassword = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("submit")

@app.route("/register")
def register():
    form = RegisterForm()
    usernameError = "none"
    repeatPasswordError = "none"
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        repeatPassword = form.repeatPassword.data

        with db.connect("database.db") as database:
            cur = database.cursor()
            userCheck = cur.execute("SELECT username FROM users WHERE username = ?", (username)).fetchone()

            if username == userCheck[0]:
                doNotRun = True
                usernameError = "That username is in use."
            else:
                doNotRun = False

            if password != repeatPassword:
                doNotRun = True
                repeatPasswordError = "Passwords must match"
            else:
                doNotRun = False
            if not doNotRun:
                pass

    return render_template("register.html", form=form, usernameError=usernameError, repeatPasswordError=repeatPasswordError)





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)


class SearchForm(FlaskForm):
    pass

class LoginForm(FlaskForm):
    pass



    submit = SubmitField("submit")

