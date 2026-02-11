import random
from game_logic import GameLogic
from game_solver import GameSolver
from game_board import GameBoard

def main():
    game = GameBoard(4, 1)
    GameLogic.randomTile(game.board)
    numMoves = 0
    while True:
        
        numMoves += 1
        tempBoard = [row[:] for row in game.board]
        direction = GameSolver.greedyHeuristic(game.board, game.heuristicBoard)
        print(direction)
        tempBoard, score = GameLogic.shiftBoard(tempBoard, direction)
        game.board = [row[:] for row in tempBoard]
        if GameLogic.checkWin(game.board):
            print("win")
            print(numMoves)
            for i in range(game.boardSize):
                print(game.board[i])
            break
        if GameLogic.checkLose(game.board):
            print("lose")
            print(numMoves)
            for i in range(game.boardSize):
                print(game.board[i])
            break

        GameLogic.randomTile(game.board)
        for i in range(game.boardSize):
            print(game.board[i])


if __name__ == '__main__':
    main()
