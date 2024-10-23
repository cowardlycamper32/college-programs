import sqlite3 as sl

from PyQt5.sip import array


def intcheck(x):
    try:
        x = int(x)
        return True
    except (TypeError, ValueError) as e:
        return False


def strcheck(x):
    try:
        x = str(x)
        return True
    except (TypeError, ValueError):
        return False


def check(x, y="int"):
    y = y.lower()
    if y == "int":
        try:
            x = int(x)
            return True
        except (TypeError, ValueError) as e:
            return False
    elif y == "str":
        try:
            x = str(x)
            return True
        except (ValueError, TypeError):
            return False


def filecheck(filename, checkfor: str = "txt"):
    filename = filename.lower()
    splitfilename = filename.split(".")
    if splitfilename[-1] == checkfor.lower():
        return True
    else:
        return False


def checkForX(item, checkFor=[" ", ]):
    for i in checkFor:
        for j in range(len(item)):
            if item[j] == i:
                return True
            else:
                return False


def slConnectionManager(database: str = 'default.sqlite'):
    connection = sl.connect(database)
    cursor = connection.cursor()
    return cursor


def query(query: str, cursor):
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def slConnectionCloser(cursor):
    cursor.close()
    return True


def slAddRow(cursor: sl.Cursor, table, data: tuple):
    cursor.execute('INSERT INTO ' + table + 'VALUES ' + str(data))
    return cursor
