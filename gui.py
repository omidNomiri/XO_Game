import tkinter as tk
from tkinter import messagebox
from game_logic import (
    create_board,
    make_move,
    check_winner,
    is_draw,
    switch_player
)


class Game_GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Control Shield Quantum")

        self.board = create_board()
        self.current_player = "X"
        self.buttons: list[object] = []
        self.mode = "PVP"
        self.turn_view = None

        self.create_grid()
        self.create_turn_view()
        self.create_reset_button()

        self.window.mainloop()

    def create_turn_view(self):
        if self.turn_view is None:
            self.turn_view = tk.Button(
                self.window,
                text="",
                font=("Arial", 24),
                width=5,
                height=2,
                state="disabled")
            self.turn_view.grid(row=3, column=0, columnspan=1, sticky="we")
        self.turn_view.config(text=f"turn: {self.current_player}")

    def create_grid(self):
        for i in range(9):
            btn = tk.Button(
                self.window,
                text=" ",
                font=("Arial", 24),
                width=5,
                height=2,
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_click(self, index: int):
        if self.buttons[index]["state"] == "disabled":
            return
        make_move(self.board, index + 1, self.current_player)

        self.buttons[index].config(
            text=self.current_player,
            state="disabled"
        )

        winner = check_winner(self.board)
        if winner:
            messagebox.showinfo("Result", f"Engineer {winner} Wins!")
            self.disable_all_buttons()
            return

        if is_draw(self.board):
            messagebox.showinfo("Result", "Draw! Gridlock Achieved.")
            self.disable_all_buttons()
            return

        self.current_player = switch_player(self.current_player)
        self.create_turn_view()

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.board = create_board()
        self.current_player = "X"
        self.create_turn_view()
        for btn in self.buttons:
            btn.config(text=" ", state="normal", fg="black")

    def create_reset_button(self):
        reset_btn = tk.Button(
            self.window,
            text="Shield Reset",
            font=("Arial", 24),
            height=2,
            command=self.reset_game
        )
        reset_btn.grid(row=3, column=1, columnspan=2, sticky="we")


if __name__ == "__main__":
    Game_GUI()
