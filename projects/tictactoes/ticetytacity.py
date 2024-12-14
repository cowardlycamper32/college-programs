import os


from nlib import novasroutines as nr, novasclasses as nc


class TicBoard():
    def __init__(self):
        pass

    def boardCreate(self):
        board = [[nc.ticSpace(0, 0, False, False), nc.ticSpace(1, 0, False, False), nc.ticSpace(2, 0, False, False)],
                 [nc.ticSpace(0, 1, False, False), nc.ticSpace(1, 1, False, False), nc.ticSpace(2, 1, False, False)],
                 [nc.ticSpace(0, 2, False, False), nc.ticSpace(1, 2, False, False), nc.ticSpace(2, 2, False, False)]]
        return board


def checkIfINITCorrect(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            space = board[i][j]
            if not(space.isAnX) and not(space.isAnO):
                space.isAvailable = True
                count += 1
    if count == 9:
        return True
    else:
        return False


def inputthingie(input):
    splitthing = nr.splitter(input, ",")
    while not all(nr.intcheck(item) for item in splitthing):
        print("Enter the coordinates please")
        inputthingie(input())
    return [int(x) for x in splitthing]


def inputLoop(board, display):
    count = 0
    finished = False
    while not(finished):
        splat = inputthingie(input("Enter the coordinate in the format 'X,Y' (or 'quit' to exit): "))
        if splat == ['quit']:
            print('Game exited')
            break;
        elif len(splat) != 2:
            print("Enter the coordinates as instructed please")
        else:
            if whosTurn(count):
                if board[splat[0]][splat[1]].isAvailable:
                    board[splat[0]][splat[1]].isAvailable = False
                    board[splat[0]][splat[1]].isX = True
                    count += 1
            elif not(whosTurn(count)):
                if board[splat[0]][splat[1]].isAvailable:
                    board[splat[0]][splat[1]].isAvailable = False
                    board[splat[0]][splat[1]].isO = True
                    count += 1
            else:
                finished = True

    displayBoardCLI(board, display)


def whosTurn(count):
    if count % 2 == 0 or count == 0:
        return True # return True for X
    else:
        return False # return False for O


def displayBoardCLI(board, display):

    for i in range(len(board)):
        for j in range(len(board[i])):
            space = board[i][j]
            if display[i][j] == " ":
                display[i][j] = ""
            elif display[i][j] == "X":
                display[i][j] = "O"
    nr.print2Dnicely(display)
    print()
    return display


initdisplay = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]
ticBoard = TicBoard().boardCreate()
if checkIfINITCorrect(ticBoard):
    inputLoop(ticBoard, initdisplay)

else:
    print("The initial board is not correct")

print("This is a test")
