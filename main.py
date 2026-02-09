from game_logic import (
    create_board,
    grid_display,
    is_valid_move,
    make_move,
    check_winner,
    is_draw,
    switch_player,
)
from ai_engine import get_smart_move
from logger import write_log
import gui


def get_player_move(player: str) -> int:
    while True:
        try:
            move = int(input(f"Engineer {player}, select a cell (1-9): "))
            return move
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")


def play_game(mode: str):
    guide_board = [str(i) for i in range(1, 10)]
    board = create_board()
    current_player = "X"
    move_history: list[str] = []
    move = 5

    print("guide board")
    grid_display(guide_board)
    while True:

        if mode == "PvP":
            move = get_player_move(current_player)

        elif mode == "PvAI":
            if current_player == "X":
                move = get_player_move("X")
            else:
                move = get_smart_move(board, "O", "X")

        elif mode == "AIvsAI":
            if current_player == "X":
                move = get_smart_move(board, "X", "O")
            else:
                move = get_smart_move(board, "O", "X")

        if not is_valid_move(board, move):
            print("Invalid move. Try again.")
            continue

        make_move(board, move, current_player)
        move_history.append(f"{current_player}>-{move}")

        winner = check_winner(board)
        if winner:
            grid_display(board)
            print(f"Winner: {winner}")
            write_log(mode, winner, move_history, board)
            return

        if is_draw(board):
            grid_display(board)
            print("Draw!")
            write_log(mode, "Draw", move_history, board)
            return

        current_player = switch_player(current_player)

        grid_display(board)


def main_menu():
    print("=" * 40)
    print("   XO Game")
    print("=" * 40)
    print("1. Player vs Player (PvP)")
    print("2. Player vs AI (PvAI)")
    print("3. AI vs AI")
    print("4. Launch GUI")
    print("0. Exit")
    print("=" * 40)

    while True:
        choice = input("Select mode: ")

        if choice == "1":
            play_game("PvP")
        elif choice == "2":
            play_game("PvAI")
        elif choice == "3":
            play_game("AIvsAI")
        elif choice == "4":
            gui.Game_GUI()
        elif choice == "0":
            print("System Shutdown.")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main_menu()
