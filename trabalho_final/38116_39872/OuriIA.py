import copy
from OuriBoard import *
from Ouri import *

class IA:
	def __init__(self, depth):
		self.depth = depth

	#Heuristic function: Difference between scores
	def heuristic(self, board):
		if board.player_turn == board.player1:
			return board.score1 - board.score2

		else:
			return board.score2 - board.score1


	def maximizer(self,board,depth, player):
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = -999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = player
			board_copy.make_move(move)

			#if next player doesn't have seeds, the current player plays again
			if board_copy.opponent_empty():
				val = self.maximizer(board_copy, depth-1, MINIMAX)
			else:
				val = self.minimizer(board_copy,depth-1, board_copy.get_opponent(MINIMAX)) 
			
			value = max(val,value)

		return value


	def minimizer(self, board,depth, player):
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = 999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = player
			board_copy.make_move(move)

			#if next player doesn't have seeds, the current player plays again
			if board_copy.opponent_empty():
				val = self.minimizer(board_copy,depth-1, player)
			else:
				val = self.maximizer(board_copy,depth-1, MINIMAX) 
			
			value = min(val,value)

		return value


	def minimax(self, board, depth, player):
		best_move = -1
		value = -999

		if depth == 0:
			return self.heuristic(board)

		if board.game_over():
			return -1

		moves = board.possible_moves()

		for move in moves:
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = player
			board_copy.make_move(move)

			#if next player doesn't have seeds, the current player plays again
			if board_copy.opponent_empty():
				val = self.maximizer(board_copy, depth-1, MINIMAX)
			else:
				val = self.minimizer(board_copy,depth-1, board_copy.get_opponent(MINIMAX)) 
				
			if val > value:
				best_move = move
				value = val

		if len(moves) == 1:
			return move

		return best_move


	def maximizerAB(self,board,depth, alpha, beta, player):
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = -999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = player
			board_copy.make_move(move)

			#if next player doesn't have seeds, the current player plays again
			if board_copy.opponent_empty():
				val = self.maximizerAB(board_copy, depth-1, alpha, beta, ALPHABETA)
			else:
				val = self.minimizerAB(board_copy,depth-1, alpha, beta, board_copy.get_opponent(ALPHABETA)) 

			value = max(value, val)
			
			if value >= beta:
				return value

			alpha = max(alpha, value)
			
		return value

	def minimizerAB(self, board,depth, alpha, beta, player):
		if depth == 0 or board.game_over():
			return self.heuristic(board)

		value = 999
		
		for move in board.possible_moves():
			board_copy = copy.deepcopy(board) # new child node
			board_copy.player_turn = player
			board_copy.make_move(move)

			#if next player doesn't have seeds, the current player plays again
			if board_copy.opponent_empty():
				val = self.minimizerAB(board_copy,depth-1, alpha, beta, player)
			else:
				val = self.maximizerAB(board_copy,depth-1, alpha, beta, ALPHABETA) 

			value = min(value, val)
			
			if value <= alpha:
				return value

			beta = min(beta, value)
		
		return value

	def alphaBeta(self,board,depth, player):
		best_move = -1
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
			board_copy.player_turn = player
			board_copy.make_move(move)
			
			#if next player doesn't have seeds, the current player plays again
			if board_copy.opponent_empty():
				val = self.maximizerAB(board_copy, depth-1, alpha, beta, ALPHABETA)
			else:
				val = self.minimizerAB(board_copy,depth-1, alpha, beta, board_copy.get_opponent(ALPHABETA)) 

			if val > value:
				best_move = move
				value = val

			alpha = max(value, alpha)
		
		if len(moves) == 1:
			return move

		return best_move