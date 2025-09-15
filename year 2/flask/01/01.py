from flask import Flask, request, render_template
from markupsafe import escape
import sqlite3 as db
import requests


app = Flask(__name__)

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

@app.route("/post/<int:id>")
def viewPost(id):
    return f"GET {id}"

#@app.route("/register")

if __name__ == '__main__':
    app.run(debug=True)