import pygame
from settings import *

background = "assets/levels/level_select.png"

class level_select():
    def __init__(self):
        self.levels = {
            "Tutorial": (100, 200),
            "Park": (300 , 100)
                       }
        self.selected_level = 0
        self.level_rects = []
        self.text = pygame.font.Font(font, 20)
        self.background = pygame.image.load(background).convert()
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        
    def keyboard_navigate(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if self.selected_level != len(self.levels) - 1:
                    self.selected_level += 1
                else:
                    self.selected_level = 0
            elif event.key == pygame.K_LEFT:
                if self.selected_level != 0:
                    self.selected_level -= 1
                else:
                    self.selected_level = len(self.levels) - 1

    def mouse_select(self, event):
        index = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for rect in self.level_rects:
                if rect.collidepoint(mouse_pos):
                    self.selected_level = index

                index += 1

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.level_rects = []
        index = 0

        for level, position in self.levels.items():
            if  index == self.selected_level:
                text_surface = self.text.render(level, True, pink)
                text_rect = text_surface.get_rect()
            else:
                text_surface = self.text.render(level, True, black)
                text_rect = text_surface.get_rect()

            x, y = position
            text_rect.centerx = x
            text_rect.centery = y
            screen.blit(text_surface, text_rect)
            self.level_rects.append(text_rect)
            index += 1

