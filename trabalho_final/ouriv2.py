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

	def get_score(self):
		return self.board[1][0]

	def get_score_opponent(self):
		return self.board[1][1]

	def reverse_lists(self):
		self.board[0] = list(reversed(self.board[0]))
		self.board[1] = list(reversed(self.board[1]))


	def opponent_empty(self):
		if sum(self.board[0][6:]) > 0:
			return False
		return True


	def possible_moves(self):
		moves = list()

		if self.opponent_empty():
			for idx in range(6):
				seeds = self.board[0][idx]

				if idx+1+seeds > 6:
					moves.append(idx+1)

		else:
			for idx in range(6):
				seeds = self.board[0][idx]

				if seeds > 0:
					moves.append(idx+1)

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

	def valid_move(self,pit):
		if pit > 6 and self.board[0][pit-1] == 0:
			return False
		return True

	def game_over(self):
		return self.get_score() + self.get_score_opponent() == 48


class Computer:
	def __init__(self):
		self.player = COMPUTER
		

	def heuristic(self, board):
		return board.get_score() - board.get_score_opponent()


	def minimax(self, depth, maximizer=False):
		value = 0

		if depth == 0 or board.game_over():
			return self.heuristic(board)

		if maximizer:
			value = -120
			board_copy = Board(board)
			moves = board.possible_moves()

			for move in moves:
				val = self.minimax(depth-1, not maximizer)
				value = max(value, val)

		else:
			value = 120
			board_copy = Board(board)
			moves = board.possible_moves()

			for move in moves:
				val = self.minimax(depth-1, not maximizer) #maximizer/not maximizer ??
				value = min(value, val)

		return value




def menu():
	print("		     WELCOME TO OURI GAME\n\n")
	#RULES


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


			moves = game.possible_moves()

			#no moves left
			if not moves:
				game.retrive_seeds()
			else:
				pit = input("->Player move: ")

				while int(pit) not in moves:
					pit = input("->Player move:")


				last_pit = game.make_move(int(pit))

				if last_pit > 5:
					game.capture(last_pit)
				

			game.reverse_lists()


def main():
	menu()

	play_game()

if __name__=='__main__':
        main()