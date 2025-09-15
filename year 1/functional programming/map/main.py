def double(number):
    return number * 2
x = [1, 2, 3, 4]
print(list(map(double, x)))

def convert(stringg):
    return int(stringg)
x = ["1", "2", "3", "4"]
print(list(map(convert, x)))

def upperthing(string):
    return string.upper()
x = ["apple", "banana", "cherry"]
print(list(map(upperthing, x)))

def lenthcalc(string):
    return len(string)
x = ["apple", "banana", "cherry"]
print(list(map(lenthcalc, x)))

