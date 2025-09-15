from nlib.novasroutines import splitter, intcheck

class Computer:
    def __init__(self, moves):
        self.moves = moves
    def normalCPU(self):
        self.moves = [[["2,2", "2,1", "3,3"],["2,2", "1,1", "1,3", "3,1", "3,3", "3,2"],["2,2", "3,1", "3,3", "1,1", "1,2"]],
                      [["3,3", "3,1", "2,3"],["1,3","3,1"],["2,1", "1,3", "3,3"]],
                      [["2,2","1,3"],["3,1", "3,3", "1,2", "2,3"],["1,1", "3,1", "1,3", "3,2"]]]

    def TurnCPU(self, lastmove, board):
        for i in range(len(lastmove)):
            if intcheck(lastmove[i]):
                lastmove[i] = int(lastmove[i])
        for i in self.moves[lastmove[0]][lastmove[1]]:
            temp = splitter(i, ",")
            for j in range(len(temp)):
                if intcheck(temp[j]):
                    temp[j] = int(temp[j])
            if board[temp[0] - 1][temp[1] - 1].isAvailable:
                board[temp[0] - 1][temp[1] - 1].changeToO()
                return board
            else:
                pass
