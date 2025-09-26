
size = 0
for i in range(-20,0):
    print(" "*size + "*"*(abs(i)-1) + "*"*(abs(i)))
    if size != 20:
        size += 1

for i in range(0,20):
    print(" "*size + "*"*(abs(i)) + "*"*(abs(i)-1))
    if size != 0:
        size -= 1