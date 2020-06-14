PLAYER = 'J'
COMPUTER = 'C' 
N_PITS = 12

class Board:
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

				if idx+seeds > 5:
					moves.append(idx)

		else:
			for idx in range(6):
				seeds = self.board[0][idx]

				if seeds > 0:
					moves.append(idx)

		return moves


	def make_move(self,pit):
		print("aqui")
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


	def minimax(self, depth, board, maximizer=False, sequence=[]):
		#value = 0

		if depth == 0:
			return self.heuristic(board), sequence

		if maximizer:
			value = -999
			best_sequence = []
			board_copy = Board(board)
			moves = board_copy.possible_moves()

			for move in moves:
				val, seq = self.minimax(depth-1,board_copy, not maximizer, sequence + [move])
				print(val)
				value = max(value, val)
				best_sequence = seq

			#print(value,best_sequence)
			return value, best_sequence

		else:
			value = 999
			best_sequence = []
			board_copy = Board(board)

			board_copy.reverse_lists()
			moves = board_copy.possible_moves()
			board_copy.reverse_lists()

			for move in moves:
				val, seq = self.minimax(depth-1,board_copy, not maximizer, sequence + [move])
				print(val)
				value = min(value, val)
				best_sequence = seq
			
			#print(value,best_sequence)
			return value, best_sequence


	def best_move(self, board, moves):
		for move in moves:
			board_copy = Board(board)
			moves = board_copy.possible_moves()

			if not moves:
				board.retrive_seeds()
				return 

			value = max(value)


		





def menu():
	print("		     WELCOME TO OURI GAME\n\n")
	#RULES


def play_game():
	board = Board(PLAYER)
	computer = Computer()

	while True:
		board.display_board()
		#check if chegou ao fim/ alguem ganhou

		#computer turn
		if board.player_turn == computer.player:
			print("IA turn")
			score, sequence = computer.minimax(2,board)
			print(sequence)
			for move in sequence:
				print("aqui ",move)

			last_pit = board.make_move(move+1)

			if last_pit > 5:
				board.capture(last_pit)

			board.player_turn = PLAYER

		#player turn
		else:
			board.reverse_lists()


			moves = board.possible_moves()

			#no moves left
			if not moves:
				board.retrive_seeds()
			else:
				pit = input("->Player move: ")

				while int(pit)-1 not in moves:
					pit = input("->Player move:")


				last_pit = board.make_move(int(pit))

				if last_pit > 5:
					board.capture(last_pit)
				

			board.reverse_lists()
			board.player_turn = COMPUTER


def main():
	menu()

	play_game()

if __name__=='__main__':
        main()