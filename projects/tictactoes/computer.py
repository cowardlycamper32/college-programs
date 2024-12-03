class Computer:
    def __init__(self, moves):
        self.moves = moves
    def normalCPU(self):
        self.moves = [[["2,2", "3,3"],["2,2", "1,1", "1,3", "3,1", "3,3"],["2,2", "3,1", "3,3", "1,1"]],
                      [["3,3", "3,1", "2,3"],["1,3","3,1"],["2,1"]],
                      [[],[],["1,1"]]]