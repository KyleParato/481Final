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
        
        squares = chess.SQUARES
        square_names = chess.SQUARE_NAMES
        fen_str = board.board_fen()
        fen = []
        
        for i in range(0,7):
            fen.append(fen_str[:fen_str.find("/")])
            fen_str = fen_str[fen_str.find("/")+1:]
        fen.append(fen_str)

        square_num = 0
        for row in reversed(fen):
            for c in row:
                if str.isdigit(c):
                    square_num += int(c)
                else:
                    util += material_cost(c)
                    square_num += 1
                    atk = board.attacks(squares[square_num-1])
                    if len(atk) != 0:
                        atks = list(atk)
                        for a in atks:
                            piece = str(board.piece_at(squares[a]))
                            x = material_cost(piece)
                            if x < 999 and x > 0:
                                util += x + 1
                            if x > -999 and x < 0:
                                util += x -1
                            if x == 1000:
                                util += 10
                            if x == -1000:
                                util += -10

                        util += 1
            pass
            #print(row)

        return util
    
    
    def terminal_test(self, board):
        if len(list(board.legal_moves)) == 0:
            return True
    

    # alpha beta search with depth
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

        # White turn (max)
        if board.turn:
            for move in moves:
                board.push(move)
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
                self.print_board_replace(board)
                val = max_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1))
                board.pop()
                if val < beta:
                    beta = val
                    best_move = move
        return best_move

    def alpha_beta_search_no_print(self, depth, last_move=None):
        #min
        def min_val(self, board, alpha, beta, depth, last_move):
            if self.terminal_test(board) or depth == 0:
                return self.current_utility_score(board)
            val = 1000
            moves = list(board.legal_moves)

            for i in moves:
                if str(i) == last_move:
                    moves.remove(i)
                    break

            for move in moves:
                board.push(move)
                val = min(val, max_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1), last_move=last_move))
                board.pop()
                if val <= alpha:
                    return val
                beta = min(beta, val)
                moves = moves[1:]
            return val
        
        #max
        def max_val(self, board, alpha, beta, depth, last_move):
            if self.terminal_test(board) or depth == 0:
                return self.current_utility_score(board)
            val = -1000
            moves = list(board.legal_moves)

            for i in moves:
                if str(i) == last_move:
                    moves.remove(i)
                    break

            for move in moves:
                board.push(move)
                val = max(val, min_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1), last_move=last_move))
                board.pop()
                if val >= beta:
                    return val
                alpha = max(alpha, val)
                moves = moves[1:]
            return val

        board = self.board
        
        if depth < 1:
            return -1
    
        moves = list(board.legal_moves)

        alpha = -1000
        beta = 1000

        best_move = None

        # White turn (max)
        if board.turn:
            for move in moves:
                board.push(move)
                val = min_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1), last_move=last_move)
                board.pop()
                if val > alpha:
                    alpha = val
                    best_move = move
        # Black turn (min)
        else:
            for move in moves:
                board.push(move)
                val = max_val(self, board=board, alpha=alpha, beta=beta, depth=(depth -1), last_move=last_move)
                board.pop()
                if val < beta:
                    beta = val
                    best_move = move
        return best_move
