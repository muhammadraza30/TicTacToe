import tkinter as tk
from tkinter import font
import time
from tictactoelogic import tictactoelogic as tttl
import random


class ui_window:

    def __init__(self, root):
        self.board = ['_'] * 9
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#2E3440")  # Dark background

        self.center_window(500, 600)

        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=14)

        self.logic = tttl()
        self.buttons = []
        self.multiplayer = False

        self.player1_score = 0  # Player 1's score
        self.player2_score = 0  # Player 2's score (or AI's score)

        self.player1_name = ""
        self.player2_name = ""

        self.player1_name_entry = None
        self.player2_name_entry = None
       
        self.turn_label = None  # Label to display current player's turn

        self.show_main_menu()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def createLabel(self, frame, text, font, bg="#2E3440", fg="#ffffff", pady=20, padx=20):
        label = tk.Label(frame, text=text, font=font, bg=bg, fg=fg, pady=pady, padx=padx)
        return label

    def createButton(self, frame, text, btnCommand, side="top", bg="#4C566A", fg="#ffffff", pady=10, padx=10, packpady=10, packpadx=10):
        button = tk.Button(frame, text=text, font=self.button_font, bg=bg, fg=fg, pady=pady, padx=padx, command=btnCommand, bd=5, activebackground="#5E81AC", activeforeground="#ffffff")
        button.pack(pady=packpady, padx=packpadx, side=side)

    def createEntry(self, frame,textvariable, bg="#333333", fg="#ffffff" ):
        entry = tk.Entry(frame, font=self.label_font, textvariable=textvariable , bg=bg, fg=fg)# Create a new entry field
        # entry.pack()
        return entry

    def show_main_menu(self):
        self.clear_widgets()
        menu_frame = tk.Frame(self.root, bg="#2E3440")
        menu_frame.pack(pady=50)

        self.createLabel(menu_frame, "Tic-Tac-Toe", font=self.title_font).pack()
        self.createButton(menu_frame, 'Play', self.get_game_mode)# Play button
        self.createButton(menu_frame, 'Options', self.show_options)
        self.createButton(menu_frame, 'Exit', self.root.quit)
       
    def show_options(self):
        self.clear_widgets()
        
        options_frame = tk.Frame(self.root, bg="#2E3440")
        options_frame.pack(pady=50)
        
        self.createLabel(options_frame, text="How to Play:", font=self.title_font).pack(pady=10)

        # Game Instructions
        instructions = [
            "1. Choose game mode: Multiplayer or Play with AI.",
            "2. Select your symbol: X or O.",
            "3. Play the game by clicking on the grid.",
            "4. The first to get 3 in a row wins."
        ]

        for instruction in instructions:
            self.createLabel(options_frame, instruction, font=self.label_font).pack(anchor="w", padx=10, pady=5)

        # Back Button
        self.createButton(options_frame, 'Back', self.show_main_menu, packpady=20)

        
    def get_game_mode(self):
        self.player1_score = 0  # Player 1's score
        self.player2_score = 0  # Player 2's score (or AI's score)
        self.clear_widgets()
        mode_frame = tk.Frame(self.root, bg="#2E3440")
        mode_frame.pack(pady=50)

        self.createLabel(mode_frame, "Choose game mode:", font=self.title_font).pack()
        self.createButton(mode_frame, 'Multiplayer', self.set_multiplayer)
        self.createButton(mode_frame, 'Play with AI', self.set_ai)
        self.createButton(mode_frame, 'Back', self.show_main_menu)
        
    def entername(self):
        self.clear_widgets()
        mode_frame = tk.Frame(self.root, bg="#2E3440")
        mode_frame.pack(pady=50)

        # Player 1 Input
        player1_frame = tk.Frame(mode_frame, bg="#2E3440")
        player1_frame.pack(pady=10)
        
        self.createLabel(player1_frame, "Enter Player 1 Name:", font=self.label_font).pack(side="left", padx=5, pady=10)
        self.player1_name_entry = self.createEntry(player1_frame, self.player1_name_entry)
        self.player1_name_entry.pack(side="left", padx=5, pady=10)

        # Player 2 Input (only in multiplayer mode)
        if self.multiplayer:
            player2_frame = tk.Frame(mode_frame, bg="#2E3440")
            player2_frame.pack(pady=10)
            
            self.createLabel(player2_frame, "Enter Player 2 Name:", font=self.label_font).pack(side="left", padx=5, pady=10)
            self.player2_name_entry = self.createEntry(player2_frame, self.player2_name_entry)
            self.player2_name_entry.pack(side="left", padx=5, pady=10)

        # Buttons
        button_frame = tk.Frame(mode_frame, bg="#2E3440")
        button_frame.pack(pady=20)

        self.createButton(button_frame, "Next", self.nextButton, side="left", packpady=10, packpadx=20)
        self.createButton(button_frame, "Back", self.get_game_mode, side="left", packpady=10, packpadx=20)


    def nextButton(self):
        print(self.turn_label)
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
        print(self.multiplayer)
        self.entername()

    def get_ai_difficulty(self):
        self.clear_widgets()
        difficulty_frame = tk.Frame(self.root, bg="#2E3440")
        difficulty_frame.pack(pady=50)

        self.createLabel(difficulty_frame, "Choose AI difficulty:", font=self.title_font).pack()
        self.createButton(difficulty_frame, 'Easy', lambda : self.set_ai_difficulty("easy"))
        self.createButton(difficulty_frame, 'Normal', lambda : self.set_ai_difficulty("normal"))
        self.createButton(difficulty_frame, 'Hard', lambda : self.set_ai_difficulty("hard"))
        self.createButton(difficulty_frame, 'Back', self.get_game_mode)
        
    def set_ai_difficulty(self, difficulty):
        self.logic.ai_difficulty = difficulty  # Store as a string
        self.get_symbols()


    def get_symbols(self):
        self.clear_widgets()

        symbol_frame = tk.Frame(self.root, bg="#2E3440")
        symbol_frame.pack(pady=50)

        # Title Label
        self.createLabel(symbol_frame, f"{self.player1_name} choose your symbol:", font=self.title_font).pack(pady=10)

        # Symbol Selection Buttons (X & O)
        button_frame = tk.Frame(symbol_frame, bg="#2E3440")
        button_frame.pack(pady=20)

        self.createButton(button_frame, 'X', lambda: self.set_symbols('X'), side="left", packpadx=20)
        self.createButton(button_frame, 'O', lambda: self.set_symbols('O'), side="left", packpadx=20)

        # Back Button (Placed Below)
        self.createButton(symbol_frame, 'Back', self.get_game_mode, packpady=20)


    def set_symbols(self, symbol):
        self.logic.set_symbols(symbol)
        if self.logic.last_winner:
            self.logic.current_player = self.logic.last_winner  # Ensures the last winner starts the next round
        self.clear_widgets()
        self.createLabel(self.root, "Starting game in 1 second...", font=self.label_font).pack()
        self.root.update()
        time.sleep(1)
        self.create_board()
        self.update_turn_label()
        if not self.multiplayer and self.logic.current_player == self.logic.ai_char:
            self.ai_move()

    def create_board(self):
        self.clear_widgets()
        self.logic.reset_board()
        self.buttons = []

        self.score_label = self.createLabel(self.root, text=f"{self.player1_name}: {self.player1_score}  {self.player2_name}: {self.player2_score}", font=self.label_font) 
        self.turn_label = self.createLabel(self.root, text="", font=self.label_font)
        self.turn_label.pack()

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
                if self.logic.current_player == self.logic.human_char:
                    self.turn_label.config(text=f"{self.player1_name}'s turn (X)" if self.logic.human_char == 'X' else f"{self.player1_name}'s turn (O)")
                else:
                    self.turn_label.config(text=f"{self.player2_name}'s turn (O)" if self.logic.human_char == 'X' else f"{self.player2_name}'s turn (X)")
            else:
                if self.logic.current_player == self.logic.human_char:
                    self.turn_label.config(text=f"{self.player1_name}'s turn")
                else:
                    self.turn_label.config(text=f"{self.player2_name}'s turn")

    def human_move(self, index):
        if self.logic.make_move(index, self.logic.current_player):
            self.buttons[index].config(text=self.logic.current_player, fg="#ffffff")
            
            if self.check_gameover():  # Stop AI if game is over
                return
            
            self.logic.current_player = self.logic.ai_char if not self.multiplayer else ('O' if self.logic.current_player == 'X' else 'X')
            self.update_turn_label()

            if not self.multiplayer and self.logic.current_player == self.logic.ai_char:
                self.ai_move()


    def ai_move(self):
        self.turn_label.config(text=f"{self.player2_name} is thinking...")
        self.root.update()
        time.sleep(0.5)

        if self.logic.ai_difficulty == "easy":
            move = self.logic.easy_ai()
        elif self.logic.ai_difficulty == "normal":
            move = self.logic.normal_ai()
        else:
            _, move = self.logic.alphabeta(self.logic.board, True)

        if move is not None:
            self.logic.make_move(move, self.logic.ai_char)
            self.buttons[move].config(text=self.logic.ai_char, fg="#ffffff")

            if self.check_gameover():
                return

            self.logic.current_player = self.logic.human_char
            self.update_turn_label()


    def check_gameover(self):
        winner, winning_cells = self.logic.get_winner()  # Use self.logic.get_winner()
        print("Board:", self.logic.board)

        if winner or '_' not in self.logic.board:  # Always refer to self.logic.board
            if winner:
                for index in winning_cells:
                    self.buttons[index].config(bg="#A3BE8C")

                winner_name = self.player1_name if winner == self.logic.human_char else self.player2_name
                self.logic.last_winner = winner
            else:
                winner_name = "It's a Tie!"

            self.root.after(2000, self.show_result, winner_name, winner)
            return True

        return False

    def show_result(self, winner_name, winner):
        for btn in self.buttons:
            btn.config(bg="#4C566A")

        if winner:
            if winner == self.logic.human_char:
                self.player1_score += 1
            else:
                self.player2_score += 1

            self.logic.last_winner = winner  # Store the last winner for next round
        else:
            self.logic.last_winner = None  # No winner in case of a tie

        self.clear_widgets()
        result_text = f"{winner_name} wins!" if winner else "It's a Tie!"
        self.createLabel(self.root, text=result_text, font=self.title_font, pady=40).pack()

        self.root.after(1000, self.show_play_again_options)


    def show_play_again_options(self):
        play_again_frame = tk.Frame(self.root, bg="#2E3440")
        play_again_frame.pack(pady=50)

        # Display the score
        self.createLabel(play_again_frame, text=f"{self.player1_name}: {self.player1_score}  {self.player2_name}: {self.player2_score}", font=self.label_font).pack()

        self.createLabel(play_again_frame, text="Do you want to play again?", font=self.title_font).pack()

        button_frame = tk.Frame(play_again_frame, bg="#2E3440")
        button_frame.pack()

        self.createButton(button_frame, 'Yes', self.restart_game,side="left")
        self.createButton(button_frame, 'No', self.show_main_menu, side="left")

        
    def restart_game(self):
        self.logic.reset_board()  # Ensure board is cleared
        self.create_board()
        self.update_turn_label()

        if not self.multiplayer and self.logic.current_player == self.logic.ai_char:
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
            # if self.board[a] == self.board[b] == self.board[c] and self.board[a] != '_':
            if self.logic.board[a] == self.logic.board[b] == self.logic.board[c] and self.logic.board[a] != '_':
                return self.board[a], combo  # Return winner and winning cells

        return None, None  # No winner