import pygame
pygame.init()

from scenes.menu import *
from scenes.help import *

screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Japan adventure")

background = pygame.image.load("assets/menu_background.png").convert()
background = pygame.transform.scale(background, (screen_width, screen_height)) # scale the background image to game dimensions

game_background = pygame.image.load("assets/levels/level1.png").convert()
game_background = pygame.transform.scale(game_background, (screen_width, screen_height)) # scale the background image to game dimensions

menu_screen = menu()
help_screen = help()

clock = pygame.time.Clock()

run = True
current_scene = "menu"
menu_option = None

while run:
    dt = clock.tick(60) # game runs 60fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # so game can quit
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_scene = "menu"
                menu_option = 0
        if current_scene == "menu":
            menu_option = menu_screen.menu_selection(event)

    if current_scene == "menu":
        screen.blit(background, (0, 0))
        menu_screen.draw_menu(screen)
        if menu_option == 0:
            current_scene = "game"
        elif menu_option == 1:
            current_scene = "help"
        elif menu_option == 2:
            current_scene = "settings"
        elif menu_option == 3:
            run = False
    elif current_scene == "game":
        screen.blit(game_background, (0, 0))
    elif current_scene == "help":
        screen.blit(background, (0, 0))
        help_screen.draw_help(screen)

    pygame.display.flip()
