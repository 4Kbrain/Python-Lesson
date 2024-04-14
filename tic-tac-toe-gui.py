import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.players = ["X", "O"]
        self.current_player = 0
        self.current_round = 1
        self.rounds_to_win = 3
        self.round_winner = None
        self.rounds = {player: 0 for player in self.players}
        self.create_board()
        self.create_buttons()
        self.window.mainloop()

    def create_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def create_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", width=10, height=3,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, i, j):
        if self.board[i][j] == " " and not self.round_winner:
            self.board[i][j] = self.players[self.current_player]
            self.buttons[i][j].config(text=self.players[self.current_player])
            if self.check_winner():
                self.rounds[self.players[self.current_player]] += 1
                if self.rounds[self.players[self.current_player]] == self.rounds_to_win:
                    messagebox.showinfo("Game Over", f"Player {self.players[self.current_player]} wins the game!")
                    self.rounds = {player: 0 for player in self.players}
                else:
                    self.round_winner = self.players[self.current_player]
                    messagebox.showinfo("Round Over", f"Player {self.players[self.current_player]} wins the round!")
                    self.current_round += 1
                    self.current_player = (self.current_player + 1) % 2
                    self.reset_board()
            elif all(all(cell != " " for cell in row) for row in self.board):
                messagebox.showinfo("Round Over", "It's a tie!")
                self.current_round += 1
                self.current_player = (self.current_player + 1) % 2
                self.reset_board()
            else:
                self.current_player = (self.current_player + 1) % 2

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
    game = TicTacToe()
