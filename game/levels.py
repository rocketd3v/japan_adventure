import pygame
import os
from settings import *

levels = os.listdir("assets/levels")
levels.remove("level_select.png")
levels.sort()

class level():
    def __init__(self):
        self.level_images = []

        for file in levels:
            image = pygame.image.load(os.path.join("assets/levels", file)).convert()
            image = pygame.transform.scale(image, (screen_width, screen_height))
            self.level_images.append(image)

    def draw_level(self, level, screen):
        image = self.level_images[level]
        screen.blit(image, (0, 0))
