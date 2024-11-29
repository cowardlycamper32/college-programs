import os

from nlib import novasroutines as nr, novasclasses as nc


class TicBoard():
    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
    def boardCreate(self):
        board = [[nc.ticSpace(0, 0, False, False), nc.ticSpace(1, 0, False, False), nc.ticSpace(2, 0, False, False)],
                 [nc.ticSpace(0, 1, False, False), nc.ticSpace(1, 1, False, False), nc.ticSpace(2, 1, False, False)],
                 [nc.ticSpace(0, 2, False, False), nc.ticSpace(1, 2, False, False), nc.ticSpace(2, 2, False, False)]]
        return board
    def wincheck(self, board, count):
        if board[0][0].isAnX and board[1][0].isAnX and board[2][0].isAnX:
            return True
        elif board[0][1].isAnX and board[1][1].isAnX and board[2][1].isAnX:
            return True
        elif board[0][2].isAnX and board[1][2].isAnX and board[2][2].isAnX:
            return True
        elif board[0][0].isAnX and board[0][1].isAnX and board[0][2].isAnX:
            return True
        elif board[1][0].isAnX and board[1][1].isAnX and board[1][2].isAnX:
            return True
        elif board[2][0].isAnX and board[2][1].isAnX and board[2][2].isAnX:
            return True
        elif board[0][0].isAnX and board[1][1].isAnX and board[2][2].isAnX:
            return True
        elif board[2][0].isAnX and board[1][1].isAnX and board[0][2].isAnX:
            return True
        elif count == 9:
            return "draw"
        else:
            return False




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

def inputthingie(funcInput):
    splitthing = nr.splitter(funcInput, ",")
    for i in range(len(splitthing)):
        if nr.intcheck(splitthing[i]):
            splitthing[i] = int(splitthing[i])
        else:
            return False
        splitthing[i] -= 1
    return splitthing

def inputLoop(board):
    display = board
    displayBoardCLI(board)

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
                    board = displayBoardCLI(board)
            elif not(whosTurn(count)):
                if board[splat[0]][splat[1]].isAvailable:
                    board[splat[0]][splat[1]].changeToO()
                    count += 1
                    board = displayBoardCLI(board)
        if board.wincheck(display, count):
            print("You won!")
            finished = True
        elif board.wincheck(display, count) == "draw":
            print("Draw!")
            finished = True
        elif not board.wincheck(display, count):
            print("You loose!")
            finished = True
        else:
            print("HOW THE FUCK DID YOU GET HERE???")
            exit()
def whosTurn(count):
    if count % 2 == 0 or count == 0:
        return True # return True for X
    else:
        return False # return False for O



def displayBoardCLI(board):
    display = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            space = board[i][j]
            display[i][j] = space.currentToken
    os.system('cls')

    nr.print2Dnicely(display)
    return board

ticBoard = TicBoard().boardCreate()

print(checkIfINITCorrect(ticBoard))
inputLoop(ticBoard)



