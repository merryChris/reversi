from core import Window, Keyboard, Board, ScoreBoard

window = Window(1200, 800, 'Welcome to Reversi AI', 'resources/images/background_100x100.png')
keyboard = Keyboard()
board = Board(window, 2, [0], ['Black', 'White'], 8, 8, 1, ('resources/images/black_82x82.png',              \
              'resources/images/white_82x82.png', 'resources/images/board_82x82_b1.png'),                    \
              'resources/images/cursor_82x82.png')
scoreboard = ScoreBoard(window, 2, board, ('resources/images/black_82x82.png',                               \
                        'resources/images/white_82x82.png', 'resources/images/background_100x100.png'))

def main():
    while True:
        if not keyboard.monitor(onkeydown_callback=board.update, always_callback=board.check):
            window.quit()
            break

        if board.need_ai():
            board.action_itself()
        if not window.done_background:
            window.draw_background()
            scoreboard.update()
            scoreboard.draw_self()
        board.draw_self()
        window.update()

if __name__ == '__main__':
    main()
