"""Simple CLI for Term Tac Toe

A very simple CLI that simply let's a user optionally set the board size and
run the game.
"""


import sys

from .tui import TUI
from .game import DEFAULT_BOARD_SIZE


def main(board_size=DEFAULT_BOARD_SIZE):
    # Try updating board size from the first positional command line arg
    try:
        board_size = int(sys.argv[1])

    # If no arg provided or is not an int, fall back to default
    except (IndexError, ValueError):
        pass

    TUI(board_size)


if __name__ == "__main__":
    main()
