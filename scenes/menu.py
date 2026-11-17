import pygame
pygame.init()

from settings import *

class menu():
    def __init__(self):
        self.options = ["1 Play", "2 Help", "3 Settings", "4 Quit"]
        self.option = 0

        self.title_font = pygame.font.Font(font, 70)
        self.menu_font = pygame.font.Font(font, 40)

        self.title_surface = self.title_font.render("Menu", True, gray)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.centerx = screen_width / 2
        self.title_rect.centery = 50

    def menu_selection(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:   
                self.option -=1
                if self.option < 0:
                    self.option = len(self.options) - 1
            elif event.key == pygame.K_DOWN or event.key == pygame.K_TAB:
                self.option += 1
                if self.option >= len(self.options):
                    self.option = 0
            elif event.key == pygame.K_1:
                self.option = 0
            elif event.key == pygame.K_2:
                self.option = 1
            elif event.key == pygame.K_3:
                self.option = 2
            elif event.key == pygame.K_4:
                self.option = 3
            elif event.key == pygame.K_RETURN:
                return self.option

    def draw_menu(self, screen):
        screen.blit(self.title_surface, self.title_rect)

        for i in range(len(self.options)):
            if i == self.option:
                option_surface = self.menu_font.render(f"> {self.options[i]}", True, gray)
            else:
                option_surface = self.menu_font.render(self.options[i], True, black)

            option_rect = option_surface.get_rect()
            option_rect.centerx = 500
            option_rect.centery = 250 + (i * 60)

            screen.blit(option_surface, option_rect)

    def draw_decor(self, screen):
        pass
