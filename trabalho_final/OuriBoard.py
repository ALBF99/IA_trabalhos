from OuriIA import *

IA = 1
IA_2 = 2
PLAYER = 2


class Board:
	def __init__(self, player_turn=2):
		self.row1 = [2,2,2,2,2,2]
		self.row2 = [4,4,4,4,4,4]
		self.score1 = 0
		self.score2 = 0
		self.player_turn = player_turn #1- ia; 2-human or ia 

	def display_board(self):
		str1 = "            1       2       3       4       5       6"
		str2 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
		str3 = "|       |       |       |       |       |       |       |       |"
		str4 = "|_______|_______|_______|_______|_______|_______|"
		str5 = "|       "
		str6 = "|       |"

		print(str1)
		print(str2)
		print(str3)
		print(str5, end='')

		self.print_pits_board(self.row1)

		print(str6)


		self.print_score_board(self.score1,True)

		print(str4,end='')

		self.print_score_board(self.score2,False)

		print(str3)
		print(str5, end='')
		list(reversed(self.row2))
		self.print_pits_board(self.row2)
		list(reversed(self.row2))

		print(str6)
		print(str3)
		print(str2)


	def print_pits_board(self,row):
		for pit in row:
			if pit > 9:
				print("|   "+str(pit)+"  ", end='')
			else:
				print("|   "+str(pit)+"   ", end='')


	def print_score_board(self,score, left):
		if score > 9:
			if left:
				print("|   "+str(score)+"  ", end='')
			else:
				print("   "+str(score)+"  |")
		else:
			if left:
				print("|   "+str(score)+"   ", end='')
			else:
				print("   "+str(score)+"   |")


	def opponent_empty(self):
		if self.player_turn == IA:
			return sum(self.row2) == 0
		else:
			return sum(self.row1) == 0


	def valid_move(self, pit, no_seeds_opponent):
		#if pit has seeds
		#if pit is between 0 and 5
		#you can only choose a pit with one seed, if you don't have any other pit with more
		if self.player_turn == IA:
			row = self.row1
		else:
			row = self.row2

		pit_seeds = row[pit]

		if pit_seeds == 0:
			return False

		elif not no_seeds_opponent and pit_seeds == 1 and not all(i <= 1 for i in row):
			return False

		elif no_seeds_opponent and pit + pit_seeds < 5:
			return False

		else:
			return True


	def possible_moves(self):
		moves = list()
		for pit in range(6):
			if self.valid_move(pit, self.opponent_empty()):
				moves.append(pit)

		return moves


	def switch_sides(self, row, opponent_row):
		if row == self.row1:
			side = PLAYER
		else:
			side = IA

		return opponent_row, row, side


	def make_move(self, pit):
		if self.player_turn == IA:
			row = self.row1
			opponent_row = self.row2
			side = IA
		else:
			row = self.row2
			opponent_row = self.row1
			side = PLAYER

		seeds = row[pit]
		row[pit] = 0
		jump = pit
		pit += 1

		while seeds > 0:
			if side == self.player_turn:
				if pit == jump:
					pit += 1

				if pit == 6:
					row, opponent_row, side = self.switch_sides(row, opponent_row)
					pit = 5

				else:
					row[pit] += 1
					seeds -= 1
					pit += 1

			else:
				if pit == -1:
					row, opponent_row, side = self.switch_sides(row, opponent_row)
					pit = 0
					
				else:
					row[pit] += 1
					seeds -= 1
					pit -= 1


		if side != self.player_turn:
			self.capture(pit+1, row)


	def capture(self, pit, row):
		count_seeds = 0
		
		while pit <= 5 and (row[pit] == 2 or row[pit] == 3):
			count_seeds += row[pit]
			row[pit] = 0
			pit += 1
			
		if self.player_turn == IA:
			self.score1 += count_seeds
		else:
			self.score2 += count_seeds


	def game_over(self):
		if self.score1 >= 25:
			return True, "IA won!"

		elif self.score2 >= 25:
			return True, "Player won!"

		elif self.score1 == 24 and self.score2 == 24:
			return True, "Tied!"

		else:
			return False

class IA:

	def heuristic(self, board):
		if board.player_turn == IA:
			return board.score1 - board.score2

		else:
			return board.score2 - board.score1

	def maximizer(self,board,depth):
		print("maxi")
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = -999
		

		for move in board.possible_moves():
			board_copy = copy.deepcopy(board)
			board_copy.player_turn = IA
			board_copy.make_move(move)

			if board_copy.opponent_empty():
				val = self.maximizer(board_copy, depth-1)
			else:
				val = self.minimizer(board_copy,depth-1) 
				
			if val > value:
				value = val
		return value

	def minimizer(self, board,depth):
		print("mini")
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = 999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board)
			board_copy.player_turn = PLAYER
			board_copy.make_move(move)

			if board_copy.opponent_empty():
				val = self.minimizer(board_copy,depth-1)
			else:
				val = self.maximizer(board_copy,depth-1) 
				
			if val < value:
				value = val
		return value

	def minimax(self, board, depth):
		m = -1
		value = -999

		if depth == 0:
			return self.heuristic(board)

		if board.game_over():
			return -1


		for move in board.possible_moves():
			board_copy = copy.deepcopy(board)
			board_copy.player_turn = IA
			board_copy.make_move(move)

			if board_copy.opponent_empty():
				val = self.maximizer(board_copy, depth-1)
			else:
				val = self.minimizer(board_copy,depth-1) 
				
			if val > value:
				m = move
				value = val
			print("minimax value",val)


		print("best move", m)
		if m == -1:
			m = move
		return m






#def menu():

def play_game(board, ia):

	while True:
		if board.player_turn == IA:


			move = ia.minimax(board,3)

			if move == -1:
				break;
			print(move)
			board.make_move(move) #??

			board.player_turn = PLAYER
			
		else:
			board.display_board()
			moves = board.possible_moves()

			if moves:
				pit = input("->Player move: ")

				while int(pit)-1 not in moves:
					pit = input("->Player move:")

				board.make_move(int(pit)-1)
				board.player_turn = IA

			if board.opponent_empty():
				board.player_turn = PLAYER

				


if __name__=='__main__':
	board = Board()
	ia = IA()
	

	play_game(board, ia)
