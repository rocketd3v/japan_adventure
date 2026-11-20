import os
import random
from settings import *
import math
import pygame

class leaves():
    def __init__(self):
        self.leaf_images = []
        self.leaves = []

        for i in os.listdir("assets/weather/leaves"):
            image = pygame.image.load(os.path.join("assets/weather/leaves", i))
            self.leaf_images.append(image)

        for i in range(1, 20):
            self.leaves.append(self.create_leaf())  

    def create_leaf(self):
        leaf = {
        "x": random.randint(0, screen_width),
        "y": 0,
        "speed": random.randint(1, 5),
        "wind_effect": random.randint(1, 3),
        "image": random.choice(self.leaf_images),
        }
        return leaf

    def update(self, screen):
        for leaf in self.leaves:
            leaf["y"] += leaf["speed"]
            leaf["x"] += math.cos(leaf["wind_effect"]) # uses cosine wave for natural sway
            leaf["wind_effect"] += 0.03

            if leaf["y"] >= screen_height or leaf["x"] >= screen_width: 
                leaf["y"] = 0
                leaf["x"] = random.randint(0, screen_width)
        

           
            screen.blit(leaf["image"], (leaf["x"], leaf["y"]))
