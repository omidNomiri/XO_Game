def create_board() -> list[str]:
    """
    Creates and returns an empty 3x3 board represented as a list of 9 elements.
    """
    return [" " for _ in range(9)]


def grid_display(board: list[str]) -> None:
    """
    Displays the current board state in console using | and - characters.
    """
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def is_valid_move(board: list[str], move: int) -> bool:
    """
    Checks if the selected move is valid:
    - Must be in range 1-9
    - Target cell must be empty
    """
    if move < 1 or move > 9:
        return False
    return board[move - 1] == " "


def make_move(board: list[str], move: int, player: str) -> None:
    """
    Places the player's symbol (X or O) on the board.
    """
    board[move - 1] = player


def check_winner(board: list[str]):
    """
    Checks all 8 winning conditions.
    Returns 'X' or 'O' if there is a winner, otherwise None.
    """
    winning_combinations = [
        (0, 1, 2),  # rows
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # columns
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # diagonals
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def is_draw(board: list[str]) -> bool:
    """
    Checks if the board is full and there is no winner.
    """
    return " " not in board


def switch_player(current_player: str) -> str:
    """
    Switches turn between X and O.
    """
    if current_player == "X":
        return "O"
    return "X"

if __name__ == "__main__":
    board = create_board()
    grid_display(board)

    make_move(board, 5, "X")
    make_move(board, 1, "O")
    grid_display(board)

    print(check_winner(board))
