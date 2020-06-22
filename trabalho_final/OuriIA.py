import copy
from OuriBoard import *

class IA:
	def __init__(self, depth=4):
		self.depth = depth

	def minimax(self, board, maximizer=False):
		if depth == 0 or board.gameOver():
			return

		if maximizer:
			value = -999999
			board_copy = copy.deepcopy(board)

			for move in board_copy.possible_moves():
				board_copy.make_move(move)

				val = self.minimax(board_copy,depth-1, not maximizer) 

				if val > value:
					value = val
			return value

		else:
			value = 999
			board_copy = copy.deepcopy(board)

			for move in board_copy.possible_moves():

				board_copy.make_move(move)

				val = self.minimax(board_copy,depth-1, not maximizer) 

				if val < value:
					value = val

			return value


