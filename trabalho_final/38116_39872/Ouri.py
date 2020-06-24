import time
import argparse
from OuriIA import *
from OuriBoard import *

#players
MINIMAX = "Minimax"
ALPHABETA = "Alphabeta"
PLAYER = "Player"

#levels of analysis and correspondent search depth
MINIMAX_5 = 7
MINIMAX_15 = 9
MINIMAX_30 = 10
ALPHABETA_5 = 11
ALPHABETA_15 = 13
ALPHABETA_30 = 15


def match_level(algorithm, level):
	if algorithm == MINIMAX:
		if level == 1:
			return MINIMAX_5
		elif level == 2:
			return MINIMAX_15
		else:
			return MINIMAX_30
	else:
		if level == 1:
			return ALPHABETA_5
		elif level == 2:
			return ALPHABETA_15
		else:
			return ALPHABETA_30


def switch_turns(board):
	board.player_turn = board.get_opponent(board.player_turn)
		

def menu(t):
	print("\n		     WELCOME TO OURI GAME\n\n")


	print("Choose a GAME MODE:")
	print(" 1- player vs ia")
	print(" 2- ia vs ia")

	mode = input("Option:")

	if mode == str(1):
		print("\nChoose the ALGORITHM you want to play against:")
		print(" 1- Minimax")
		print(" 2- Alphabeta")

		algo = input("Option:")

		if algo == str(1):
			algo = MINIMAX
		else:
			algo = ALPHABETA

	print("\nChoose the LEVEL OF ANALYSIS of the algorithm:")
	print(" 1- 5 seconds")
	print(" 2- 15 seconds")
	print(" 3- 30 seconds")

	level = input("Option:")

	if mode == str(1):
		player_vs_ia(t, algo, int(level))
	else:
		ia_vs_ia(t, int(level))


def ia_vs_ia(t, level):
	if t == 1:
		board = Board(MINIMAX, ALPHABETA, MINIMAX)
	else:
		board = Board(MINIMAX, ALPHABETA, ALPHABETA)


	ia = IA(match_level(MINIMAX, level)) #minimax
	ia2 = IA(match_level(ALPHABETA, level)) #alphabeta

	while True:
		board.display_board()

		if board.game_over():
			print("\n-------------------------------END-------------------------------")
			board.display_board()
			print(board.winner)
			break

		if board.player_turn == MINIMAX:
			print("Minimax turn")

			start_time = time.time()
			move = ia.minimax(board, ia.depth, MINIMAX)
			print("--- %s seconds ---" % round(time.time() - start_time))

			if move != -1:
				print("Best move: ", 6-move, "\n")
				board.make_move(move)

				if not board.opponent_empty():
					switch_turns(board)

		else:
			print("Alphabeta turn")

			start_time = time.time()
			move = ia2.alphaBeta(board, ia2.depth, ALPHABETA)
			print("--- %s seconds ---" % round(time.time() - start_time))

			if move != -1:
				print("Best move: ", 6-move, "\n")
				board.make_move(move)

				if not board.opponent_empty():
					switch_turns(board)


def player_vs_ia(t, algo, level):
	if t == 1:
		board = Board(algo, PLAYER, algo)
	else:
		board = Board(algo, PLAYER, PLAYER)

	ia = IA(match_level(algo, level)) #minimax or alphabeta

	while True:
		board.display_board()

		if board.game_over():
			print("\n-------------------------------END-------------------------------")
			board.display_board()
			print(board.winner)
			break


		if board.player_turn == PLAYER:
			moves = board.possible_moves()

			if moves:

				pit = input("->Player move: ")

				while int(pit)-1 not in moves:
					print("Invalid move!")
					pit = input("->Player move:")

				board.make_move(int(pit)-1)
			
			if not board.opponent_empty():
				switch_turns(board)

		else:

			print("Computer turn...")
			start_time = time.time()

			if board.player_turn == MINIMAX:
				move = ia.minimax(board, ia.depth, MINIMAX)

			if board.player_turn == ALPHABETA:
				move = ia.alphaBeta(board, ia.depth, ALPHABETA)

			print("--- %s seconds ---" % round(time.time() - start_time))
			
			if move != -1:
				print("Best move: ", 6-move, "\n")
				board.make_move(move)

				if not board.opponent_empty():
					switch_turns(board)
					


if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Ouri')
	parser.add_argument('-p', help="Computer plays first", action="store_true")
	parser.add_argument('-s', help="Player plays first", action="store_false")
	args = parser.parse_args()

	#program starts first
	if args.p == True:
		menu(1)
	else:
		menu(2)
