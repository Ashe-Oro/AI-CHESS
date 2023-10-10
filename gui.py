'''
This file contains the ChessGUI class which represents the graphical user interface.
'''
import tkinter as tk
from chess_game import ChessGame
class ChessGUI:
    def __init__(self, game):
        self.game = game
        # Create the main window
        self.window = tk.Tk()
        self.window.title("AI Chess")
        # Create the chess board GUI
        self.create_board_gui()
    def create_board_gui(self):
        # Create the chess board GUI using tkinter
        board = self.game.get_board()
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                label = tk.Label(self.window, text=piece, width=2, height=1)
                label.grid(row=row, column=col)
    def start(self):
        # Start the GUI main loop
        self.window.mainloop()