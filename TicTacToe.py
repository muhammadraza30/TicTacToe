import tkinter as tk
from tkinter import font
import random
import time

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#2E3440")  # Dark background

        self.center_window(500, 600)

        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=14)

        self.human_char = None
        self.ai_char = None
        self.board = ['_'] * 9
        self.buttons = []
        self.multiplayer = False
        self.ai_difficulty = None

        self.player1_score = 0  # Player 1's score
        self.player2_score = 0  # Player 2's score (or AI's score)

        self.player1_name = ""
        self.player2_name = ""

        self.player1_name_entry = ""
        self.player2_name_entry = ""

        self.current_player = None  # Tracks whose turn it is
        self.turn_label = None  # Label to display current player's turn
        self.last_winner = None  # Tracks the last winner

        self.show_main_menu()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def show_main_menu(self):
        self.clear_widgets()
        self.menu_frame = tk.Frame(self.root, bg="#2E3440")
        self.menu_frame.pack(pady=50)

        tk.Label(self.menu_frame, text="Tic-Tac-Toe", font=self.title_font, bg="#2E3440", fg="#ffffff").pack(pady=20)

        tk.Button(self.menu_frame, text='Play', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.get_game_mode, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.menu_frame, text='Options', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.show_options, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.menu_frame, text='Exit', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.root.quit, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)

    def show_options(self):
        self.clear_widgets()
        self.options_frame = tk.Frame(self.root, bg="#2E3440")
        self.options_frame.pack(pady=50)

        tk.Label(self.options_frame, text="How to Play:", font=self.title_font, bg="#2E3440", fg="#ffffff").pack(pady=10)
        tk.Label(self.options_frame, text="1. Choose game mode: Multiplayer or Play with AI.", font=self.label_font, bg="#2E3440", fg="#ffffff").pack()
        tk.Label(self.options_frame, text="2. Select your symbol: X or O.", font=self.label_font, bg="#2E3440", fg="#ffffff").pack()
        tk.Label(self.options_frame, text="3. Play the game by clicking on the grid.", font=self.label_font, bg="#2E3440", fg="#ffffff").pack()
        tk.Label(self.options_frame, text="4. The first to get 3 in a row wins.", font=self.label_font, bg="#2E3440", fg="#ffffff").pack()
        tk.Button(self.options_frame, text='Back', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.show_main_menu, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=20)

    def get_game_mode(self):
        self.player1_score = 0  # Player 1's score
        self.player2_score = 0  # Player 2's score (or AI's score)
        self.clear_widgets()
        self.mode_frame = tk.Frame(self.root, bg="#2E3440")
        self.mode_frame.pack(pady=50)

        tk.Label(self.mode_frame, text="Choose game mode:", font=self.title_font, bg="#2E3440", fg="#ffffff").pack(pady=10)
        tk.Button(self.mode_frame, text='Multiplayer', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.set_multiplayer, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.mode_frame, text='Play with AI', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.set_ai, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.mode_frame, text='Back', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.show_main_menu, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)

    def entername(self):
        self.clear_widgets()
        self.mode_frame = tk.Frame(self.root, bg="#2E3440")
        self.mode_frame.pack(pady=50)

        tk.Label(self.mode_frame, text="Player 1 Name:", font=self.label_font, bg="#2E3440", fg="#ffffff").pack(pady=10)
        self.player1_name_entry = tk.Entry(self.mode_frame, font=self.label_font, bg="#333333", fg="#ffffff")
        self.player1_name_entry.pack(pady=10, padx=20)

        if self.multiplayer:
            tk.Label(self.mode_frame, text="Player 2 Name:", font=self.label_font, bg="#2E3440", fg="#ffffff").pack(pady=10)
            self.player2_name_entry = tk.Entry(self.mode_frame, font=self.label_font, bg="#333333", fg="#ffffff")
            self.player2_name_entry.pack(pady=10, padx=20)

        tk.Button(self.mode_frame, text='Next', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.nextButton, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.mode_frame, text='Back', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.get_game_mode, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)

    def nextButton(self):
        self.player1_name = self.player1_name_entry.get().capitalize()

        if self.multiplayer:
            self.player2_name = self.player2_name_entry.get().capitalize()
        else:
            self.player2_name = "AI"

        if self.multiplayer and self.player1_name != "" and self.player2_name != "" and self.player1_name != self.player2_name:
            self.get_symbols()
        else:
            if not self.multiplayer and self.player1_name != "":
                self.get_ai_difficulty()

    def set_multiplayer(self):
        self.multiplayer = True
        self.entername()

    def set_ai(self):
        self.multiplayer = False
        self.entername()

    def get_ai_difficulty(self):
        self.clear_widgets()
        self.difficulty_frame = tk.Frame(self.root, bg="#2E3440")
        self.difficulty_frame.pack(pady=50)

        tk.Label(self.difficulty_frame, text="Choose AI difficulty:", font=self.title_font, bg="#2E3440", fg="#ffffff").pack(pady=10)
        tk.Button(self.difficulty_frame, text='Easy', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=lambda: self.set_ai_difficulty('easy'), bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.difficulty_frame, text='Normal', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=lambda: self.set_ai_difficulty('normal'), bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.difficulty_frame, text='Hard', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=lambda: self.set_ai_difficulty('hard'), bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.difficulty_frame, text='Back', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.get_game_mode, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)

    def set_ai_difficulty(self, difficulty):
        self.ai_difficulty = difficulty
        self.get_symbols()

    def get_symbols(self):
        self.clear_widgets()
        self.symbol_frame = tk.Frame(self.root, bg="#2E3440")
        self.symbol_frame.pack(pady=50)

        tk.Label(self.symbol_frame, text="Choose your symbol:", font=self.title_font, bg="#2E3440", fg="#ffffff").pack(pady=10)
        tk.Button(self.symbol_frame, text='X', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=lambda: self.set_symbols('X'), bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.symbol_frame, text='O', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=lambda: self.set_symbols('O'), bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)
        tk.Button(self.symbol_frame, text='Back', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.get_game_mode if self.multiplayer else self.get_ai_difficulty, bd=0, activebackground="#5E81AC", activeforeground="#ffffff").pack(pady=10)

    def set_symbols(self, symbol):
        self.human_char = symbol
        self.ai_char = 'O' if symbol == 'X' else 'X'

        self.clear_widgets()
        tk.Label(self.root, text="Starting game in 1 second...", font=self.label_font, bg="#2E3440", fg="#ffffff").pack()
        self.root.update()
        time.sleep(1)

        self.create_board()

        if self.last_winner is None:
            self.current_player = random.choice([self.human_char, self.ai_char])
        else:
            self.current_player = self.last_winner

        self.update_turn_label()

        if not self.multiplayer and self.current_player == self.ai_char:
            self.ai_move()

    def create_board(self):
        self.clear_widgets()
        self.board = ['_'] * 9
        self.buttons = []

        if self.multiplayer:
            self.score_label = tk.Label(self.root, text=f"{self.player1_name}: {self.player1_score}  {self.player2_name}: {self.player2_score}",
                                       font=self.label_font, bg="#2E3440", fg="#ffffff")
        else:
            self.score_label = tk.Label(self.root, text=f"{self.player1_name}: {self.player1_score}  {self.player2_name}: {self.player2_score}",
                                       font=self.label_font, bg="#2E3440", fg="#ffffff")
        self.score_label.pack(pady=10)

        self.turn_label = tk.Label(self.root, text="", font=self.label_font, bg="#2E3440", fg="#ffffff")
        self.turn_label.pack(pady=10)

        board_frame = tk.Frame(self.root, bg="#2E3440")
        board_frame.pack(pady=20)

        for i in range(9):
            btn = tk.Button(board_frame, text='', font=self.button_font, bg="#4C566A", fg="#ffffff", width=5, height=2,
                            command=lambda i=i: self.human_move(i), bd=0, activebackground="#5E81AC", activeforeground="#ffffff")
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        self.update_turn_label()

    def update_turn_label(self):
        if hasattr(self, 'turn_label') and self.turn_label.winfo_exists():
            if self.multiplayer:
                if self.current_player == self.human_char:
                    self.turn_label.config(text=f"{self.player1_name}'s turn (X)" if self.human_char == 'X' else f"{self.player1_name}'s turn (O)")
                else:
                    self.turn_label.config(text=f"{self.player2_name}'s turn (O)" if self.human_char == 'X' else f"{self.player2_name}'s turn (X)")
            else:
                if self.current_player == self.human_char:
                    self.turn_label.config(text=f"{self.player1_name}'s turn")
                else:
                    self.turn_label.config(text=f"{self.player2_name}'s turn")

    def human_move(self, index):
        if self.board[index] == '_':
            # Use the current player's symbol
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="#ffffff")

            if self.check_gameover():
                return

            # Switch turns
            if self.multiplayer:
                if self.current_player == self.human_char:
                    self.current_player = self.ai_char  # Switch to Player 2
                else:
                    self.current_player = self.human_char  # Switch back to Player 1
            else:
                self.current_player = self.ai_char  # Switch to AI
                self.ai_move()

            # Update the turn label
            self.update_turn_label()

    def ai_move(self):
        # Add a 2-second delay before AI makes its move
        self.turn_label.config(text=f"{self.player2_name} is thinking...")
        self.root.update()
        time.sleep(0.5)

        if self.ai_difficulty == 'easy':
            move = self.easy_ai()
        elif self.ai_difficulty == 'normal':
            move = self.normal_ai()
        elif self.ai_difficulty == 'hard':
            _, move = self.alphabeta(self.board, True)

        if move is not None:
            self.board[move] = self.ai_char
            self.buttons[move].config(text=self.ai_char, fg="#ffffff")
            if self.check_gameover():
                return
            self.current_player = self.human_char  # Switch back to human
            self.update_turn_label()

    def easy_ai(self):
        available_moves = [i for i, val in enumerate(self.board) if val == '_']
        return random.choice(available_moves)

    def normal_ai(self):
        if random.choice([True, False]):
            _, move = self.alphabeta(self.board, True)
            return move
        else:
            return self.easy_ai()

    def check_gameover(self):
        winner, winning_cells = self.get_winner()

        if winner or '_' not in self.board:
            if winner:
                for index in winning_cells:
                    self.buttons[index].config(bg="#A3BE8C")

                if self.multiplayer:
                    winner_name = self.player1_name if winner == self.human_char else self.player2_name
                else:
                    winner_name = self.player1_name if winner == self.human_char else "AI"

                self.last_winner = winner
            else:
                winner_name = "It's a Tie!"

            self.root.after(2000, self.show_result, winner_name, winner)

            return True
        return False

    def show_result(self, winner_name, winner):
        for btn in self.buttons:
            btn.config(bg="#4C566A")

        if winner:
            if self.multiplayer:
                if winner == self.human_char:
                    self.player1_score += 1
                else:
                    self.player2_score += 1
            else:
                if winner == self.human_char:
                    self.player1_score += 1
                else:
                    self.player2_score += 1

        self.clear_widgets()
        result_text = f"{winner_name} wins!" if winner else "It's a Tie!"
        tk.Label(self.root, text=result_text, font=self.title_font, bg="#2E3440", fg="#ffffff").pack( pady=40)

        self.root.after(1000, self.show_play_again_options)

    def show_play_again_options(self):
        play_again_frame = tk.Frame(self.root, bg="#2E3440")
        play_again_frame.pack(pady=50)

        # Display the score
        if self.multiplayer:
            tk.Label(play_again_frame, text=f"{self.player1_name}: {self.player1_score}  {self.player2_name}: {self.player2_score}",
                      font=self.label_font, bg="#2E3440", fg="#ffffff").pack(pady=10)
        else:
            tk.Label(play_again_frame, text=f"{self.player1_name}: {self.player1_score}  {self.player2_name}: {self.player2_score}",
                      font=self.label_font, bg="#2E3440", fg="#ffffff").pack(pady=10)

        tk.Label(play_again_frame, text="Do you want to play again?", font=self.title_font, bg="#2E3440", fg="#ffffff").pack(pady=10)

        button_frame = tk.Frame(play_again_frame, bg="#2E3440")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text='Yes', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.reset_game).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text='No', font=self.button_font, bg="#4C566A", fg="#ffffff", padx=20, pady=10,
                  command=self.show_main_menu).pack(side=tk.LEFT, padx=10)

    def reset_game(self):
        self.create_board()
        # Assign the first move to the last winner
        if self.last_winner is not None:
            self.current_player = self.last_winner
        else:
            self.current_player = random.choice([self.human_char, self.ai_char])

        self.update_turn_label()

        if not self.multiplayer and self.current_player == self.ai_char:
            self.ai_move()

    def reset_score(self):
        self.player1_score = 0
        self.player2_score = 0
        self.show_main_menu()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def get_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != '_':
                return self.board[a], combo  # Return winner and winning cells

        return None, None  # No winner

    def alphabeta(self, board, maximizing, alpha=-2, beta=2):
        winner = self.get_winner()
        if winner == self.human_char:
            return -1, None
        elif winner == self.ai_char:
            return 1, None
        elif '_' not in board:
            return 0, None

        if maximizing:
            max_eval, best_move = -2, None
            for i in range(9):
                if board[i] == '_':
                    board[i] = self.ai_char
                    eval, _ = self.alphabeta(board, False, alpha, beta)
                    board[i] = '_'
                    if eval > max_eval:
                        max_eval, best_move = eval, i
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval, best_move
        else:
            min_eval, best_move = 2, None
            for i in range(9):
                if board[i] == '_':
                    board[i] = self.human_char
                    eval, _ = self.alphabeta(board, True, alpha, beta)
                    board[i] = '_'
                    if eval < min_eval:
                        min_eval, best_move = eval, i
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval, best_move

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()