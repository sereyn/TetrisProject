from random import choice

def getBlockList(letter):
	if letter == "o":
		return [
			[1, 1],
			[1, 1]
		]
	if letter == "i":
		return [
			[0, 0, 0, 0],
			[2, 2, 2, 2],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	if letter == "j":
		return [
			[0, 0, 0],
			[3, 3, 3],
			[0, 0, 3]
		]
	if letter == "l":
		return [
			[0, 0, 0],
			[4, 4, 4],
			[4, 0, 0]
		]
	if letter == "s":
		return [
			[0, 0, 0],
			[0, 5, 5],
			[5, 5, 0],
		]
	if letter == "z":
		return [
			[0, 0, 0],
			[6, 6, 0],
			[0, 6, 6],
		]
	if letter == "t":
		return [
			[0, 0, 0],
			[7, 7, 7],
			[0, 7, 0],
		]

class Block():
	def __init__(self, gameBoard=None, cols=0):
		self.mat = getBlockList(choice(["o", "i", "j", "l", "s", "z", "t"]))
		if gameBoard == None:
			self.x = cols
		else:
			self.x = int(gameBoard.cols/2-len(self.mat)/2)
		self.y = 0
		self.cols = self.x
	def newBlock(self):
		self.__init__(None, self.cols)
	def rotate(self, inverse=False):
		if inverse:
			for i in range(3):
				self.rotate()
		else:
			N = len(self.mat)
			for x in range(0, int(N/2)):
				for y in range(x, N-x-1):
					temp = self.mat[x][y]
					self.mat[x][y] = self.mat[y][N-1-x]
					self.mat[y][N-1-x] = self.mat[N-1-x][N-1-y]
					self.mat[N-1-x][N-1-y] = self.mat[N-1-y][x]
					self.mat[N-1-y][x] = temp
	def hasProblem(self, gB):
		for i in range(len(self.mat[0])):
			for j in range(len(self.mat)):
				if self.mat[j][i] != 0:
					xx, yy = self.x+i, self.y+j
					if yy >= gB.lines or xx >= gB.cols or xx < 0:
						return True
					else:
						if gB.grid[yy][xx] != 0:
							return True
		return False
