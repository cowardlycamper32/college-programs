from flask import Flask, request, render_template, redirect
from markupsafe import escape
import sqlite3 as db
import requests
from Exceptions import UsernameAlreadyExists

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
    with db.connect("userCache.db") as database:
        cur = database.cursor()
        posts = cur.execute("SELECT Title, id FROM posts").fetchall()
    return render_template('index.html', posts=posts)


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
            return redirect("/error?err=UserNotFound&prv=home")

@app.route("/posts")
def viewPosts():
    pass

@app.route("/posts/<id>")
def viewPost(id):
    with db.connect("userCache.db") as uc:
        ucc = uc.cursor()
        #try:
        result = ucc.execute("SELECT * FROM posts WHERE id = ?", (id,))
        export = result.fetchone()
        print(export)
        try:
            results = {
                "name": escape(export[0]),
                "content": escape(export[3]),
            }
            print(results)
            return render_template("post.html", post=results)
        except TypeError as e:
            return redirect("/error?err=PostNotFound&prv=home")

@app.route("/post/new", methods=["GET", "POST"])
def newPost():
    form = PostForm()
    if form.validate_on_submit():
        PostTitle = form.postTitle.data
        PostContent = form.postBody.data
        PostUsername = form.postUsername.data

        with db.connect("userCache.db") as database:
            cur = database.cursor()
            DoNotRun = True
            currentUsers = cur.execute("SELECT username, id FROM users").fetchall()
            for user in currentUsers:
                if user[0] == PostUsername:
                    DoNotRun = False
                    posterID = user[1]

            if not DoNotRun:
                cur.execute("INSERT INTO posts (Title, content, userID) VALUES (?, ?, ?)", (PostTitle, PostContent, posterID))
                postID = cur.execute("SELECT id FROM posts WHERE Title = ? AND content = ? AND userID = ?", (PostTitle, PostContent, posterID)).fetchone()[0]
                return redirect("/posts/{}".format(postID))
            else:
                return redirect("/error?err=UserNotFound&prv=post-new")

    return render_template("newPost.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    message = ""
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        rPassword = form.repeatPassword.data

        with db.connect("userCache.db") as database:
            cur = database.cursor()
            doNotRun = False
            currentUsers = cur.execute("SELECT username FROM users").fetchall()
            for user in currentUsers:
                if user[0] == username:
                    doNotRun = True
            if not doNotRun:
                cur.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, rPassword))
                print(username, password, rPassword)
                return redirect("/register/success")
            else:
                return redirect("/error?err=UserExists&prv=register")



    return render_template("register.html", form=form)

@app.route("/error")
def error():
    err = request.args.get("err")
    back = request.args.get("prv")
    error = ""
    match escape(err):
        case "UserExists":
            error = "Username already exists"
        case "UserNotFound":
            error = "That Username doesn't exist"
        case "PostNotFound":
            error = "That Post Doesn't Exist"
        case _:
            error = "An Unknown Error Occurred"
    if back == "home" or back is None:
        link = "/"
    elif "-" in back:
        splat = back.split("-")
        construct = ""
        for i in splat:
            construct += "/"
            construct += i

        link = construct
    else:
        link = "/" + escape(back)
    return render_template("error.html", error=error, link=link)


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(10, 40)])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 200)])
    repeatPassword = PasswordField("Repeat Password", validators=[DataRequired(), Length(8, 200)])

    submit = SubmitField("Submit")


class PostForm(FlaskForm):
    postTitle = StringField("Title", validators=[DataRequired()])
    postBody = StringField()
    postUsername = StringField("Username", validators=[DataRequired()])

    submit =SubmitField("Post")

    

if __name__ == '__main__':
    app.run(debug=True)