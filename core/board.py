import pygame

from rule import Reversi

__all__ = ('Board', 'ScoreBoard')

class Board(object):

    MOVE = ((0,0),(-1,0),(0,1),(1,0),(0,-1))

    def __init__(self, window, player_number=2, height=0, width=0, block_border=0, pieces_path=(), cursor_piece_path=''):
        self.window = window
        self.player_number = player_number
        self.height = height
        self.width = width
        self.pieces = ()

        if pieces_path:
            self.pieces = tuple([pygame.image.load(pp) for pp in pieces_path if pp])
        if cursor_piece_path: self.cp = pygame.image.load(cursor_piece_path)

        # Boader overlapping.
        self.block_size = (self.pieces[0].get_height()-block_border, self.pieces[0].get_width()-block_border)
        self.anchor = (self.window.height/10, self.window.width/10)
        self.state = [[-1]*self.width for _ in range(self.height)]
        self.state[3][3] = self.state[4][4] = 0
        self.state[3][4] = self.state[4][3] = 1
        self.cursor = (3, 3)

        self.rule = Reversi(self.player_number, self.state)

    def count(self):
        cnt = [0]*self.player_number
        for i in range(self.height):
            for j in range(self.width):
                if self.state[i][j] != -1:
                    cnt[self.state[i][j]] += 1

        return cnt

    def update(self, keys):
        d = 0
        if keys[pygame.K_UP]: d = 1
        if keys[pygame.K_RIGHT]: d = 2
        if keys[pygame.K_DOWN]: d = 3
        if keys[pygame.K_LEFT]: d = 4
        nxt_cursor = tuple([self.cursor[0]+Board.MOVE[d][0], self.cursor[1]+Board.MOVE[d][1]])
        if 0 <= nxt_cursor[0] < self.height and 0 <= nxt_cursor[1] < self.width:
            self.cursor = nxt_cursor
        if d != 0: return

        if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
            if self.rule.is_valid(self.cursor):
              self.rule.shift(self.state, self.cursor)
              self.window.done_background = False

    def draw_self(self):
        self.window.draw_grid(self.anchor, self.block_size, self.state, self.pieces)
        self.window.draw_suface(self.anchor, (self.block_size[0]*self.cursor[0], self.block_size[1]*self.cursor[1]), self.cp)


class ScoreBoard(object):

    def __init__(self, window, player_number=2, pieces_path=(), board=None):
        self.window = window
        self.player_number = player_number
        self.pieces = ()
        self.board = board

        if pieces_path:
            self.pieces = tuple([pygame.image.load(pp) for pp in pieces_path if pp])
        self.anchor = (self.window.height/10, self.window.width/10*2+board.block_size[1]*board.width)

    def draw_self(self):
        loc, padding_lr = [0, 0], self.board.width/100
        self.window.draw_suface(self.anchor, tuple(loc), self.pieces[0])

        loc[1] += self.board.block_size[1]+padding_lr
        font = pygame.font.Font(None, 80)
        text = ' : '.join(map(str, self.board.count()))
        size = font.size(text)
        padding_tb = (self.board.block_size[0]-size[1])/2
        loc[0] += padding_tb
        ren = font.render(text, True, (0,0,0))
        self.window.draw_suface(self.anchor, tuple(loc), ren)
        loc[0] -= padding_tb

        loc[1] += size[0]+padding_lr
        self.window.draw_suface(self.anchor, tuple(loc), self.pieces[1])
