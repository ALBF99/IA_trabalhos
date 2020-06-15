import copy
import argparse

PLAYER = 'J'
COMPUTER = 'C' 
N_PITS = 12

class Board:
	def __init__(self, player):
		self.board = [[4,4,4,4,4,4,4,4,4,4,4,4],[0,0]]
		self.player_turn = player #we decide who starts
		#self.winner

	#def __str__(self, *args, **kwargs):
	#	return str(self.board)
	
	#def __repr__(self, *args, **kwargs):
	#	return "Board%s" % self.__str__()

	#refazer função
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

		for idx in range(6):
			if self.valid_move(idx, self.opponent_empty()):
				moves.append(idx)

		print("possible",moves)
		return moves


	def make_move(self,pit):
		seeds = self.board[0][pit]
		self.board[0][pit] = 0
		idx = pit+1

		while True:
			self.board[0][idx] += 1
			seeds -= 1

			if seeds == 0:
				break;

			idx += 1
			idx %= N_PITS

		if idx > 5:
			self.capture(idx)


	def capture(self,pit):
		count_seeds = 0

		while self.board[0][pit] == 2 or self.board[0][pit] == 3 and pit > 5:
			count_seeds += self.board[0][pit]
			self.board[0][pit] = 0
			pit -= 1

		self.board[1][0] += count_seeds


	def valid_move(self,pit, no_seeds_opponent):
		#if pit has seeds
		#if pit is between 0 and 5
		#you can only choose a pit with one seed, if you don't have any other pit with more
		pit_seeds = self.board[0][pit]
		if pit_seeds == 0:
			return False

		elif pit_seeds == 1 and not all(i > 1 for i in self.board[0]):
			return False

		elif no_seeds_opponent and pit + pit_seeds < 5:
			return False

		else:
			return True


	def game_over(self):
		if self.get_score() >= 25 or self.get_score_opponent() >= 25:
			return True

		#empate
		elif self.get_score == 24 and self.get_score_opponent() == 24:
			return True

		else:
			return False
		
		


class Computer:
	def __init__(self):
		self.player = COMPUTER

	def heuristic(self, board):
		return (board.get_score() - board.get_score_opponent())


	def minimax(self, depth, board, maximizer=False, sequence=[]):
		if depth == 0 or board.game_over():
			print(board.game_over())
			return self.heuristic(board), sequence

		if maximizer:
			value = -999
			best_sequence = []
			board_copy = copy.deepcopy(board)
			print("ia")
			moves = board_copy.possible_moves()

			for move in moves:

				if board_copy.opponent_empty():
					maximizer = False

				board_copy.make_move(move)

				val, seq = self.minimax(depth-1,board_copy, not maximizer, sequence + [move])
				value = max(value, val)
				best_sequence = seq
			print("best_sequence",best_sequence)
			return value, best_sequence

		else:
			value = 999
			best_sequence = []
			board_copy = copy.deepcopy(board)
			board_copy.reverse_lists()
			print("player")
			moves = board_copy.possible_moves()
			board_copy.reverse_lists()
			
			for move in moves:

				if board_copy.opponent_empty():
					maximizer = True

				board_copy.make_move(move)
				val, seq = self.minimax(depth-1,board_copy, not maximizer, sequence + [move])
				value = min(value, val)
				best_sequence = seq
			print("best_sequence",best_sequence)
			return value, best_sequence


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

			if board.opponent_empty():
				score,sequence = computer.minimax(4,board,True)
			score, sequence = computer.minimax(4,board)
			print(sequence)
			

			board.make_move(sequence[0]) #??

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

				board.make_move(int(pit)-1)
				

			board.reverse_lists()
			board.player_turn = COMPUTER


def main():
	menu()

	play_game()

if __name__=='__main__':
       	#A resolver
        #parser = argparse.ArgumentParser(description='Ouri')
        #parser.add_argument('-p', default=PLAYER)
        #parser.add_argument('-s', default=COMPUTER)
        #args = parser.parse_args()

        #play_game(args.player_turn)

        main()