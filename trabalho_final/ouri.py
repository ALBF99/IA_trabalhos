PLAYER = True
OPPONENT = False
N_PITS = 12

class Board:
	def __init__(self):
		self.board = [[4,4,4,4,4,4,4,4,4,4,4,4],[0,0]]
		#self.player_turn = 'Player'

	def display_board(self):
		print("            1       2       3       4       5       6 ")
		print("+-------+-------+-------+-------+-------+-------+-------+-------+")
		print("|       |       |       |       |       |       |       |       |")
		print("|       ", end='')

		for item in self.board[0][0:6]:
			print("|   "+str(item)+"   ", end='')

		print("|       |")

		if self.board[1][0] < 9:
			print("|   "+str(self.board[1][0])+"   ", end='')
		else:
			print("|   "+str(self.board[1][0])+"  ", end='')
		print("|_______|_______|_______|_______|_______|_______|",end='')
		
		if self.board[1][1] < 9:
			print("   "+str(self.board[1][1])+"   |")
		else:
			print("   "+str(self.board[1][1])+"  |")
		print("|       |       |       |       |       |       |       |       |")
		print("|       ", end='')

		self.board[0] = list(reversed(self.board[0]))
		for item in self.board[0][0:6]:
			print("|   "+str(item)+"   ", end='')

		print("|       |")
		print("|       |       |       |       |       |       |       |       |")
		print("+-------+-------+-------+-------+-------+-------+-------+-------+")
		self.board[0] = list(reversed(self.board[0]))


	def make_move(self, pit, player):
		self.reverse_lists(player)

		#if opponent_empty():

		last_pit = self.normal_move(pit)

		if last_pit > 5:
			print(last_pit)
			self.capture(last_pit)

		self.reverse_lists(player)

		
	def reverse_lists(self,player):
		if player:
			self.board[0] = list(reversed(self.board[0]))
			self.board[1] = list(reversed(self.board[1]))


	def normal_move(self,pit):
		seeds = self.board[0][pit-1]
		self.board[0][pit-1] = 0
		idx = pit

		while True:
			self.board[0][idx] += 1
			seeds -= 1

			if seeds == 0:
				return idx

			idx += 1
			idx %= N_PITS

	#def empty_move(self):

	def capture(self,pit):
		count_seeds = 0

		while self.board[0][pit] >= 2 and pit > 5:
			count_seeds += self.board[0][pit]
			self.board[0][pit] = 0
			pit -= 1

		self.board[1][0] += count_seeds


	def opponent_empty(self):
		if sum(self.board[0][6:]) > 0:
			return False
		return True


	def game_over(self):
		if self.board[1][0] == 24 and self.board[1][0] == 24:
			return "Tied"

		elif self.board[1][0] >= 25:
			return "Computer"

		elif sel.board[1][1] >= 25:
			return "Player"


	#def best_move(self):

	#def minimax(self, )



def player_move(board):
	pit = input("->Player move: ")

	while not valid_move(int(pit)):
		pit = input("->Player move: ")

	board.make_move(int(pit),PLAYER)
	

def valid_move(pit):
	if pit > 6:
		return False
	return True

#def cicle:

def menu():
	print("		     WELCOME TO OURI GAME\n\n")
	#RULES


def main():
	menu()

	board = Board()
	board.display_board()

	while True:
		player_move(board)
		board.display_board()
	#play = True

	#while play:
		#if player_turn:

			#player_turn = False

		#else:
			#player_turn = True


if __name__=='__main__':
        main()