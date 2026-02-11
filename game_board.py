

# Solve methods
# Manual(testing)
# Random
# Greedy
# MonteCarlo
#Creates the board object to keep track of the current game instance
class GameBoard:
    boardSize = 4
    solveMethod = 1
    board = [[0] * 4 for i in range(4)]
    gameScore = 0
    highestValueTile = 0
    numMoves = 0
    heuristicBoard = [[2048, 1024, 512, 256],
                      [128, 64, 32, 16],
                      [8, 4, 2, 1],
                      [1, 1, 1, 1]]

    def __init__(self, _boardSize, _solveMethod): #, _fourFrequency):
        if(_boardSize < 2):
            return -1
        if(_solveMethod != 1 and _solveMethod != 2 and _solveMethod != 3 and _solveMethod != 4):
            return -1
        self.solveMethod = _solveMethod
        self.board = [[0] * _boardSize for i in range(_boardSize)]
        self.heuristicBoard = [[0] * _boardSize for i in range(_boardSize)]
        for i in range(_boardSize):
            for j in range(_boardSize):
                self.heuristicBoard[i][j] = (2 ** i) * (2 ** (j * _boardSize))
        