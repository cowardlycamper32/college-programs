from flask import Flask, request, render_template, redirect, session, flash
from flask_wtf.file import FileAllowed
from markupsafe import escape
import sqlite3 as db
import requests
from flask_wtf import FlaskForm, CSRFProtect, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired, Length, EqualTo
import flask_bootstrap
from flask_argon2 import Argon2
from time import sleep as wait

app = Flask(__name__)
secretFile = open('secret.scrt', 'r')
app.secret_key = secretFile.read()
secretFile.close()
argon = Argon2()

argon.init_app(app)
@app.route("/")
def index():
    try:
        return render_template("index.html", pageName="Home", siteName="Shopping", loggedInUsername=session["loggedInUsername"])
    except:
        return render_template("index.html", pageName="Home", siteName="Shopping", loggedInUsername=None)

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
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    repeatPassword = PasswordField("Repeat Password", validators=[DataRequired()])

    submit = SubmitField("Submit")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    usernameError = ""
    repeatPasswordError = ""
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        repeatPassword = form.repeatPassword.data

        with db.connect("database.db") as database:
            cur = database.cursor()
            userCheck = cur.execute("SELECT username FROM users").fetchall()
            for user in userCheck:

                if username == user[0]:
                    doNotRun = True
                    usernameError = "That username is in use."
                else:
                    doNotRun = False

            if password != repeatPassword:
                doNotRun = True
                repeatPasswordError = "Passwords must match"
            else:
                doNotRun = False

            print(doNotRun)
            if not doNotRun:
                cur.execute("INSERT INTO users (username, email, passwordHash, Flags) VALUES (?, ?, ?, ?)", (username, email, argon.generate_password_hash(password), "user"))
                session["loggedInUsername"] = username
                return redirect("/login")
    print(form.errors)

    return render_template("register.html", form=form)

class LoginForm(FlaskForm):
    usernameOrEmail = StringField("Username or Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Submit")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    usernameoremail = form.usernameOrEmail.data
    password = form.password.data

    if form.validate_on_submit():
        if "@" in usernameoremail:
            lookFor = "email"
        else:
            lookFor = "username"

        with db.connect("database.db") as database:
            cur = database.cursor()
            doNotRun = True
            #print(usernameoremail)
            if lookFor == "email":
                curentUsers = cur.execute("SELECT email, passwordHash FROM users WHERE email = ?", (usernameoremail,)).fetchone()
            elif lookFor == "username":
                currentUsers = cur.execute("SELECT username, passwordHash FROM users WHERE username = ?", (usernameoremail,)).fetchone()
            else:
                raise TypeError("Invalid input")



            #print(currentUsers)
            if currentUsers[0] is not None:
                doNotRun = False
            else:
                doNotRun = True

            if not doNotRun:
                #print(currentUsers)
                if argon.check_password_hash(currentUsers[1], password):
                    temp = cur.execute("SELECT username FROM users WHERE email = ? OR username = ?",(usernameoremail, usernameoremail)).fetchone()[0]
                    session["loggedInUsername"] = temp
                    return redirect("/")


    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    session.pop("loggedInUsername")
    return redirect("/")

def parseFlags(flags):
    flagsList = flags.split(",")
    for i in range(len(flagsList)):
        flagsList[i].strip()
    return flagsList

class Admin():
    class DeleteUserForm(FlaskForm):
        username = StringField("Username", validators=[DataRequired()])
        confirmUsername = StringField("Confirm Username", validators=[DataRequired()])
        confirmationText = "I confirm the deletion of the user."
        confirmation = StringField("Confirmation", validators=[DataRequired(), EqualTo(confirmationText)])
        submit = SubmitField("Submit")

    class EditUserForm(FlaskForm):
        username = StringField("Username", validators=[DataRequired()])
        submit = SubmitField("Submit")
    class CreateUserForm(FlaskForm):
        username = StringField("Username", validators=[DataRequired()])
        password = StringField("Password", validators=[DataRequired()])
        email = StringField("Email Address", validators=[DataRequired()])
        flags = StringField("Flags", validators=[DataRequired()])

        submit = SubmitField("Submit")



@app.route("/admin")
def admin():
    try:
        with db.connect("database.db") as database:
            cur = database.cursor()
            flags = cur.execute("SELECT flags FROM users WHERE username = ?", (session["loggedInUsername"],)).fetchone()[0]
    except:
        return redirect("/login")

    flags = parseFlags(flags)
    if "administrator" in flags:
        deleteUser = Admin().DeleteUserForm()
        createUser = Admin().CreateUserForm()
        editUser = Admin().EditUserForm()
        return render_template("admin.html", deleteUsers=deleteUser, addUsers=createUser)
    else:

        return "<h1>403 UNAUTHORISED</h1><script>alert('You are not authorized to access this page');</script><a href='/'>Go Home</a>"

@app.route("/admin/deleteUser", methods=["GET", "POST"])#
def adminDeleteUser():
    try:
        user = session["loggedInUsername"]
    except KeyError:
        return redirect("/admin")
    with db.connect("database.db") as database:
        cur = database.cursor()
        result = cur.execute("SELECT flags FROM users WHERE username = ?", (user,)).fetchone()[0]
        if "administrator" in parseFlags(result):
            form = request.form
            userToDelete = form.get("username")
            cur.execute("DELETE FROM users WHERE username = ?", (userToDelete,)).fetchone()
            return redirect("/admin", code=302)

@app.route("/admin/addUser", methods=["POST"])
def adminEditUser():
    try:
        user = session["loggedInUsername"]
    except KeyError:
        return redirect("/admin")
    with db.connect("database.db") as database:
        cur = database.cursor()
        result = cur.execute("SELECT flags FROM users WHERE username = ?", (user,)).fetchone()[0]
        if "administrator" in parseFlags(result):
            form = request.form
            existingUser = cur.execute("SELECT username FROM users WHERE username = ?", (form.get("username"),)).fetchone()
            if existingUser is not None:
                print("Username Exists")
                return redirect("/admin", code=400)
            else:
                cur.execute("INSERT INTO users (email, username, passwordHash, Flags) VALUES (?, ?, ?, ?)", (form.get("email"), form.get("username"), argon.generate_password_hash(form.get("password")), form.get("flags")))



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)




class SearchForm(FlaskForm):
    pass
