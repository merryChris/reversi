__all__ = ('Reversi')

class Rule(object):

    def __init__(self, player_number=2):
        self.player_number = player_number
        self.current_player = 0
        self.feasible_locations = {}

    def _flip(self, board, loc):
        self.current_player = (self.current_player+1) % self.player_number

    def _reset_feasible_locations(self, board):
        self.feasible_location = {}

    def is_valid(self, loc=()):
        if not loc: return False

        return loc not in self.feasible_locations

    def shift(self, board=[], loc=()):
        if not board or not loc: return

        board[loc[0]][loc[1]] = self.current_player
        self._flip(board, loc)
        self._reset_feasible_locations(board)


class Reversi(Rule):

    def _flip(self, board, loc):
        super(Reversi, self)._flip(board, loc)

    def _reset_feasible_locations(self, board):
        super(Reversi, self)._reset_feasible_locations(board)
