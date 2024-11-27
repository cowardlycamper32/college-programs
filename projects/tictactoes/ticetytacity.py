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


ticBoard = TicBoard().boardCreate()
print(checkIfINITCorrect(ticBoard))

