import nlib
from nlib import novastestvalues as nt
from nlib import novasroutines as nv

allowed = False
username = ""
disallowed = nt.specialChars

'''while not(allowed):
    username = input("Please enter your username: ")
    validinput = nr.checkForX(username, disallowed)
    if validinput:
        allowed = True
    else:
        allowed = False'''
username = input("Please enter your username: ")
for i in disallowed:
    for j in range(len(username)):
        if username[j] == i:
            print(username[j] + " has a disallowed character.")
        else:
            print(username[j] + " has a been allowed.")