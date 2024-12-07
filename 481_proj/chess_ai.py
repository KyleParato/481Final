import chess


class chess_alpha_beta_search():


    def __init__(self):
        self.board = chess.Board()
        self.moves = self.board.legal_moves
        self.utility = self.current_utility_score(self.board)
        pass

    def set_board(self, new_board):
        self.board = new_board
        return
    
    def current_utility_score(self, board):
        return 1