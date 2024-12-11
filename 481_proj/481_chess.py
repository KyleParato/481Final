import chess
import time
from chess_ai import *

#stagnant board for kings pawn opening
def kings_pawn_opening_setup(board):
	board.push_san('e4')
	board.push_san('e5')
	board.push_san('Nf3')
	board.push_san('Nc6')
	board.push_san('Nc3')
	board.push_san('Nf6')
	board.push_san('Bc4')
	board.push_san('Bc5')
	board.push_san('O-O')
	board.push_san('O-O')
	board.push_san('d3')
	board.push_san('d6')
	board.push_san('Bg5')
	board.push_san('Bg4')
	board.push_san('h3')
	board.push_san('Bh5')
	board.push_san('b3')
	board.push_san('h6')
	board.push_san('Bh4')
	board.push_san('b6')
	board.push_san('a4')
	board.push_san('a5')
	#print(board.legal_moves)

def print_board_replace(board):
	for i in range(0,8):
		print("\033[A", end="")
	print(board)

def play_game(board, d1, d2):
	board = board.board
	p1 = chess_ai()
	p2 = chess_ai()
	turn = True
	w_last_move = None
	b_last_move = None
	move_count = 1
	print(board)
	while(board.is_stalemate() != True) and (board.is_checkmate() != True):
		if turn:
			p1.board = board
			move = p1.alpha_beta_search_no_print(depth=d1, last_move=w_last_move)
			board.push(move)
			# print(w_last_move)
			# print(move)
			# w_last_move = str(move)
			# w_last_move = w_last_move[2:] + w_last_move[:2]
			turn = False
			print_board_replace(board)
			#print("Turn: " + str(move_count))
			move_count += 1
		else:
			p2.board = board
			move = p2.alpha_beta_search_no_print(depth=d2)
			# print(b_last_move)
			# print(move)
			board.push(move)
			# b_last_move = str(move)
			# b_last_move = b_last_move[2:] + b_last_move[:2]
			turn = True
			print_board_replace(board)
			#print("Turn: " + str(move_count))
			move_count += 1
	return turn

if __name__ == '__main__':

	#create the chess board
	# print("Test board\n")
	# board = chess.Board()
	# kings_pawn_opening_setup(board)
	# print(board)

	#use the A* search algorithm for winning pieces condition

	c_ai = chess_ai()
	
	# kings_pawn_opening_setup(c_ai.board)

	# # print("\nOriginal Board")
	# # print(c_ai.board)

	# for d in range(1,6):
	# 	print("\nBest Move depth " + str(d) + "\n")
	# 	start = time.time()
	# 	print(f"\nBest move: " + str(c_ai.alpha_beta_search(depth=d)))
	# 	end = time.time()
	# 	print(f"Elapsed time: {(end-start):.2f} seconds")

	# # # print()
	# Play Game
	# time.sleep(5)

	print("\nPlay Game depth 2 vs depth 4\n")
	c_ai.board.reset
	play_game(board=c_ai, d1=2,d2=4)
