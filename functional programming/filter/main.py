

def evenfilt(number):
    if number % 2 == 0:
        return True
    else:
        return False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(evenfilt, numbers)))

def greaterthanfivefilt(stringg):
    if len(stringg) > 5:
        return True
    else:
        return False
strings = ["apple", "banana", "kiwi", "cherry", "blueberry"]
print(list(filter(greaterthanfivefilt, strings)))

def containsafilt(stringg):
    if "a" in stringg:
        return True
    else:
        return False
strings = ["apple", "banana", "kiwi", "cherry", "grape"]
print(list(filter(containsafilt, strings)))

def oddfilt(number):
    if number % 2 == 0:
        return False
    else:
        return True
print(list(filter(oddfilt, numbers)))