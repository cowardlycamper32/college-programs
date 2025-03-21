import os
from datetime import datetime as dt
import datetime
import math
from nlib import exceptions as ne

def datetimegen():
    filenametime = dt.strftime("%d.%m.%Y-%H:%M:%S", time.localtime(floor(time.time())))
    return filenametime


def timestampgen():
    readabletime = dt.strftime("%H:%M:%S", datetime.time.localtime(math.floor(datetime.time.time())))
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
        raise ne.LogNotOpenError("Log is Not open. Contact the program maintainer.")# from None

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