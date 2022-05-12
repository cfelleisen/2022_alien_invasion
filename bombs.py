import pygame
from pygame.sprite import Sprite


class Bombs(Sprite):
    """a class to manage the bombs fired from the ship"""

    def __init__(self, settings, screen, alien):
        """initilizaes a bullet object and tracks the position on the screen"""
        super(Bombs, self).__init__()
        self.screen = screen

        # create bullet rectangle
        # create a rectangular bullet at 0,0
        self.rect = pygame.Rect(0,0, settings.bomb_width, settings.bomb_height)
        # move the bullet to the center/top of the ship
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        # store the bullets position as a decimal value
        self.y = float(self.rect.y)

        # assign color to bullets
        self.color = settings.bomb_color

        # assign speed to bullets
        self.speed = settings.bomb_speed

    def update(self):
        """move the bullet up the screen"""
        self.y += self.speed
        self.rect.y = self.y

    def draw_bomb(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
