class Book():
    def __init__(self, title, author, year, isbn, status):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.status = status

class ticSpace():
    def __init__(self, x: int, y: int, isAnX: bool, isAnO: bool):
        self.x = x
        self.y = y
        self.isAnX = isAnX
        self.isAnO = isAnO
    def changeToX(self, x, y):
        self.x = x
        self.y = y
        self.isAnX = True
        self.isAnO = False
    def changeToO(self, x, y):
        self.x = x
        self.y = y
        self.isAnO = True
        self.isAnX = False

