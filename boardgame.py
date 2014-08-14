import board
import random
class BoardGame:
	def __init__(self, typeOfGame):
		if typeOfGame == "TicTacToe":
			self.boardArr = board.Board(3,3)
			self.playerCount = 2
			self.connectionLength = 3
			self.playingPlayer = "A"
			self.typeOfGame = typeOfGame
		elif typeOfGame == "ConnectFour":
			self.boardArr = board.Board(6,6)
			self.playerCount = 2
			self.connectionLength = 4
			self.playingPlayer = "A"
			self.typeOfGame = typeOfGame
		elif typeOfGame == "MegaTicTacToe":
			self.boardArr = board.Board(8,8)
			self.playerCount = 4
			self.connectionLength = 3
			self.playingPlayer = "A"
			self.typeOfGame = typeOfGame	

	def makeMove(self, rowLoc, colLoc):
		if boardArr.isSpaceOccupied(rowLoc, colLoc):
			return None
		else:
			boardArr[rowLoc][colLoc] = self.playingPlayer
		if self.playingPlayer == "A":
			self.playingPlayer = "B"
		else:
			self.playingPlayer = "A"

	def makeConnectFourMove(self, playerNum):
		pieceToPut = None
		if playerNum == 0:
			pieceToPut = "A"
		else:
			pieceToPut = "B"
		movePlaced = False
		while movePlaced == False:
			colLoc = random.randint(0,5)
			for rowLoc in range(5,-1,-1):
				if self.boardArr.boardArray[rowLoc][colLoc] == "-":
					self.boardArr.boardArray[rowLoc][colLoc] = pieceToPut
					movePlaced = True
					break

	def hasWon(self,typeOfGame):
		if typeOfGame == "TicTacToe":
			#check row
			boardToCheck = self.boardArr.boardArray
			#check column
			for i in range(0, self.boardArr.columnSize):
				if boardToCheck[0][i] == boardToCheck[1][i] == boardToCheck[2][i] and boardToCheck[0][i]!="-":
					return True

			for i in range(0, self.boardArr.rowSize):
				if boardToCheck[i][0] == boardToCheck[i][1] == boardToCheck[i][2] and boardToCheck[i][0]!="-":
					return True

			#check Diag Up to Right
			if boardToCheck[0][0] == boardToCheck[1][1] == boardToCheck[2][2] and boardToCheck[0][0]!="-":
				return True

			#check Diag bottom left To top right
			elif boardToCheck[0][2] == boardToCheck[1][1] == boardToCheck[2][0] and boardToCheck[0][2]!="-":
				return True

			else:
				return False
		elif typeOfGame == "ConnectFour":
			boardToCheck = self.boardArr.boardArray
			#check rows
			for row in range(0,self.boardArr.rowSize):
				for col in range(0, 3):
					if boardToCheck[row][col] == boardToCheck[row][col+1] == boardToCheck[row][col+2] == boardToCheck[row][col+3] and boardToCheck[row][col]!="-":
						print "4 in row"
						return True
			#check columns
			for col in range(0,self.boardArr.columnSize):
				for row in range(0, 3):
					if boardToCheck[row][col] == boardToCheck[row+1][col] == boardToCheck[row+2][col] == boardToCheck[row+3][col] and boardToCheck[row][col]!="-":
						print "4 in col"
						return True
			#check diag bottom left to top right
			for row in range(5,2,-1):
				for col in range(3):
					if boardToCheck[row][col] == boardToCheck[row-1][col+1] == boardToCheck[row-2][col+2] == boardToCheck[row-3][col+3] and boardToCheck[row][col]!="-":
						print "diag bottom left to top right"
						return True
			#check diagonals up to right
			for row in range(0,3):
				for col in range(3):
					if boardToCheck[row][col] == boardToCheck[row+1][col+1] == boardToCheck[row+2][col+2] == boardToCheck[row+3][col+3] and boardToCheck[row][col]!="-":
						print "diag up to right"
						return True
			return False
		elif typeOfGame == "MegaTicTacToe":
			boardToCheck = self.boardArr.boardArray
			#diag left to right
			for row in range(0,5):
				for col in range(0,5):
					if boardToCheck[row][col] == boardToCheck[row+1][col+1] == boardToCheck[row+2][col+2] and boardToCheck[row][col] != "-":
						print row
						print col
						print "lefttoright"
						return True
			#diag right to left
			for row in range(7,1,-1):
				for col in range(0,6):
					if boardToCheck[row][col] == boardToCheck[row-1][col+1] == boardToCheck[row-2][col+2] and boardToCheck[row][col] !="-":
						print row 
						print col
						print"righttoleft"
						return True
			return False
