from state import TicTacToe, NONE, CROSS, CIRCLE
from minmax import Max, Min
import sys

#
# Program call: python3 main.py <first player> <second player>
#	Players can be either 'player' or 'cpu'
#

class Player:
	def __init__(self, plays):
		self.turn = plays
		
	def play(self, state):
		square = int(input('\033[1;30mSelecione numero onde deseja jogar: '))
		i = square//3
		j = square%3
		while state.game[i][j] != NONE:
			square = int(input('\033[1;30mNumero ja usado, selecione outro: '))
			i = square//3
			j = square%3
			
		print(end='\n')
		state.play(self.turn, i, j)
		return state
		
def main(player1, player2):
	game = TicTacToe()
	players = [player1, player2]
	turn = 0
	game.printSelf()
	print(end='\n')
	while game.plays < 9 and game.value == NONE:
		game = players[turn].play(game)
		game.printSelf()
		print(end='\n')
		turn = (turn+1)%2
		
	if game.value == NONE:
		print('\033[1;30mJogo empatado')
	elif game.value == CROSS:
		print('\033[1;37mJogador 1 ganhou')
	else:
		print('\033[0;31mJogador 2 ganhou')	

player1 = Max(CROSS) if sys.argv[1] == 'cpu' else Player(CROSS)
player2 = Min(CIRCLE) if sys.argv[2] == 'cpu' else Player(CIRCLE)
	
main(player1, player2)
