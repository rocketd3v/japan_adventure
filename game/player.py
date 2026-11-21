import pygame
from settings import *
import os

class player():
    def __init__(self):
        self.walking_folder = "assets/player/walking"
        self.walking_frames = len(os.listdir(self.walking_folder))
        self.idle_image = pygame.image.load("assets/player/idle.png")
        self.idle_image = pygame.transform.scale_by(self.idle_image, 2)
        self.walking_images = []

        for i in range(1, self.walking_frames):
            image = pygame.image.load(f"assets/player/walking/walk{i}.png") #.convert_alpha()
            self.walking_images.append(image)

        self.jump_sound = ""

        self.x = screen_width / 2
        self.y =screen_height
        self.floor_y = screen_height
        self.on_floor = True
        self.gravity = 9.81

        self.moving = False
        self.moving_left = False
        self.moving_right = False
        self.facing_left = True

        self.animation_i = 0
        self.animation_timer = 0 
        self.animation_speed = 30

    
        

    
