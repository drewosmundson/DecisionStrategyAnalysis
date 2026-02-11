
import random
class GameLogic:  
    #2048 game logic
    #from a given direction, move all tiles in that direction
    #if two tiles of the same value collide, combine them
    #returns 1 if game is over, 0 if game is not over
    @staticmethod
    def checkWin(board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 2048: #32768:
                    return True
        return False
    @staticmethod
    def checkLose(board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    return False
        return True
    
    @staticmethod
    def getHighestValueTile(board):
        highestValueTile = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] > highestValueTile:
                    highestValueTile = board[i][j]
        return highestValueTile
    
    @staticmethod
    def randomTile(board, twoFrequency = 0.8, fourFrequency = 0.2):
        boardSize = len(board)
        emptyTiles = []
        for i in range(boardSize):
            for j in range(boardSize):
                if board[i][j] == 0:
                    emptyTiles.append([i, j])
        if len(emptyTiles) == 0:
            return board
        randomTile = random.choice(emptyTiles)
        fourOrTwo = random.choices([2, 4], [twoFrequency, fourFrequency])[0]
        board[randomTile[0]][randomTile[1]] = int(fourOrTwo)
        return board
    
    @staticmethod
    def heuristicScoreCheck(board, heuristicBoard):
        heuristicScore = 0
        for i in range(len(board)):
            for j in range(len(board)): 
                heuristicScore += heuristicBoard[i][j] * board[i][j]      
        return heuristicScore

#https://www.codespeedy.com/how-to-build-2048-game-in-python/

    @staticmethod
    def compress(mat):
        new_mat=[[0 for i in range(4)] for i in range(4)]     
        for i in range(4):
            pos=0
            for j in range(4):
                if mat[i][j]!=0:
                    new_mat[i][pos]=mat[i][j]             #This compress function is for lest move.
                    pos+=1
        return new_mat
    
    @staticmethod
    def merge(mat):
        score = 0
        for i in range(4):
            for j in range(3):
                if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                    mat[i][j]+=mat[i][j]                     #This merge function is for left move.
                    mat[i][j+1]=0
                    score += mat[i][j]
        return mat, score
    
    @staticmethod
    def reverse(mat):
        new_mat=[]
        for i in range(4):
            new_mat.append([])
            for j in range(4):
                new_mat[i].append(mat[i][3-j])
        return new_mat
    
    @staticmethod
    def transp(mat):
        new_mat=[[0 for i in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                new_mat[i][j]=mat[j][i]
        return new_mat

    @staticmethod
    def shiftBoard(board, direction):
        if direction == 1:
            return GameLogic.shiftUp(board)
        elif direction == 2:
            return GameLogic.shiftDown(board)
        elif direction == 3:
            return GameLogic.shiftLeft(board)
        elif direction == 4:
            return GameLogic.shiftRight(board)
        else:
            raise ValueError("Invalid direction: " + direction)
        
    @staticmethod
    def shiftLeft(board):
        board = GameLogic.compress(board)
        board, score = GameLogic.merge(board)
        board = GameLogic.compress(board)
        return board, score
    
    @staticmethod
    def shiftRight(board):
        board = GameLogic.reverse(board) #oreient board
        board = GameLogic.compress(board)
        board, score = GameLogic.merge(board)
        board = GameLogic.compress(board)
        board = GameLogic.reverse(board) #unorient board
        return board, score
    
    @staticmethod
    def shiftUp(board):
        board = GameLogic.transp(board) #oreient board 
        board = GameLogic.compress(board) 
        board, score = GameLogic.merge(board)
        board = GameLogic.compress(board)
        board = GameLogic.transp(board)
        return board,score
    
    @staticmethod
    def shiftDown(board):
        board = GameLogic.transp(board) #oreient board
        board = GameLogic.reverse(board)
        board = GameLogic.compress(board)
        board, score = GameLogic.merge(board)
        board = GameLogic.compress(board) #unorient board
        board = GameLogic.reverse(board)
        board = GameLogic.transp(board)
        return board, score