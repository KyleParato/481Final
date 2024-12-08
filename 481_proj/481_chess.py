import chess
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
	print(board.legal_moves)

def print_board_replace(board):
	for i in range(0,8):
		print("\033[A", end="")
	print(board)


if __name__ == '__main__':
	#create the chess board
	print("Test board\n")
	board = chess.Board()
	kings_pawn_opening_setup(board)
	print(board)
	#use the A* search algorithm for winning pieces condition
	print("\Play Game depth 3 vs depth 5\n")
	c_ai = chess_ai()
	print(c_ai.alpha_beta_search(depth=5))
