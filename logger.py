import csv
from datetime import datetime
import os


LOG_FILE = "logs_shield.csv"


def board_to_string(board: list[str]) -> str:
    """
    Converts board list to a single string representation.
    Example: ['X','O',' ','X',...] -> 'XO X...'
    """
    return "".join(board)


def write_log(game_mode: str, winner: str, move_history: list[str], final_board: list[str]) -> None:
    """
    Writes a single game log entry to the CSV file.

    Columns:
    Timestamp, GameMode, Winner, MoveHistory, FinalBoard
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    moves = " | ".join(move_history)
    board_state = board_to_string(final_board)

    file_exists = os.path.isfile(LOG_FILE)

    try:
        with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write header only once
            if not file_exists:
                writer.writerow([
                    "Timestamp",
                    "GameMode",
                    "Winner",
                    "MoveHistory",
                    "FinalBoardState"
                ])

            writer.writerow([
                timestamp,
                game_mode,
                winner,
                moves,
                board_state
            ])

    except OSError as e:
        print("Log Error: Unable to write to log file.")
        print(f"System Message: {e}")
