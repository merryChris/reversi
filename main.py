from core import Window, Keyboard, Board


window = Window(1200, 800, 'Welcome to Reversi AI', 'resources/images/background_100x100.png')
keyboard = Keyboard()
board = Board(window, 1, 'resources/images/board_82x82_b1.png', \
                         'resources/images/black_82x82.png',    \
                         'resources/images/white_82x82.png',    \
                         'resources/images/cursor_82x82.png')

def main():
    window.draw_background()
    while True:
        if not keyboard.monitor(board.update):
            window.quit()
            break
        board.draw_self()
        window.update()

if __name__ == '__main__':
    main()
