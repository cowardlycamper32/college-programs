class ChessBoard:
    def __init__(self):
        self.board = [[" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "]]


class ChessSpace:
    def __init__(self, x, y, piece):
        self.piece = piece
        self.x = x
        self.y = y


class Piece:
    def __init__(self, pieceName, pieceToken, regularMoves, takingMoves):
        self.pieceName = pieceName
        self.pieceToken = pieceToken
        self.regularMoves = regularMoves
        self.takingMoves = takingMoves
    def checkValidMoves(self, board, attemptedMove):
        pass


piece = Piece("pawn", "P", [[" ", ".", " "],
                                                            [" ", ".", " "],
                                                            [" ", "X", " "]], [[" ", " ", " "],
                                                                                          [".", " ", "."],
                                                                                          [" ", "X", " "]])