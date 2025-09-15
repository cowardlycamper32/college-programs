import sqlite3 as db

def GET(cur, table, ):
    cur.execute(f"SELECT * FROM {table}")