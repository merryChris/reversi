import random

__all__ = ('Reversi')

class Rule(object):

    def __init__(self, player_number=2, board=[]):
        self.player_number = player_number
        self.current_player = 0
        self.feasible_locations = None
        self._reset_feasible_locations(board)

    def _flip(self, board, loc):
        self.current_player = (self.current_player+1) % self.player_number

    def _reset_feasible_locations(self, board):
        self.feasible_locations = set()

    def has_feasible_location(self):
        return True if self.feasible_locations else False

    def is_valid(self, loc=()):
        if not self.feasible_locations or not loc: return False

        return loc in self.feasible_locations

    def get_current_player(self):
        return self.current_player

    def shift(self, board=[], loc=()):
        self._flip(board, loc)
        self._reset_feasible_locations(board)


class Reversi(Rule):

    MOVE = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))

    def _flip(self, board, loc):
        if loc:
            board[loc[0]][loc[1]] = self.current_player
            for d in Reversi.MOVE:
                if self._is_feasible(board, loc, d):
                    tx, ty = loc[0]+d[0], loc[1]+d[1]
                    while 0<=tx<len(board) and 0<=ty<len(board[0]):
                        if board[tx][ty] == self.current_player: break
                        board[tx][ty] ^= 1
                        tx += d[0]
                        ty += d[1]

        super(Reversi, self)._flip(board, loc)

    def _reset_feasible_locations(self, board):
        super(Reversi, self)._reset_feasible_locations(board)

        if not board: return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != -1: continue
                for md in Reversi.MOVE:
                    if self._is_feasible(board, (i, j), md):
                        self.feasible_locations.add((i,j))
                        break

    def _is_feasible(self, board, loc, d):
        tx, ty, cnt = loc[0]+d[0], loc[1]+d[1], 0
        while 0<=tx<len(board) and 0<=ty<len(board[0]):
            if board[tx][ty] in (-1, self.current_player): break
            cnt += 1
            tx += d[0]
            ty += d[1]

        return 0<=tx<len(board) and 0<=ty<len(board[0]) and board[tx][ty] == self.current_player and cnt>0

    def select(self):
        return random.choice(list(self.feasible_locations))
