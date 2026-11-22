import pygame
import os
from settings import *

class player():
    def __init__(self):
        self.idle_image = pygame.image.load("assets/player/idle.png")
        self.idle_image = pygame.transform.scale_by(self.idle_image, 2)

        self.walking_images = []
        self.floor_y = screen_height
        self.x = screen_width / 2
        self.y = self.floor_y

        self.walking_folder = os.listdir("assets/player/walking")
        for i in self.walking_folder:
            image = pygame.image.load(f"assets/player/walking/{i}")
            image = pygame.transform.scale_by(image, 2)
            self.walking_images.append(image)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.idle_image.get_width(), self.idle_image.get_height())

    def movement(self):
        pass
