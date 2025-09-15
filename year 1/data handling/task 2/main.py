import os
from nlib import novasroutines as nr

log = nr.logInit("data handling/main.py")

print(os.listdir("./txtdata"))
balls = open("balls.csv", "wt+")
balls.write("First Name, Last Name\n")
numitems = len(os.listdir("./txtdata"))# pointless ass code

print(numitems)

for i in range(numitems):
    directory = f"./txtdata/New Text Document - Copy ({i+2}).txt"
    with open(directory, "rt") as f:
        contents = f.read()
        contents = contents.replace("\n", " ")
        contents = contents.split(" ")
        for j in range(len(contents)-1):
            if contents[j-1] == "":
                del contents[j-1]
        balls.write(f"{contents[1]}, {contents[3]}\n")