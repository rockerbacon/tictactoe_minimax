from state import TicTacToe, NONE, CROSS, CIRCLE
from copy import deepcopy

#
# state = estado a partir do qual buscar
# myTurn = jogada que o jogador fara (CROSS ou CIRCLE)
# opponentTurn = jogada que o oponente fara (CROSS ou CIRCLE)
# alpha = valor para poda das possibilidades do jogador
# beta = valor para poda das jogadas do oponente
# determineBestIn = funcao que determine melhor jogada para o jogador em uma lista (min ou max)
# determineWorstIn = funcao que determine melhor jogada para o oponente em uma lista (min ou max)
#
def search(state, myTurn, opponentTurn, alpha, beta, determineBestIn, determineWorstIn, depth):
	# fim da recursao caso nao hajam mais jogadas possiveis
	if state.plays == 9 or state.value != NONE:
		#print('leaf')	#debug
		return (state.value/depth, state)
	else:	
		# cria lista com todos os estados a partir do estado atual e seus valores
		children = []
		for i in range(3):
			for j in range(3):
				if state.game[i][j] == NONE:
					possibility = deepcopy(state)
					possibility.play(myTurn, i, j)
					
					# procura melhor movimento do oponente a partir do estado atual e adiciona a lista
					opponentPlay = search(possibility, opponentTurn, myTurn, beta, alpha, determineWorstIn, determineBestIn, depth+1)
					children.append((opponentPlay[0], possibility))
					
					# se melhor movimento do oponente eh melhor do que o encontrado em outro caminho faz poda
					if determineBestIn(opponentPlay[0], beta) == opponentPlay[0]:
						return determineBestIn(children, key=lambda state: state[0])
					
					# atualiza melhor mavimento caso necessario
					alpha = determineBestIn(opponentPlay[0], alpha)
		
		# retorna melhor jogada possivel
		play = determineBestIn(children, key=lambda state: state[0])
		
		#play.printSelf()	#debug
		#print(play.lineCount)	#debug
		#print(play.columCount)	#debug
		#print(play.firstDiagonalCount, play.secondDiagonalCount)	#debug
		#print(play.value)	#debug
		
		return play
					

class Max:
	def __init__(self, plays):
		self.turn = plays
	
	def play(self, state):
		print('\033[1;30mMax escolhendo jogada...', end='\n\n')
		# faz busca com alpha sendo a pior jogada possivel e beta sendo a melhor jogada possivel de maneira que nao haja poda antes do primeiro no folha ser alcancado
		play = search(state, self.turn, -self.turn, -self.turn, self.turn, max, min, 0)
		return play[1]
		
class Min:
	def __init__(self, plays):
		self.turn = plays
		
	def play(self, state):
		print('\033[1;30mMin escolhendo jogada...', end='\n\n')
		# faz busca com alpha sendo a pior jogada possivel e beta sendo a melhor jogada possivel de maneira que nao haja poda antes do primeiro no folha ser alcancado
		play = search(state, self.turn, -self.turn, -self.turn, self.turn, min, max, 0)
		return play[1]
		
