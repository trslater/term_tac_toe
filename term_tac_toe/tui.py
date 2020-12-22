"""TUI for Term Tac Toe

Handles the basic TUI (Terminal User Interface) actions for the game, including
the game loop (input, draw).
"""


import curses

from .game import Game, DEFAULT_BOARD_SIZE


KEY_SPACEBAR = ord(' ')


class TUI:
    def __init__(self, board_size=DEFAULT_BOARD_SIZE):
        self.board_size = board_size
        self.game = Game(self.board_size)

        curses.wrapper(self.game_loop, self.game)

    def game_loop(self, stdscr, game):
        self.stdscr = stdscr

        self.draw()
        while self.get_input():
            self.draw()

    def get_input(self):
        # Try getting key press
        try:
            key = self.stdscr.getch()

        except KeyboardInterrupt:
            return False

        # Route key actions
        if key == curses.KEY_LEFT:
            self.game.board.cursor.left()

        elif key == curses.KEY_RIGHT:
            self.game.board.cursor.right()

        elif key == curses.KEY_UP:
            self.game.board.cursor.up()

        elif key == curses.KEY_DOWN:
            self.game.board.cursor.down()

        elif key == KEY_SPACEBAR:
            # If someone has won
            if self.game.winner:
                self.game.reset()

            # No one has won yet
            else:
                # If square taken successfully
                if self.game.take():
                    # Check if current player has won
                    self.game.check_win()
                    # Advance to next player
                    self.game.next_player()

        # If everything went fine
        return True

    def draw(self):
        # Clear the screen
        self.stdscr.clear()
        # Add the drawn game as string to screen
        self.stdscr.addstr(self.game.draw())
