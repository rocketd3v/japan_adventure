import pygame
import os
from settings import *

class player:
    def __init__(self):
        self.idle_image = pygame.image.load("assets/player/idle.png").convert_alpha()
        self.idle_image = pygame.transform.scale_by(self.idle_image, 2)

        self.walking_images = []
        self.walking_folder = sorted(os.listdir("assets/player/walking"))

        for i in self.walking_folder:
            image = pygame.image.load(f"assets/player/walking/{i}").convert_alpha()
            image = pygame.transform.scale_by(image, 2)
            self.walking_images.append(image)

        self.floor_y = screen_height - self.idle_image.get_height()
        self.x = screen_width / 2
        self.y = self.floor_y
        self.speed = 5
        self.jump_strength = 13
        self.velocity_y = 0
        self.gravity = 0.5
        self.facing = "left"

        self.image = self.idle_image
        self.animation_i = 0
        self.animation_timer = 0
        self.animation_speed = 180

    def rect(self):
        return pygame.Rect(round(self.x), round(self.y), self.idle_image.get_width(), self.idle_image.get_height())

    def movement(self, dt):
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed * dt / 16.67
            self.facing = "left"
            moving = True

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed * dt / 16.67
            self.facing = "right"
            moving = True

        if (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]) and self.y >= self.floor_y:
            self.velocity_y = -self.jump_strength

        self.velocity_y += self.gravity * dt / 16.67
        self.y += self.velocity_y * dt / 16.67

        if self.y >= self.floor_y:
            self.y = self.floor_y
            self.velocity_y = 0

        if moving and self.walking_images:
            self.animation_timer += dt

            if self.animation_timer >= self.animation_speed:
                self.animation_i = (self.animation_i + 1) % len(self.walking_images)
                self.animation_timer -= self.animation_speed

            self.image = self.walking_images[self.animation_i]
        else:
            self.image = self.idle_image
            self.animation_i = 0
            self.animation_timer = 0

        if self.facing == "right":
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
