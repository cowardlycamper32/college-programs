from nlib import novasroutines as nr, novasclasses as nc


class TicBoard():
    def __init__(self):
        pass
    def boardCreate(self):
        board = [[nc.ticSpace(0, 0, False, False), nc.ticSpace(1, 0, False, False), nc.ticSpace(2, 0, False, False)],
                 [nc.ticSpace(0, 1, False, False), nc.ticSpace(1, 1, False, False), nc.ticSpace(2, 1, False, False)],
                 [nc.ticSpace(0, 2, False, False), nc.ticSpace(1, 2, False, False), nc.ticSpace(2, 2, False, False)]]
        return board

ticBoard = TicBoard().boardCreate()
for i in range(len(ticBoard)):
    for j in range(len(ticBoard[i])):
        space = ticBoard[i][j]
        if not(space.isAnX) and not(space.isAnO):
            ticBoard[i][j].isAvailable = True


