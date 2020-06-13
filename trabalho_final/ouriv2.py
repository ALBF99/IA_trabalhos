PLAYER = 'J'
COMPUTER = 'C' 
N_PITS = 12


class Game:
	def __init__(self, player):
		self.board = [[4,4,4,4,4,4,4,4,4,4,4,4],[0,0]]
		self.player_turn = player #we decide who starts
		#self.winner

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

	def reverse_lists(self):
		self.board[0] = list(reversed(self.board[0]))
		self.board[1] = list(reversed(self.board[1]))


	def opponent_empty(self):
		if sum(self.board[0][6:]) > 0:
			return False
		return True


	def possible_moves(self):
		moves = list()

		for idx in range(6):
			seeds = self.board[0][idx]

			if idx+1+seeds > 6:
				moves.append(idx+1)

		if not moves:
			return None
		else:
			return moves


	def make_move(self,pit):
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


	def capture(self,pit):
		count_seeds = 0

		while self.board[0][pit] >= 2 and pit > 5:
			count_seeds += self.board[0][pit]
			self.board[0][pit] = 0
			pit -= 1

		self.board[1][0] += count_seeds




class Computer:
	def __init__(self):
		self.player = COMPUTER







def menu():
	print("		     WELCOME TO OURI GAME\n\n")
	#RULES

def valid_move(pit):
	if pit > 6:
		return False
	return True

def play_game():
	game = Game(PLAYER)
	computer = Computer()

	while True:
		game.display_board()
		#check if chegou ao fim/ alguem ganhou

		#computer turn
		if game.player_turn == computer.player:
			print(winner)
		#player turn
		else:
			game.reverse_lists()

			#opponet don't have any seeds
			if game.opponent_empty():
				moves = game.possible_moves()

				#no moves left
				if moves == None:
					game.retrive_seeds()

				else:
					pit = input("->Player move: ")

					#making sure the player's move puts seeds in the opponent side
					while int(pit) not in moves:
						pit = input("->Player move:")

					game.make_move(int(pit))

			#normal move
			else:
				pit = input("->Player move: ")

				while not valid_move(int(pit)):
					pit = input("->Player move: ")

				last_pit = game.make_move(int(pit))

				if last_pit > 5:
					game.capture(last_pit)
				

			game.reverse_lists()


def main():
	menu()

	play_game()

if __name__=='__main__':
        main()