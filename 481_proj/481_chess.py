import chess
import time
from chess_ai import *

# stagnant board for kings pawn opening
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

# replace current printed board
def print_board_replace(board):
	for i in range(0,8):
		print("\033[A", end="")
	print(board)

# example search from depth one to desired depth
def find_next_best_move_example(ai, depth):
	# show original board
	print("\nOriginal Board")
	print(c_ai.board)
	# loop through depth, tracking time
	for d in range(1,depth+1):
		print("\nBest Move depth " + str(d) + "\n")
		start = time.time()
		print(f"\nBest move: " + str(c_ai.alpha_beta_search(depth=d)))
		end = time.time()
		print(f"Elapsed time: {(end-start):.2f} seconds")
	print() #nl for spacing

# play game with two alpha beta search 
def play_game(board, d1, d2):
	p1 = chess_ai() # chess ai object
	turn = True 	# turn tracker, true is white, false is black
	move_count = 1	# track number of moves

	last_6 = [] # tracks last 6 turns, 12 moves total for stalemate condtions

	# stalemate condtions, if there are 4 repeat moves in a set of 12, the ai is at a stalemate
	def check_stalemate(move):
		repeat = 0 # how many repeat moves
		if len(last_6) != 12:
			last_6.append(move)
		else:
			last_6.pop(0)
			last_6.append(move)
			for i in range(0,12):
				for ii in range(i+1,12):
					if last_6[i] == last_6[ii]:
						if repeat > 4:
							return True
						else:
							repeat += 1
		return False

	# start of game loop
	print(board) # inital print 
	while(board.is_stalemate() != True) and (board.is_checkmate() != True): # break loop if normal stalemate or checkmate
		if turn: # white turn
			p1.board = board # set ai board to current game board
			move = p1.alpha_beta_search_no_print(depth=d1) # search for next best move
			board.push(move) # make best move
			if check_stalemate(move=move): # break loop if stuck
				break
			turn = False # set turn to black
			print_board_replace(board) # show move
			move_count += 1	
		else: # black turn
			p1.board = board # set ai board to current game board
			move = p1.alpha_beta_search_no_print(depth=d2) # search for next best move
			board.push(move) # make best move
			if check_stalemate(move=move): # break loop if stuck
				break
			turn = True # set turn to white
			print_board_replace(board) # show move
			move_count += 1

	utility_score = p1.current_utility_score(p1.board)
	print(f'Utility Score: {utility_score}')
	print(f'Number of moves: {move_count}')
	if board.is_checkmate():
		print("Game ended in a checkmate")
	else:
		print("Game ended in a stalemate")
	if utility_score > 0:
		return True
	elif utility_score < 0:
		return False
	else:
		return None

if __name__ == '__main__':

	# create the chess ai 
	c_ai = chess_ai()

	# set up kings pawn opening
	kings_pawn_opening_setup(c_ai.board)

	# find next best move for kings pawn opening
	find_next_best_move_example(c_ai, depth=4) # raising value above 5 will lead to slow compuation times
	

	# Play Game

	number_of_games = 3

	white_depth = 2 # depth limit for white

	black_depth = 4 # depth limit for black

	white_wins = 0
	black_wins = 0

	for i in range(0,number_of_games):
		c_ai = chess_ai() # reliably reset board
		print(f'\nGame {i+1}')
		end_state = play_game(board=c_ai.board, d1=white_depth,d2=black_depth)
		if end_state == True:
			print("White higher utility score")
			white_wins += 1
		elif end_state == False:
			print("Black higher utility score")
			black_wins += 1
		else:
			print('Tie')

	print()
	print(f'White won {white_wins} with a depth of {white_depth}')
	print(f'Black won {black_wins} with a depth of {black_depth}')

