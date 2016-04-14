import pygame

class Window:

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

    def draw_background(self):
        if not self.bgp: return

        self.window.fill(0)
        for i in xrange((self.width+self.bgpw-1)/self.bgpw):
            for j in xrange((self.height+self.bgph-1)/self.bgph):
                self.window.blit(self.bgp, (i * self.bgpw, j * self.bgph))

        self.update()
        self.done_background = True

    """ Should be included in a loop. """
    def draw_grid(self, anchor=(0,0), block=(0,0), grid=[[]], img=()):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                loc = (anchor[0]+i*block[0], anchor[1]+j*block[1])[::-1]
                self.window.blit(img[0], loc)
                if grid[i][j] != 0: self.window.blit(img[grid[i][j]], loc)

    def draw_img(self, anchor=(0,0), pos=(0,0), img=None):
        loc = (anchor[0]+pos[0], anchor[1]+pos[1])[::-1]
        if img: self.window.blit(img, loc)


class Keyboard:

    RANGE = 400

    def __init__(self):
        # ASCII VALUE RANGE
        self.keys = [False] * Keyboard.RANGE

    def monitor(self, onkeydown_callback=None):
        event = pygame.event.poll()
        if event.type == pygame.QUIT: return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: return False
            self.keys[event.key] = True
            if onkeydown_callback: onkeydown_callback(self.keys)
            self.keys[event.key] = False

        return True
