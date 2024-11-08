import sqlite3 as sl

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

def infiniteCheck(question: str, typeLookingFor: str,  error: str = "Invalid input"):
    continuepls = True
    userInput = input(question)
    while continuepls:
        if userInput == "":
            continuepls = False
        if typeLookingFor == "int":
            try:
                userInput = int(userInput)
                continuepls = False
                return True
            except (TypeError, ValueError):
                userInput = input(error + "\n")
                continuepls = True

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
    cursor.execute('INSERT INTO ' + table + ' VALUES ' + str(data))
    return cursor

def insertSort(array = []):
    complete = False
    pointer1 = 0
    pointer2 = 1
    check = 0
    while not(complete):
        check = 0
        for num in range(len(array)):
            try:
                if array[pointer1] < array[pointer2]:
                    array[pointer1], array[pointer2] = array[pointer2], array[pointer1]
                else:
                    check += 1
            except IndexError:
                break
            if pointer1 != pointer2 - 1:
                pointer1 += 1
            else:
                pointer2 += 1
        if check == len(array):
            complete = True
    return array


def splitter(x, split: str):
    out = x.split(split)
    return out