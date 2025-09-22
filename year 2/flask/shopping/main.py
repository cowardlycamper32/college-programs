from flask import Flask, request, render_template, redirect
from flask_wtf.file import FileAllowed
from markupsafe import escape
import sqlite3 as db
import requests
from flask_wtf import FlaskForm, CSRFProtect, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, EqualTo
import flask_bootstrap
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

class Product:
    def __init__(self, name, price, description, id):
        self.name = name
        temp = price / 100
        self.price = "$" + str(temp)
        self.description = description
        self.id = "/product/" + str(id)

@app.route("/search")
def search():
    query = request.args.get("q")
    products = []
    with db.connect("database.db") as database:
        cur = database.cursor()
        results = cur.execute("SELECT * FROM products WHERE instr(Name, ?) > 0 OR instr(Description, ?) > 0", (escape(query),escape(query))).fetchall()
        for product in results:
            products.append(Product(product[1], product[3], product[2], product[0]))



    return render_template("search.html", products=products)

@app.route("/product/<id>")
def product(id):
    with db.connect("database.db") as database:
        cur = database.cursor()
        product = cur.execute("SELECT * FROM products WHERE id = ?", (id,)).fetchone()


    return render_template()


@app.route("/about")
def about():
    return f"UNDER CONSTRUCTION ASSHAT"

@app.route("/contact")
def contact():
    return "SERIOUSLY FUCK OFF ASSHOLE"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)


class SearchForm(FlaskForm):
    pass

class LoginForm(FlaskForm):
    pass

class RegisterForm(FlaskForm):
    pass


