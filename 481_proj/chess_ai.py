import chess

# alpha beta search chess ai
class chess_ai():

    # initialize object
    def __init__(self):
        self.board = chess.Board()
        self.moves = self.board.legal_moves
        self.utility = self.current_utility_score(self.board)

    # prints over current printed board
    def print_board_replace(self, board):
        for i in range(0,8):
            print("\033[A", end="")
        print(board)

    # calculate utility score of board
    def current_utility_score(self, board, aggression_motivaion=1):
        util = 0 # utility score

        # calculate material cost, white pieces are postive, black is negative
        def material_cost(c):
            cost = 0
            if c == 'p':
                cost += -1
            elif c == 'n' or c == "b":
                cost += -3
            elif c == 'r':
                cost += -5
            elif c == 'q':
                cost += -9
            elif c == 'k':
                cost += -1000
            elif c == 'P':
                cost += 1
            elif c == 'N' or c == "B":
                cost += 3
            elif c == 'R':
                cost += 5
            elif c == 'Q':
                cost += 9
            elif c == 'K':
                cost += 1000
            return cost
        
        squares = chess.SQUARES # board "itr"
        fen_str = board.board_fen() # string of fen notation
        fen = [] # list of rows in fen notation
        
        # seperate fen notation of board into fen notation of rows
        for i in range(0,7):
            fen.append(fen_str[:fen_str.find("/")])
            fen_str = fen_str[fen_str.find("/")+1:]
        fen.append(fen_str)

        # iterate through board
        square_num = 0
        for row in reversed(fen):
            for c in row: # iterate through row
                if str.isdigit(c): # skip empty squares
                    square_num += int(c) # skip c squares
                else: # square has piece
                    util += material_cost(c) # add material piece of current squre
                    square_num += 1          # next square
                    atk = board.attacks(squares[square_num-1]) # get pieces it can attack
                    if len(atk) != 0: # if there are pieces to attack
                        atks = list(atk)
                        for a in atks: # iterate through pieces to attack
                            piece = str(board.piece_at(squares[a]))
                            x = material_cost(piece) # get piece material cost
                            if x < 999 and x > 0: # if not white king, add material cost + motivation
                                util += x - aggression_motivaion
                            if x > -999 and x < 0: # if not black king, add material cost - motivation
                                util += x + aggression_motivaion
                            if x == 1000: # if white king, add motivation factor * 10, adding util breaks ai
                                util -= (aggression_motivaion*10)
                            if x == -1000: # if black king
                                util += -(aggression_motivaion*10)
        return util

    # if no more legal moves
    def terminal_test(self, board):
        if len(list(board.legal_moves)) == 0:
            return True
    
    # alpha beta search with depth
    def alpha_beta_search(self, depth, aggression=1, print_board=False):
        #min
        def min_val(self, board, alpha, beta, depth, aggression=aggression, print_board=print_board):
            if self.terminal_test(board) or depth == 0:
                return self.current_utility_score(board, aggression_motivaion=aggression)
            val = 1000
            moves = list(board.legal_moves)
            for move in moves:
                board.push(move)
                if print_board:
                    self.print_board_replace(board)
                val = min(val, max_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1), aggression=aggression, print_board=print_board))
                board.pop()
                if val <= alpha:
                    return val
                beta = min(beta, val)
                moves = moves[1:]
            return val 
        #max
        def max_val(self, board, alpha, beta, depth, aggression=aggression, print_board=print_board):
            if self.terminal_test(board) or depth == 0:
                return self.current_utility_score(board, aggression_motivaion=aggression)
            val = -1000
            moves = list(board.legal_moves)
            for move in moves:
                board.push(move)
                if print_board:
                    self.print_board_replace(board)
                val = max(val, min_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1), aggression=aggression, print_board=print_board))
                board.pop()
                if val >= beta:
                    return val
                alpha = max(alpha, val)
                moves = moves[1:]
            return val

        board = self.board
        if print_board:
            print(board)
        
        if depth < 1:
            depth = 1
    
        moves = list(board.legal_moves)

        alpha = -1000
        beta = 1000

        best_move = None

        # White turn (max)
        if board.turn:
            for move in moves:
                board.push(move)
                if print_board:
                    self.print_board_replace(board)
                val = min_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1))
                board.pop()
                if val > alpha:
                    alpha = val
                    best_move = move
        # Black turn (min)
        else:
            for move in moves:
                board.push(move)
                if print_board:
                    self.print_board_replace(board)
                val = max_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1))
                board.pop()
                if val < beta:
                    beta = val
                    best_move = move
        return best_move
