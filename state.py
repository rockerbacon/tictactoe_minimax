NONE = 0
CROSS = 1
CIRCLE = -1

class TicTacToe:
	def __init__(self):
		self.lineCount = [0 for i in range(3)]
		self.columCount = [0 for i in range(3)]
		self.firstDiagonalCount = 0
		self.secondDiagonalCount = 0
		
		self.game = [[NONE for j in range(3)] for i in range(3)]
		self.plays = 0
		self.value = NONE	
		
	def play(self, play, i, j):
		if self.game[i][j] == NONE:
			self.game[i][j] = play
			self.plays += 1
			
			#atualizar avaliacao do jogo e retorna vencedor caso haja um
			self.lineCount[i] += play
			if self.lineCount[i] == 3*play:
				self.value = play
				
			self.columCount[j] += play
			if self.columCount[j] == 3*play:
				self.value = play
				
			if i == j:
				self.firstDiagonalCount += play
				if self.firstDiagonalCount == 3*play:
					self.value = play
			if i == abs(j-2):
				self.secondDiagonalCount += play
				if self.secondDiagonalCount == 3*play:
					self.value = play
					
			#self.printSelf()	#debug
			#print(self.lineCount)	#debug
			#print(self.columCount)	#debug
			#print(self.firstDiagonalCount, self.secondDiagonalCount)	#debug
			#print(self.value, end='\n\n')	#debug
		
	def canPlay(self):
		return self.plays == 9
		
	def printSelf(self):
		for i in range(3):
			for j in range(3):
				if self.game[i][j] == CROSS:
					print('\033[1;37m x', end=' ')
				elif self.game[i][j] == CIRCLE:
					print('\033[0;31m o', end=' ')
				else:
					print('\033[1;30m', i*3+j, end=' ')
			print(end='\n')		
