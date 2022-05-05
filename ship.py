import pygame


class Ship():

    def __init__(self, screen):
        self.screen = screen

        # load image of ship and access image data
        self.image = pygame.image.load('images/xwing_pixel.png')
        self.image = pygame.transform.scale(self.image, (85, 75))

        # tells computer to interpret self.image as a rectangle
        self.rect = self.image.get_rect()
        # tells computer to interpret the screen as a rectangle
        self.screen_rect = screen.get_rect()

        # set starting location of each ship
        # makes the center x value of the ship the same as the center x valule of the screen
        self.rect.centerx = self.screen_rect.centerx
        # makes sthe bottom of the ship the same as the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom

        # stores center x and y of ship as a decimal value
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # create movement flags to determine if the ship is moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.rotate_clockwise = False
        self.rotate_counterclockwise = False
        self.angle_rotation = 0

    def blitme(self):
        """ draw the ship on the screen"""
        # image.blit(image being added, location)
        self.screen.blit(self.image, self.rect)

    def rotate_ship(self):
        pass

    def update(self):
        """ updates image of ship left/right"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += 1.5
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= 1.5
        if self.moving_up and self.rect.top > 0:
            self.centery -= 1.5
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 1.5
        """
        if self.rotate_clockwise:
            self.angle_rotation -= 1
            self.blitRotate()
        elif self.rotate_counterclockwise:
            self.angle_rotation += 1
            self.blitRotate()
        """

        # update rect from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # stores center x and y of ship as a decimal value
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitRotate(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle_rotation)
        # self.rect = rotated_image.get_rect()

        self.screen.blit(rotated_image, self.rect)
