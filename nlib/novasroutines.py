import sqlite3 as sl
import datetime
import sys
import time
from math import floor
from time import strftime
import os
from platform import system
import unittest
from nlib import exceptions as ne


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

def infiniteCheck(question: str, typeLookingFor: str, log,  error: str = "Invalid input"):
    continuepls = True
    userInput = input(question)
    while continuepls:
        if userInput == "":
            continuepls = True
            writeLog(log, "Invalid input: No Input Detected")
            userInput = input("Invalid Input: No Input Detected\n")
        else:
            if typeLookingFor == "int":
                if not(intcheck(userInput)):
                    userInput = input(error + ":\nPlease enter a number")
                    writeLog(log, error + ": Enter a Number")
                else:
                    continuepls = False

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

def datetimegen():
    filenametime = strftime("%d.%m.%Y-%H:%M:%S", time.localtime(floor(time.time())))
    return filenametime


def timestampgen():
    readabletime = strftime("%H:%M:%S", time.localtime(floor(time.time())))
    return "[" + readabletime + "]"

def fileCorrect(path):
    temparr = path.split("\\")
    for i in temparr:
        if ".py" in i:
            filename = i
    return filename


def logInit(calledFrom = "nowhere"):
    currenttime = datetimegen()
    if not(os.path.exists("../logs")):
        os.mkdir("../logs")

    log = open("../logs/" + currenttime + '.log', 'a')
    log.write(timestampgen() + " Program \'" + fileCorrect(calledFrom) + "\' started\n")
    return log

def writeLog(log, passedinput):
    try:
        log.write(timestampgen() +" " + str(passedinput) + "\n")
    except AttributeError:
        raise ne.LogNotOpenError("Log is Not open. Contact the program maintainer.") from None

def closelog(log):
    log.close()

def createpath(path: str):
    if not(os.path.exists(path)):
        os.mkdir(path)
    return True


def createfile(path: str):
    file = open(path, "a")
    return file


def fileexistscheck(path: str):
    if os.path.exists(path):
        return True
    else:
        return False

def simpwrite(file, text):
    file.write(text + "\n")

def print2Dnicely(array):
    for row in array:
        print(row)

def clearer():
    oS = system()
    if oS == "Windows":
        os.system("cls")
    else:
        os.system("clear")



def unitTest():
    assert sum([1,2,3]) == 5, "should be 5"

