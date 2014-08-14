import boardgame
import random
from collections import deque

def main():
    typeOfGame = input('Choose Type Of Game To Play (1 for TicTacToe, 2 for ConnectFour, 3 for MegaTicTacToe): ')
    gameState = None
    if typeOfGame == 1:
    	#create tictactoegame
    	gameState = boardgame.BoardGame("TicTacToe")
        #keep prompting for input
        gameWon = False
        playerTurn = 0
        gameState.boardArr.printBoard()
        movePlaced = False
        while gameWon == False:
            rowLoc = random.randint(0,2)
            colLoc = random.randint(0,2)
            movePlaced == False
            print movePlaced
            while gameState.boardArr.isSpaceOccupied(rowLoc,colLoc) == False:
                if gameState.boardArr.isSpaceOccupied(rowLoc,colLoc) == True:
                    rowLoc = random.randint(0,2)
                    colLoc = random.randint(0,2)
                else:
                    if playerTurn == 0:
                        gameState.boardArr.boardArray[rowLoc][colLoc] = "A"
                        playerTurn = 1
                        movePlaced = True
                        break
                    else:
                        gameState.boardArr.boardArray[rowLoc][colLoc] = "B"
                        playerTurn = 0
                        break
            gameState.boardArr.printBoard()
            gameWon = gameState.hasWon("TicTacToe")
            print "GAME WON"
    elif typeOfGame == 2:
        #play connect four
        gameState = boardgame.BoardGame("ConnectFour")
        gameWon = False
        playerTurn = 0
        gameState.boardArr.printBoard()
        movePlaced = False
        while gameWon == False:
            #randomly select column number
            gameState.makeConnectFourMove(playerTurn)
            if playerTurn == 0:
                playerTurn = 1
            else:
                playerTurn = 0
            print "move made"
            gameState.boardArr.printBoard()
            gameWon = gameState.hasWon("ConnectFour")
    elif typeOfGame == 3:
        gameState = boardgame.BoardGame("MegaTicTacToe")
        gameWon=False
        playerQueue = deque(["A","B","C","D"])
        while gameWon == False:
            rowLoc = random.randint(0,7)
            colLoc = random.randint(0,7)
            while gameState.boardArr.isSpaceOccupied(rowLoc,colLoc) == False:
                if gameState.boardArr.isSpaceOccupied(rowLoc,colLoc) == True:
                    rowLoc = random.randint(0,7)
                    colLoc = random.randint(0,7)
                else:
                    pieceToPlay = playerQueue.popleft()
                    gameState.boardArr.boardArray[rowLoc][colLoc] = pieceToPlay
                    playerQueue.append(pieceToPlay)
                    break
            print "made move"
            gameState.boardArr.printBoard()
            gameWon = gameState.hasWon("MegaTicTacToe")

if __name__ == "__main__":
    main()
