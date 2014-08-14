class Board:

	def __init__(self, rowSize, columnSize):
		self.rowSize = rowSize
		self.columnSize = columnSize
		self.boardArray = [["-" for x in xrange(rowSize)] for x in xrange(columnSize)]

	def isSpaceOccupied(self, rowLoc, colLoc):
		if self.boardArray[rowLoc][colLoc] != "-":
			return True
		else:
			return False

	def printBoard(self):
		for rowIndex in range(self.rowSize):
			for columnIndex in range(self.columnSize):
				print("|" + str(self.boardArray[rowIndex][columnIndex]) + "|"),
			print

