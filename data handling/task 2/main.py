import os

print(os.listdir("./txtdata"))
balls = open("./balls.csv", "wt")

for i in range(12):
    directory = f"./txtdata/New Text Document - Copy ({i+2}).txt"
    with open(directory, "rt") as f:
       names = f.read()
       balls.write(names.split[" "][1])
