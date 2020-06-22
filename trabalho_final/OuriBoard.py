import copy
from OuriIA import *

IA = 1
IA_2 = 2
PLAYER = 2


class Board:
	def __init__(self, player_turn=2, winner=None):
		self.row1 = [4,4,4,4,4,4]
		self.row2 = [4,4,4,4,4,4]
		self.score1 = 0
		self.score2 = 0
		self.player_turn = player_turn #1- ia; 2-human or ia 
		self.winner = winner

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
		self.print_pits_board(list(reversed(self.row1)))
		print(str6)
		self.print_score_board(self.score1,True)
		print(str4,end='')
		self.print_score_board(self.score2,False)
		print(str3)
		print(str5, end='')
		self.print_pits_board(self.row2)
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
			if side == self.player_turn and pit == jump:
				pit += 1

			if pit == 6:
				row, opponent_row, side = self.switch_sides(row, opponent_row)
				pit = 0

			else:
				row[pit] += 1
				seeds -= 1
				pit += 1
		
		if side != self.player_turn:
			self.capture(pit-1, row)


	def capture(self, pit, row):
		count_seeds = 0
		
		while pit >= 0 and (row[pit] == 2 or row[pit] == 3):
			count_seeds += row[pit]
			row[pit] = 0
			pit -= 1
			
		if self.player_turn == IA:
			self.score1 += count_seeds
		else:
			self.score2 += count_seeds


	def game_over(self):
		if self.score1 >= 25:
			self.winner = "IA won!"
			return True

		elif self.score2 >= 25:
			self.winner = "Player won!"
			return True

		elif self.score1 == 24 and self.score2 == 24:
			self.winner = "Tie!"
			return True

		elif self.no_more_moves():
			self.retrive_seeds()
			self.winner = "No winner!"
			return True

		else:
			return False

	def no_more_moves(self):
		if not self.possible_moves() and self.opponent_empty():
			return True

		return False

	def retrive_seeds(self):

		for seeds1 in self.row1:
			self.score1 += seeds1
			self.row1 = [0,0,0,0,0,0]

		for seeds2 in self.row2:
			self.score2 += seeds2
			self.row2 = [0,0,0,0,0,0]

	#def detect_cycle(self):



def menu():
	print()
def ia_vs_ia(board, ia, ia2):

	while True:
		board.display_board()

		if board.game_over():
			print(board.winner)
			break

		if board.player_turn == IA:
			print("Minimax turn")

			move = ia.minimax(board,7)
			
			if move == -1:
				break;
			
			board.make_move(move) 

			if board.opponent_empty():
				board.player_turn = IA
			else:
				board.player_turn = IA_2

		else:
			print("Alphabeta turn")

			move = ia2.alphaBeta(board,7)

			if move == -1:
				break;
			
			board.make_move(move) 

			if board.opponent_empty():
				board.player_turn = IA_2
			else:
				board.player_turn = IA



def player_vs_ia(board, ia):
	
	while True:
		board.display_board()

		if board.game_over():
			print(board.winner)
			break

		if board.player_turn == IA:
			print("IA turn")

			move = ia.minimax(board,11)
			
			if move == -1:
				break;
			
			board.make_move(move) 

			if board.opponent_empty():
				board.player_turn = IA
			else:
				board.player_turn = PLAYER
			
		else:
			moves = board.possible_moves()

			if moves:
				pit = input("->Player move: ")

				while int(pit)-1 not in moves:
					pit = input("->Player move:")

				board.make_move(int(pit)-1)
		
			if board.opponent_empty():
				board.player_turn = PLAYER
			else:
				board.player_turn = IA

				


if __name__=='__main__':
	board = Board()
	ia = Ia()
	ia2 = Ia()
	
	#player_vs_ia(board, ia)
	ia_vs_ia(board, ia, ia2)
