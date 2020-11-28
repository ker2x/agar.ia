import pygame
from pygame.locals import *
import time
import random
import numpy


class Agaria:
    def __init__(self, rendering = True):
        self.rendering = rendering
        self.start_time = time.time()
        self.screen_size = (800,600)
        self.background_color = (255,255,255)
        self.is_running = True
        if self.rendering:
            pygame.init()
            self.screen = pygame.display.set_mode(self.screen_size, pygame.DOUBLEBUF | pygame.RESIZABLE)
            pygame.display.set_caption("Agar.IA")

        self.setup()
        self.loop()

    def setup(self):
        pass

    def loop(self):
        while self.is_running:
            self.update()
            if self.rendering:
                self.render()
            pass

    def update(self):
        pass

    def render(self):
        for e in pygame.event.get():
            if e.type == pygame.VIDEORESIZE:
                self.screen_size = self.screen.get_size()
            if e.type == pygame.QUIT:
                self.quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.quit()

        if self.is_running:
            self.screen.fill(self.background_color)
            # game logic
            pygame.display.flip()
        else:
            raise RuntimeError("Render was called while self.is_running == False")

    def quit(self):
        self.is_running = False
        print("Game ended after %s seconds." % int(time.time() - self.start_time))
        pygame.quit()
        quit(0)

    # ---- IA SPECIFIC BELOW ----
    def observation(self, player):
        pass

    def reward(self, player):
        pass

    def done(self, player):
        pass

    def info(self, player):
        pass

    def new_player(self):
        pass