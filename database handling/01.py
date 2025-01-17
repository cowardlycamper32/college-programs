import sqlite3 as sq
table = """ID int,
        username string,
        first_name string,
        last_name string,
        password string,
        email string"""



db = sq.connect('test.sqlite')
cursor = db.cursor()
try:
    db.execute("CREATE TABLE users (" + table + ")")
except sq.OperationalError:
    print("Table already exists")


cursor.execute("INSERT INTO users (ID, username, first_name, last_name, password, email) VALUES (1, 'johndoe', 'john', 'doe', 'test@test.no', '1234')")
db.commit()