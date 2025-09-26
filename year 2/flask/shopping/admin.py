from main import app
from flask import request
import sqlite3
@app.route("/admin/deleteUser")
def deleteUser():
    user = request.args.get('user')
