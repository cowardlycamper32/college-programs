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


def check(x, y = "int"):
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
    else: return False

def checkForX(item, checkFor = [" ",]):
    for i in checkFor:
        for j in range(len(item)):
            if item[j] == i:
                return True
            else:
                return False





