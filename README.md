# Tic-Tac-Toe Game with AI and Multiplayer Mode

## Overview
This is a graphical Tic-Tac-Toe game built using Python's Tkinter library. The game offers multiple modes, including:
- **Multiplayer Mode**: Two users can play against each other.
- **AI Mode**: Play against an AI opponent with three difficulty levels: Easy, Normal, and Hard.
- **Hard Mode AI**: Uses the Alpha-Beta Pruning algorithm for efficient decision-making.

## Features
- **Graphical Interface**: Built with Tkinter, featuring a modern dark theme.
- **Multiplayer Support**: Play with a friend on the same device.
- **AI Opponent**: Choose from three AI difficulty levels.
- **Minimax with Alpha-Beta Pruning**: AI plays optimally at Hard difficulty.
- **Score Tracking**: Keeps track of wins for both players.
- **Randomized First Move**: Ensures fairness by choosing the first player randomly.

## Installation
To run the game, you need Python installed on your system. Follow these steps:

1. Clone or download this repository.
2. Install Tkinter (comes pre-installed with Python, but ensure it's available):
   ```sh
   pip install tk
   ```
3. Run the script:
   ```sh
   python tictactoe.py
   ```

## How to Play
1. **Launch the Game**: Run the Python script.
2. **Choose a Mode**:
   - Multiplayer (Two players take turns)
   - Play against AI (Select difficulty: Easy, Normal, Hard)
3. **Choose Symbol**: Pick 'X' or 'O' for the game.
4. **Gameplay**:
   - Click on a grid cell to make a move.
   - The game continues until a player gets three marks in a row (horizontally, vertically, or diagonally) or the board is full.
5. **End of Game**:
   - The winner is displayed, or a tie is declared.
   - Play again or exit.

## AI Difficulty Levels
- **Easy**: Random moves.
- **Normal**: Mix of random moves and optimal strategy.
- **Hard**: Uses Alpha-Beta Pruning for the best moves.

## Technologies Used
- **Python**
- **Tkinter** (for GUI)
- **Minimax Algorithm with Alpha-Beta Pruning** (for AI decision-making)

## Future Improvements
- Implement online multiplayer support.
- Add sound effects for gameplay.
- Improve AI response time.

## License
This project is open-source and available for modification and use. Feel free to contribute and enhance the features!

---
Enjoy playing Tic-Tac-Toe!
