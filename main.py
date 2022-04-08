# import pygame and system features
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


# define main game function
def alien_invasion():
    # initialize pygame library
    pygame.init()
    # access settings
    settings = Settings()
    # create a display by inputting  width and height of screen
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # names the displayed screen
    pygame.display.set_caption('Alien Invasion')
    # make a player ship
    ship = Ship(screen)

    # make a group to store bullets in
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings, screen,ship, aliens)

    # loop to start animation
    while True:

        # access event handler from game_functions
        gf.check_events(settings, screen, ship, bullets)
        # updates the screen from game_functions
        gf.update_screen(settings, screen, ship, bullets, aliens)



alien_invasion()
