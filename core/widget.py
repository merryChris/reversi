import time, pygame

__all__ = ('Window', 'Keyboard')

class Window(object):

    def __init__(self, width, height, title='', background_image_path=''):
        pygame.init()

        self.width, self.height, self.title = width, height, title
        if self.width and self.height:
            self.window = pygame.display.set_mode((self.width, self.height))
            if self.title: pygame.display.set_caption(self.title)

        if background_image_path:
            self.bgp = pygame.image.load(background_image_path)
            self.bgpw, self.bgph = self.bgp.get_width(), self.bgp.get_height()

        self.done_background = False

    def update(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()

    def reset_background(self):
        self.done_background = False

    def draw_background(self):
        if not self.bgp: return

        self.window.fill(0)
        for i in xrange((self.width+self.bgpw-1)/self.bgpw):
            for j in xrange((self.height+self.bgph-1)/self.bgph):
                self.window.blit(self.bgp, (i * self.bgpw, j * self.bgph))

        self.update()
        self.done_background = True

    """ Should be included in a loop. """
    def draw_suface(self, anchor=(0,0), pos=(0,0), suface=None):
        loc = (anchor[0]+pos[0], anchor[1]+pos[1])[::-1]
        if suface: self.window.blit(suface, loc)

    def draw_grid(self, anchor=(0,0), block=(0,0), grid=[[]], suface=()):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                loc = (anchor[0]+i*block[0], anchor[1]+j*block[1])[::-1]
                self.window.blit(suface[-1], loc)
                if grid[i][j] != -1: self.window.blit(suface[grid[i][j]], loc)


class Keyboard(object):

    RANGE = 400

    def __init__(self):
        # ASCII VALUE RANGE
        self.keys = [False] * Keyboard.RANGE

    def monitor(self, onkeydown_callback=None, always_callback=None):
        event = pygame.event.poll()
        if event.type == pygame.QUIT: return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: return False
            self.keys[event.key] = True
            if onkeydown_callback: onkeydown_callback(self.keys)
            self.keys[event.key] = False

        always_callback()
        return True

class Timer(object):

    def sleep(self, second=2):
        time.sleep(second)
