import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """a class to manage the bullets fired from the ship"""

    def __init__(self, settings, screen, ship):
        """initilizaes a bullet object and tracks the position on the screen"""
        super(Bullets, self).__init__()
        self.screen = screen

        # create bullet rectangle
        # create a rectangular bullet at 0,0
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        # move the bullet to the center/top of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullets position as a decimal value
        self.y = float(self.rect.y)

        # assign color to bullets
        self.color = settings.bullet_color

        # assign speed to bullets
        self.speed = settings.bullet_speed

    def update(self):
        """move the bullet up the screen"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
