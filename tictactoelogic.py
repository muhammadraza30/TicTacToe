import random

class tictactoelogic:
    def __init__(self):
        self.board = ['_'] * 9
        self.human_char = None
        self.ai_char = None
        self.current_player = None
        self.last_winner = None
        self.ai_difficulty = None

    def set_symbols(self, symbol):
        self.human_char = symbol
        self.ai_char = 'O' if symbol == 'X' else 'X'
        self.current_player = random.choice([self.human_char, self.ai_char]) if self.last_winner is None else self.last_winner

    def reset_board(self):
        self.board = ['_'] * 9

    def make_move(self, index, player):
        if self.board[index] == '_':
            self.board[index] = player
            return True
        return False

    # def get_winner(self):
    #     winning_combinations = [
    #         (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    #         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    #         (0, 4, 8), (2, 4, 6)  # Diagonals
    #     ]

    #     for combo in winning_combinations:
    #         a, b, c = combo
    #         if self.board[a] == self.board[b] == self.board[c] and self.board[a] != '_':
    #             return self.board[a], combo  # Return winner and winning cells

    #     return None, None  # No winner

    def get_winner(self):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                    (0, 4, 8), (2, 4, 6)]:  # Diagonals
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != '_':
                return self.board[a], combo
        return None, []

    def easy_ai(self):
        available_moves = [i for i, val in enumerate(self.board) if val == '_']
        return random.choice(available_moves)
        


    def is_winning_move(self, move, player):
        """Check if a move leads to a win for the given player."""
        self.board[move] = player
        winner, _ = self.get_winner()
        self.board[move] = '_'  # Undo the move
        return winner == player

    def normal_ai(self):
        available_moves = [i for i, val in enumerate(self.board) if val == '_']

        # if random.random() < 0.6:  # 60% chance of playing optimally
        #     _, move = self.easy_ai()
        #     return move if move is not None else random.choice(available_moves)
        
        #  _, best_move = self.alphabeta(self.board, True)
        # return best_move if best_move is not None else random.choice(available_moves)
        if random.choice([True, False]):
            _, move = self.alphabeta(self.board, True)
            return move if move is not None else random.choice(available_moves)
        else:
            return self.easy_ai()
        
    def alphabeta(self, board, maximizing, alpha=-2, beta=2):
        board_copy = board[:]  # Copy the board
        winner, _ = self.get_winner()
        
        if winner == self.human_char:
            return -1, None
        elif winner == self.ai_char:
            return 1, None
        elif '_' not in board_copy:
            return 0, None

        if maximizing:
            max_eval, best_move = -2, None
            for i in range(9):
                if board_copy[i] == '_':
                    board_copy[i] = self.ai_char
                    eval, _ = self.alphabeta(board_copy, False, alpha, beta)
                    board_copy[i] = '_'
                    if eval > max_eval:
                        max_eval, best_move = eval, i
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval, best_move
        else:
            min_eval, best_move = 2, None
            for i in range(9):
                if board_copy[i] == '_':
                    board_copy[i] = self.human_char
                    eval, _ = self.alphabeta(board_copy, True, alpha, beta)
                    board_copy[i] = '_'
                    if eval < min_eval:
                        min_eval, best_move = eval, i
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval, best_move
