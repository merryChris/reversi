import pygame

class Screen:

    def __init__(self, width, height, title='', background_image_path=''):
        pygame.init()

        self.width, self.height, self.title = width, height, title
        if self.width and self.height:
            self.screen = pygame.display.set_mode((self.width, self.height))
            if self.title: pygame.display.set_caption(self.title)

        if background_image_path:
            self.bgp = pygame.image.load(background_image_path)
            self.bgpw, self.bgph = self.bgp.get_width(), self.bgp.get_height()

        self.done_background = False

    def update(self):
        pygame.display.flip()

    def draw_background(self):
        if not self.bgp: return

        self.screen.fill(0)
        for i in xrange((self.width+self.bgpw-1)/self.bgpw):
            for j in xrange((self.height+self.bgph-1)/self.bgph):
                self.screen.blit(self.bgp, (i * self.bgpw, j * self.bgph))

        self.update()
        self.done_background = True

    """ Should be included in a loop. """
    def draw_grid(self, anchor=(0,0), block=(0,0), grid=[[]], img=()):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                pos = (anchor[0]+i*block[0], anchor[1]+j*block[1])
                self.screen.blit(img[0], pos)
                if grid[i][j] != 0: self.screen.blit(img[grid[i][j]], pos)
