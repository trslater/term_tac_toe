"""Term Tac Toe Business Logic

This is the actual game mechanics.
"""


from itertools import cycle


DEFAULT_BOARD_SIZE = 3


class Game:
    def __init__(self, board_size=DEFAULT_BOARD_SIZE):
        self.board = Board(board_size)
        self.players = cycle(('X', 'O'))
        self.curr_player = self.first_player = next(self.players)
        self.winner = None

    def take(self):
        if self.board.cursor.empty():
            self.board.cursor.value = self.curr_player
            return True

        return False

    def next_player(self):
        self.curr_player = next(self.players)

    def check_win(self):
        # Check rows
        for y, row in enumerate(self.board):
            self.winner = self.curr_player

            for x, square in enumerate(row):
                if square != self.curr_player:
                    self.winner = None
                    break

            if self.winner:
                return

        # Check cols
        for x in range(self.board.size):
            self.winner = self.curr_player

            for y, row in enumerate(self.board):
                if self.board[y][x] != self.curr_player:
                    self.winner = None
                    break

            if self.winner:
                return

        # Check forward diagonal
        self.winner = self.curr_player
        for i in range(self.board.size):
            if self.board[i][i] != self.curr_player:
                self.winner = None
                break

        if self.winner:
            return

        # Check backward diagonal
        self.winner = self.curr_player
        for i in range(self.board.size):
            if self.board[i][self.board.size-i-1] != self.curr_player:
                self.winner = None
                break

    def reset(self):
        while self.curr_player != self.first_player:
            self.next_player()

        self.winner = None
        self.board.clear()

    def draw(self):
        return (
            f"{self.board.draw()}\n"
            f"Current player: {self.curr_player}\n"
            f"Winner: {self.winner}")


class Board:
    def __init__(self, size=DEFAULT_BOARD_SIZE):
        self.size = size
        self.clear()
        self.cursor = Cursor(self)

    def clear(self):
        self.squares = [[' ']*self.size for _ in range(self.size)]

    def __getitem__(self, query):
        return self.squares[query]

    def draw(self):
        return f"\n{'+'.join(['-'*3]*self.size)}\n".join(
            "|".join(
                f"({square})"
                if (x, y) == self.cursor.to_tuple()
                else f" {square} "
                for x, square in enumerate(row))
            for y, row in enumerate(self.squares))


class Cursor:
    def __init__(self, board):
        self.board = board
        self.x_max = self.board.size - 1
        self.y_max = self.board.size - 1

        self._x = 0
        self._y = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        if new_x < 0:
            new_x = 0

        if new_x > self.x_max:
            new_x = self.x_max

        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        if new_y < 0:
            new_y = 0

        if new_y > self.y_max:
            new_y = self.y_max

        self._y = new_y

    @property
    def value(self):
        return self.board[self.y][self.x]

    @value.setter
    def value(self, value):
        self.board[self.y][self.x] = value

    def empty(self):
        return self.value == ' '

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1

    def to_tuple(self):
        return (self.x, self.y)
