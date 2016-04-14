import pygame

class Board:

    SIZE = 8
    MOVE = ((0,0),(-1,0),(0,1),(1,0),(0,-1))

    def __init__(self, window, block_border=0, empty_piece_path='', black_piece_path='', white_piece_path='', cursor_piece_path=''):
        self.window = window
        if empty_piece_path:  self.ep = pygame.image.load(empty_piece_path)
        if black_piece_path:  self.bp = pygame.image.load(black_piece_path)
        if white_piece_path:  self.wp = pygame.image.load(white_piece_path)
        if cursor_piece_path: self.cp = pygame.image.load(cursor_piece_path)

        # Boader overlapping.
        self.block_size = (self.ep.get_width()-block_border, self.ep.get_height()-block_border)
        self.board_anchor = (self.window.width/10, self.window.height/10)
        self.board_state = [[0]*Board.SIZE for _ in range(Board.SIZE)]
        self.board_state[3][3] = self.board_state[4][4] = 1
        self.board_state[3][4] = self.board_state[4][3] = 2
        self.cursor = [3, 3]

    def update(self, keys):
        d = 0
        if keys[pygame.K_UP]: d = 1
        if keys[pygame.K_RIGHT]: d = 2
        if keys[pygame.K_DOWN]: d = 3
        if keys[pygame.K_LEFT]: d = 4
        nxt_cursor = [self.cursor[0]+Board.MOVE[d][0], self.cursor[1]+Board.MOVE[d][1]]
        if 0 <= nxt_cursor[0] < Board.SIZE and 0 <= nxt_cursor[1] < Board.SIZE:
            self.cursor = nxt_cursor
        if d != 0: return

        if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
            self.board_state[self.cursor[0]][self.cursor[1]] = 1

    def draw_self(self):
        self.window.draw_grid(self.board_anchor, self.block_size, self.board_state, (self.ep, self.bp, self.wp))
        self.window.draw_img(self.board_anchor, (self.block_size[0]*self.cursor[0], self.block_size[1]*self.cursor[1]), self.cp)
