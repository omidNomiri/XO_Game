import random
from game_logic import check_winner, is_valid_move, make_move


def get_empty_cells(board: list[str]) -> list[int]:
    """
    Returns a list of empty cell indices (1-9).
    """
    return [i + 1 for i in range(9) if board[i] == ' ']


def get_random_move(board: list[str]) -> int:
    """
    Random AI: selects a random empty cell.
    """
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)


def find_winning_move(board: list[str], player: str):
    """
    Checks if the player can win in the next move.
    Returns the winning move (1-9) if exists, otherwise None.
    """
    for move in get_empty_cells(board):
        temp_board = board.copy()
        make_move(temp_board, move, player)
        if check_winner(temp_board) == player:
            return move
    return None


def get_smart_move(board: list[str], ai_player: str, opponent_player: str) -> int:
    """
    Smart AI decision-making based on priority:
    1. Win if possible
    2. Block opponent's win
    3. Take center
    4. Take corner or random empty cell
    """

    winning_move = find_winning_move(board, ai_player)
    if winning_move:
        return winning_move

    block_move = find_winning_move(board, opponent_player)
    if block_move:
        return block_move

    if is_valid_move(board, 5):
        return 5

    corners = [1, 3, 7, 9]
    available_corners = [c for c in corners if is_valid_move(board, c)]
    if available_corners:
        return random.choice(available_corners)

    return get_random_move(board)
