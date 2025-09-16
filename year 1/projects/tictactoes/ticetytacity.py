import os

from nlib import novasroutines as nr, novasclasses as nc
import computer as cpu
lastmove = ["",""]

class TicBoard():
    def __init__(self):
        board = [[" ", " ", " "],
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
        elif board[0][0].isAnO and board[1][0].isAnO and board[2][0].isAnO:
            return False
        elif board[0][1].isAnO and board[1][1].isAnO and board[2][1].isAnO:
            return False
        elif board[0][2].isAnO and board[1][2].isAnO and board[2][2].isAnO:
            return False
        elif board[0][0].isAnO and board[0][1].isAnO and board[0][2].isAnO:
            return False
        elif board[1][0].isAnO and board[1][1].isAnO and board[1][2].isAnO:
            return False
        elif board[2][0].isAnO and board[2][1].isAnO and board[2][2].isAnO:
            return False
        elif board[0][0].isAnO and board[1][1].isAnO and board[2][2].isAnO:
            return False
        elif board[2][0].isAnO and board[1][1].isAnO and board[0][2].isAnO:
            return False
        elif count == 9:
            return "draw"
        else:
            return "continue"





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
            if splitthing[i] > 3 or splitthing[i] < 0:
                return False
        else:
            return False
        splitthing[i] -= 1
    return splitthing

def inputLoop(objectBoard, board, computerYes, computer):
    display = board
    displayBoardCLI(board)

    count = 0
    finished = False
    while not(finished):
        if whosTurn(count):
            splat = inputthingie(input("enter the coordinate in the format \'X,Y\'."))
            if not splat:
                print("enter the coordinates please")
            elif len(splat) != 2:
                print("enter the coordinates as instructed please")
            else:
                if board[splat[0]][splat[1]].isAvailable:
                    board[splat[0]][splat[1]].changeToX()
                    count += 1
                    board = displayBoardCLI(board)
                    lastmove = splat
        elif not(whosTurn(count)):
            if computerYes:
                temp = computer.TurnCPU(lastmove, board)
                count += 1
                temp = displayBoardCLI(temp)
            else:
                splat = inputthingie(input("enter the coordinate in the format \'X,Y\'."))
                if not splat:
                    print("enter the coordinates please")
                elif len(splat) != 2:
                    print("enter the coordinates as instructed please")
                else:
                    if board[splat[0]][splat[1]].isAvailable:
                        board[splat[0]][splat[1]].changeToO()
                        count += 1
                        board = displayBoardCLI(board)
                        lastmove = splat
        if objectBoard.wincheck(display, count) == "continue":
            pass
        elif objectBoard.wincheck(display, count) == "draw":
            print("Draw!")
            finished = True
        elif objectBoard.wincheck(display, count):
            print("You Win!")
            finished = True
        elif not objectBoard.wincheck(display, count):
            print("You Lose!")
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
    nr.clearer()

    nr.print2Dnicely(display)
    return board

def computerTurn(board, computer):

    computer.normalCPU()
    computermoves = computer.moves

def computerDiff(computer):
    if input("use normal difficulty?").lower() == "yes":
        computer.normalCPU()
    else:
       exit()


INITBoard = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
ticBoard = TicBoard()
regboard = ticBoard.boardCreate()
computer = cpu.Computer(regboard)
if input("use AI?").lower() == "yes":
    useComputer = True
    computerDiff(computer)
else:
    useComputer = False


print(checkIfINITCorrect(regboard))
inputLoop(ticBoard, regboard, useComputer, computer)



