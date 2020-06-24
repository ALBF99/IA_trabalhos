from Ouri import *
from OuriIA import *


class Board:
	def __init__(self, player1, player2, player_turn, winner=None):
		self.row1 = [4,4,4,4,4,4]
		self.row2 = [4,4,4,4,4,4]
		self.score1 = 0
		self.score2 = 0
		self.player1 = player1
		self.player2 = player2
		self.player_turn = player_turn 
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


	def get_opponent(self, player):
		if self.player1 == player:
			return self.player2

		return self.player1


	#check if the opponent don't have seeds to move
	def opponent_empty(self):
		if self.player_turn == self.player1:
			return sum(self.row2) == 0
		else:
			return sum(self.row1) == 0


	def valid_move(self, pit, no_seeds_opponent):
		#if pit has seeds
		#if pit is between 0 and 5
		#you can only choose a pit with one seed if you don't have any other pit with more

		if self.player_turn == self.player1:
			row = self.row1
		else:
			row = self.row2

		pit_seeds = row[pit]

		if pit_seeds == 0:
			return False

		elif not no_seeds_opponent and pit_seeds == 1 and not all(i <= 1 for i in row):
			return False

		elif no_seeds_opponent and pit + pit_seeds < 6:
			return False

		else:
			return True


	#Legal moves the player can do 
	def possible_moves(self):
		moves = list()

		for pit in range(6):
			if self.valid_move(pit, self.opponent_empty()):
				moves.append(pit)
		
		return moves


	def switch_rows(self, row, opponent_row):
		if row == self.row1:
			side = self.player2
		else:
			side = self.player1

		return opponent_row, row, side


	#Move seeds across the board
	def make_move(self, pit):
		if self.player_turn == self.player1:
			row = self.row1
			opponent_row = self.row2
			side = self.player1
		else:
			row = self.row2
			opponent_row = self.row1
			side = self.player2

		seeds = row[pit]
		row[pit] = 0
		jump = pit
		pit += 1

		while seeds > 0:
			if side == self.player_turn and pit == jump:
				pit += 1

			if pit == 6:
				row, opponent_row, side = self.switch_rows(row, opponent_row)
				pit = 0

			else:
				row[pit] += 1
				seeds -= 1
				pit += 1
		
		#check if the last seed was put in the opponent side
		if side != self.player_turn:
			self.capture(pit-1, row)


	def capture(self, pit, row):
		count_seeds = 0
		
		while pit >= 0 and (row[pit] == 2 or row[pit] == 3):
			count_seeds += row[pit]
			row[pit] = 0
			pit -= 1
			
		if self.player_turn == self.player1:
			self.score1 += count_seeds
		else:
			self.score2 += count_seeds


	#check if the game ended
	def game_over(self):
		if self.no_more_moves():
			self.collect_seeds()

		if self.score1 >= 25:
			self.winner = self.player1 + " won!"
			return True

		elif self.score2 >= 25:
			self.winner = self.player2 + " won!"
			return True

		elif self.score1 == 24 and self.score2 == 24:
			self.winner = "Tie!"
			return True

		else:
			return False

	#the game is near the end when
	#Case 1: we can't put seeds in the opponent side (that is empty)
	#Case 2: we detect a cycle
	def no_more_moves(self):
		if not self.possible_moves() and self.opponent_empty():
			return True

		if self.detect_cycle():
			return True

		return False

	#Case 1
	def collect_seeds(self):

		for seeds1 in self.row1:
			self.score1 += seeds1
			self.row1 = [0,0,0,0,0,0]

		for seeds2 in self.row2:
			self.score2 += seeds2
			self.row2 = [0,0,0,0,0,0]

	#Case 2
	def detect_cycle(self):
		if sum(self.row1) == 1 and sum(self.row2) == 1 and self.row1 == self.row2:
			return True

		return False
