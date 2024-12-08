import chess


class chess_ai():


    def __init__(self):
        self.board = chess.Board()
        self.moves = self.board.legal_moves
        self.utility = self.current_utility_score(self.board)
        pass

    def print_board_replace(self, board):
        for i in range(0,8):
            print("\033[A", end="")
        print(board)

    def set_board(self, new_board):
        self.board = new_board
        return
    
    def current_utility_score(self, board):
        util = 0
        # material cost
        for c in str(board):
            if c == 'p':
                util += -1
                continue
            if c == 'n' or c == "b":
                util += -3
                continue
            if c == 'r':
                util += -5
                continue
            if c == 'q':
                util += -9
                continue
            if c == 'k':
                util += -1000
                continue
            if c == 'P':
                util += 1
                continue
            if c == 'N' or c == "B":
                util += 3
                continue
            if c == 'R':
                util += 5
                continue
            if c == 'Q':
                util += 9
                continue
            if c == 'K':
                util += 1000
                continue

        return util
    
    def terminal_test(self, board):
        if len(list(board.legal_moves)) == 0:
            return True
    
    def alpha_beta_search(self, depth):

        #min
        def min_val(self, board, alpha, beta, depth):
            if self.terminal_test(board) or depth == 0:
                return self.current_utility_score(board)
            val = 1000
            moves = list(board.legal_moves)
            for move in moves:
                board.push(move)
                self.print_board_replace(board)
                val = min(val, max_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1)))
                board.pop()
                if val <= alpha:
                    return val
                beta = min(beta, val)
                moves = moves[1:]
            return val
        
        #max
        def max_val(self, board, alpha, beta, depth):
            if self.terminal_test(board) or depth == 0:
                return self.current_utility_score(board)
            val = -1000
            moves = list(board.legal_moves)
            for move in moves:
                board.push(move)
                self.print_board_replace(board)
                val = max(val, min_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1)))
                board.pop()
                if val >= beta:
                    return val
                alpha = max(alpha, val)
                moves = moves[1:]
            return val

        board = self.board
        print(board)
        
        if depth < 1:
            return -1
    
        moves = list(board.legal_moves)

        alpha = -1000
        beta = 1000

        best_move = None

        for move in moves:
            board.push(move)
            self.print_board_replace(board)
            val = min_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1))
            board.pop()
            if val > alpha:
                alpha = val
                best_move = move
        return best_move



