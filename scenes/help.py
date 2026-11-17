import pygame
pygame.init()

from settings import *

class help():
    def __init__(self):
        self.content = ["Use WAD and arrow keys to move", "", "Storyline (can be found in readme)", "you're a stray cat who always used to be petted by a child on their", "way to school.", "one day they dissapear,", "but you discover that they've left clues for you", "to find them, so every day non-stop for 84 days you beat every level", "and on the end of day 84, you finally reunite with the child", "and the parents allow the child to adopt you,", "Completing more levels gives you a higher chance", "of the child's parents", "taking you in"]

        self.title_font = pygame.font.Font(font, 70)
        self.menu_font = pygame.font.Font(font, 20)

        self.title_surface = self.title_font.render("Help", True, black)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.centerx = screen_width / 2
        self.title_rect.centery = 50

    def draw_help(self, screen):
        screen.blit(self.title_surface, self.title_rect)

        for i in range(len(self.content)):
            content_surface = self.menu_font.render(self.content[i], True, black)

            content_rect = content_surface.get_rect()
            content_rect.centerx = 500
            content_rect.centery = 250 + (i * 30)

            screen.blit(content_surface, content_rect)
