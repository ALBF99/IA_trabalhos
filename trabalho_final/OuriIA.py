import copy
from OuriBoard import *

class Ia:

	def heuristic(self, board):
		if board.player_turn == IA:
			return board.score1 - board.score2

		else:
			return board.score2 - board.score1

	def maximizer(self,board,depth):
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = -999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
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
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = 999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
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

		moves = board.possible_moves()

		for move in moves:
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = IA
			board_copy.make_move(move)

			if board_copy.opponent_empty():
				val = self.maximizer(board_copy, depth-1)
			else:
				val = self.minimizer(board_copy,depth-1) 
				
			if val > value:
				m = move
				value = val

		if len(moves) == 1:
			return move

		return m

	def maximizerAB(self,board,depth, alpha, beta):
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = -999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = IA_2
			board_copy.make_move(move)

			if board_copy.opponent_empty():
				val = self.maximizerAB(board_copy, depth-1, alpha, beta)
			else:
				val = self.minimizerAB(board_copy,depth-1, alpha, beta) 

			value = max(value, val)
			#print(value)
			if value >= beta:
				return value

			alpha = max(alpha, value)
			
		return value

	def minimizerAB(self, board,depth, alpha, beta):
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = 999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = IA
			board_copy.make_move(move)

			if board_copy.opponent_empty():
				val = self.minimizerAB(board_copy,depth-1, alpha, beta)
			else:
				val = self.maximizerAB(board_copy,depth-1, alpha, beta) 

			value = min(value, val)
		
			if value <= alpha:
				return value

			beta = min(beta, value)
		
		return value

	def alphaBeta(self,board,depth):
		m = -1
		value = -999
		alpha = -999
		beta = 999

		if depth == 0:
			return self.heuristic(board)

		if board.game_over():
			return -1

		moves = board.possible_moves()

		for move in moves:
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = IA_2
			board_copy.make_move(move)

			if board_copy.opponent_empty():
				val = self.maximizerAB(board_copy, depth-1, alpha, beta)
			else:
				val = self.minimizerAB(board_copy,depth-1, alpha, beta) 

			if val > value:
				m = move
				value = val

			alpha = max(value, alpha)
		

		if len(moves) == 1:
			return move

		return m