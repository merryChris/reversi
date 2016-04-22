__all__ = ('Reversi',)

class Rule(object):

    def __init__(self, player_number=2, height=0, width=0):
        self.player_number = player_number
        self.height = height
        self.width = width

        self.state = [[-1]*self.width for _ in range(self.height)]
        self.state[3][4] = self.state[4][3] = 0
        self.state[3][3] = self.state[4][4] = 1
        self.current_player = 0
        self.vacant = 0
        self.feasible_locations = None
        self._reset_feasible_locations()

    def _flip(self, loc):
        pass

    def _poll(self):
        self.current_player = (self.current_player+1) % self.player_number

    def _reset_feasible_locations(self):
        self.feasible_locations = set()

    def has_feasible_location(self):
        return True if self.feasible_locations else False

    def get_current_player(self):
        return self.current_player

    def get_feasible_locations(self):
        return self.feasible_locations

    def get_hashed_state(self):
        return ''.join([''.join(map(str, _)) for _ in self.state])

    def get_state(self):
        return self.state

    def get_vacant(self):
        return self.vacant

    def get_winner(self):
        cnt = self.count()
        max_val = max(cnt)

        if cnt.count(max_val) == self.player_number: return tuple(range(self.player_number),)
        return (cnt.index(max_val),)

    def count(self):
        cnt = [0]*self.player_number
        for i in range(self.height):
            for j in range(self.width):
                if self.state[i][j] != -1:
                    cnt[self.state[i][j]] += 1

        return cnt

    def validate_loc(self, loc=()):
        if not self.feasible_locations or not loc: return False

        return loc in self.feasible_locations

    def place(self, loc=()):
        if not loc: return

        self.state[loc[0]][loc[1]] = self.current_player

    def shift(self, loc=()):
        if self.has_feasible_location(): self._flip(loc)
        self._poll()
        self._reset_feasible_locations()
        if self.feasible_locations: self.vacant = 0
        else: self.vacant += 1


class Reversi(Rule):

    MOVE = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))

    def _flip(self, loc):
        if not loc: return

        for d in Reversi.MOVE:
            if self._is_feasible(loc, d):
                tx, ty = loc[0]+d[0], loc[1]+d[1]
                while 0<=tx<self.height and 0<=ty<self.width:
                    if self.state[tx][ty] == self.current_player: break
                    self.state[tx][ty] ^= 1
                    tx += d[0]
                    ty += d[1]

    def _reset_feasible_locations(self):
        super(Reversi, self)._reset_feasible_locations()

        for i in range(self.height):
            for j in range(self.width):
                if self.state[i][j] != -1: continue
                for md in Reversi.MOVE:
                    if self._is_feasible((i, j), md):
                        self.feasible_locations.add((i,j))
                        break

    def _is_feasible(self, loc, d):
        tx, ty, cnt = loc[0]+d[0], loc[1]+d[1], 0
        while 0<=tx<self.height and 0<=ty<self.width:
            if self.state[tx][ty] in (-1, self.current_player): break
            cnt += 1
            tx += d[0]
            ty += d[1]

        return 0<=tx<self.height and 0<=ty<self.width and self.state[tx][ty] == self.current_player and cnt>0
