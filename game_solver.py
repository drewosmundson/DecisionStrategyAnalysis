import random
from game_logic import GameLogic
class GameSolver:
#different methods for determining move
    #each will return a direction for the game board to be moved
    #up, down left and right
    #manual method for testing
    @staticmethod
    def manual():
        direction = input("Enter direction: ")
        if direction == "w":
            direction = 1
        elif direction == "s":
            direction = 2
        elif direction == "a":
            direction = 3
        elif direction == "d":
            direction = 4
        else:
            direction = GameSolver.randomDirection()
        return direction
    
    #random method to pick direction
    @staticmethod
    def randomDirection():
        direction = random.choice([1,2,3,4])
        return direction
    
    #plays the move which will result in the highest value tile from the current board state
    #by calling the gameLogic function on each possible move and comparing the scores
    #for up, down, left and right
    @staticmethod
    def greedyScore(board):
        direction = 0
        maxScore = 0
        for i in range(1, 5):                      #for each direction
            board, score = GameLogic.shiftBoard(board, i)  
            if score > maxScore:          #shiftResult[1] is the second element in tuple (board, score)
                maxScore = score
                direction = i
        if direction == 0:
            direction = GameSolver.randomDirection()
        return direction
    
    @staticmethod
    def greedyHeuristic(board, heuristicBoard):
        direction = 0
        maxScore = 0
        i = 1
        for i in range(1, 5):
            board, tempScore = GameLogic.shiftBoard(board, i)            
            tempScore = GameLogic.heuristicScoreCheck(board, heuristicBoard)       #extra line from regular greedy algotithm to use compare score from greedy heuristic
            if tempScore > maxScore: 
                maxScore = tempScore
                direction = i
        if direction == 0:
            direction = GameSolver.randomDirection()
        return direction

    #monte carlo method
    #https://stanford-cs221.github.io/autumn2019-extra/posters/4.pdf
    #how are games differetn than depth 
    #will need to simullate the spawning of 2s and 4s thats what makes it different and not jsut thhe same greedy algorithm
    #random moves from the simualator of the game are simulated and the best move is chosen 
    #all directions or greedy algorithm for use of pruning
    @staticmethod
    def monteCarlo(board, heuristicBoard):
        bestAverageScore = 0
        bestDirection = 0
        for x in range(1, 5):
            directionBoard = [row[:] for row in board]
            directionBoard, score = GameLogic.shiftBoard(directionBoard, x, )
            averageScore = 0
            for i in range(1):
                simulatedScore = 0
                simulatedBoard = [row[:] for row in directionBoard]
                GameLogic.randomTile(simulatedBoard)   # Randomly add a tile to the board
                numSimulatedMoves = 0
                while numSimulatedMoves < 1:
                    direction = GameSolver.greedyHeuristic(simulatedBoard, heuristicBoard)
                    simulatedShiftedBoard, moveScore = GameLogic.shiftBoard(simulatedBoard, direction)
                    simulatedScore += moveScore
                    GameLogic.randomTile(simulatedShiftedBoard)
                    numSimulatedMoves += 1
                    if GameLogic.checkLose(simulatedShiftedBoard):
                        break
                averageScore = averageScore * i
                averageScore = (averageScore + simulatedScore) / (i + 1)
            if averageScore > bestAverageScore:
                bestAverageScore = averageScore
                bestDirection = x
        print(bestDirection)
        return bestDirection
    
    def monteCarlo(board, boardSize, heuristicBoard):
        boardCopy = [row[:] for row in board]





    #expectimax method
    #heuristics based on highest score
    #all possible moves and random spawns from empty spaces are considered and the best move is chosen
    @staticmethod
    def expectimax(board):
        direction = 0
        return direction


    #heruistic based on highest tile value
    #is the heuristic the highest value tile on the board? or the score?
    #or the number of empty tiles? or the number of tiles with the same value next to each other? for a map
    @staticmethod
    def minimaxAlphaBeta(board):
        direction = 0
        return direction
    