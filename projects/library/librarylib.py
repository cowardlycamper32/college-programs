from nlib import novasroutines as nr
from nlib.novasclasses import Book


def libsetup(listOfFields):

    setup = input("please enter the information of a book in this format " + str(listOfFields) + ":\n")
    items = nr.splitter(setup, ',')
    print(items)
    for index in range(len(items)):
        items[index] = items[index].strip()
    print(items)
    if len(items) != len(listOfFields):
        print("Error X000: Invalid Input")
        return False
    else:
        book = Book(items[0], items[1], items[2], items[3], True)
        print(book)

    return book
