import pygame
import asyncio
pygame.init()

from scenes.menu import *
from scenes.help import *
from game.weather import *
from game.player import *
from scenes.level_select import *
from game.levels import *

screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Japan adventure")

background = pygame.image.load("assets/menu_background.png").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

game_background = pygame.image.load("assets/levels/level0.png").convert()
game_background = pygame.transform.scale(game_background, (screen_width, screen_height))

menu = menu()
help = help()
leaves = leaves()
player = player()
level_select = level_select()
clock = pygame.time.Clock()
level = level()

run = True
current_scene = "menu"
menu_option = None

async def main():
    global run, current_scene, menu_option
    selected_level = 0

    while run:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_scene = "menu"
                    menu_option = None
            if current_scene == "menu":
                menu_option = menu.menu_selection(event)
                mouse_option = menu.mouse_selection(event)
                if mouse_option is not None:
                    menu_option = mouse_option
            elif current_scene == "level_select":
                keyboard_option = level_select.keyboard_navigate(event)
                mouse_option = level_select.mouse_select(event)
                if keyboard_option != None:
                    selected_level = keyboard_option
                    current_scene = "game"
                if mouse_option != None:
                    selected_level = mouse_option
                    current_scene = "game"

        if current_scene == "menu":
            screen.blit(background, (0, 0))
            menu.draw_menu(screen)
            leaves.update(screen)
            if menu_option == 0:
                current_scene = "level_select"
                menu_option = None
            elif menu_option == 1:
                current_scene = "help"
                menu_option = None
            elif menu_option == 2:
                current_scene = "settings"
                menu_option = None
            elif menu_option == 3:
                run = False
        elif current_scene == "level_select":
            level_select.draw(screen)
        elif current_scene == "game":
            level.draw_level(selected_level, screen)
            player.movement(dt)
            player.draw(screen)
        elif current_scene == "help":
            screen.blit(background, (0, 0))
            help.draw_help(screen)
        pygame.display.flip()
        await asyncio.sleep(0)


asyncio.run(main())
