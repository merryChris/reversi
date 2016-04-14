from pygame.locals import *

from core import Screen, Board


screen = Screen(1200, 800, 'Welcome to Reversi', 'resources/images/background_100x100.png')
board = Board(screen, 1, 'resources/images/board_82x82_b1.png', \
                         'resources/images/black_82x82.png',    \
                         'resources/images/white_82x82.png')

def main():
    screen.draw_background()
    while True:
        board.draw_self()
        screen.update()

if __name__ == '__main__':
    main()
