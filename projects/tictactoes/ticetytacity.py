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
                board[i][j].isAvailable = True
                count += 1
    if count == 9:
        return True
    else:
        return False

def inputthingie(input):
    splitthing = nr.splitter(input, ",")
    for i in range(len(splitthing)):
        if nr.intcheck(splitthing[i]):
            splitthing[i] = int(splitthing[i])
        else:
            return False
    return splitthing

def inputLoop(board):
    display = board

    count = 0
    finished = False
    while not(finished):
        splat = inputthingie(input("enter the coordinate in the format \'X,Y\'."))
        if not splat:
            print("enter the coordinates please")
        elif len(splat) != 2:
            print("enter the coordinates as instructed please")
        else:
            if whosTurn(count):
                if board[splat[0]][splat[1]].isAvailable:
                    board[splat[0]][splat[1]].changeToX()
                    count += 1
                    displayBoardCLI(board)
            elif not(whosTurn(count)):
                if board[splat[0]][splat[1]].isAvailable:
                    board[splat[0]][splat[1]].changeToO()
                    count += 1
                    displayBoardCLI(board)

def whosTurn(count):
    if count % 2 == 0 or count == 0:
        return True # return True for X
    else:
        return False # return False for O



def displayBoardCLI(board):
    display = board
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            space = board[i][j]
            display[i][j] = space.currentToken
    os.system('cls')
    nr.print2Dnicely(display)

ticBoard = TicBoard().boardCreate()
print(checkIfINITCorrect(ticBoard))
inputLoop(ticBoard)



