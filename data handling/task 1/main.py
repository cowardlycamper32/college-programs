import pandas as pdd
data = open("data.csv", "r")
length = open("data.csv", "r")
file = open("separated.csv", "wt")
file.write("Last Name, First Name\n")

data.readline()
print(data.readline())
line_count = 0
for line in length:
    line_count += 1

for line in range(line_count):
    file.write(data.readline())

data.close()
length.close()
file.close()

file = open("separated.csv", "r")

df = pdd.read_csv("separated.csv")
print(df)



print(df)

df.to_csv('separated_names.csv', index=False)
