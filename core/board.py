import pygame

class Board:

    def __init__(self, screen, block_border=0, empty_state_path='', black_piece_path='', white_piece_path=''):
        self.window = screen
        if empty_state_path: self.ep = pygame.image.load(empty_state_path)
        if black_piece_path: self.bp = pygame.image.load(black_piece_path)
        if white_piece_path: self.wp = pygame.image.load(white_piece_path)

        # Boader overlapping.
        self.block_size = (self.ep.get_width()-block_border, self.ep.get_height()-block_border)
        self.board_anchor = (self.window.width/10, self.window.height/10)
        self.board_state = [[0]*8 for _ in range(8)]
        self.board_state[3][3] = self.board_state[4][4] = 1
        self.board_state[3][4] = self.board_state[4][3] = 2

    def draw_self(self):
        self.window.draw_grid(self.board_anchor, self.block_size, self.board_state, (self.ep, self.bp, self.wp))
