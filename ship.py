import pygame


class Ship():

    def __init__(self, screen):
        self.screen = screen

        # load image of ship and access image data
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

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
        if self.rotate_clockwise:
            self.angle_rotation -= 1
            self.blitRotate()
        elif self.rotate_counterclockwise:
            self.angle_rotation += 1
            self.blitRotate()

        # update rect from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitRotate(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle_rotation)
        # self.rect = rotated_image.get_rect()

        self.screen.blit(rotated_image, self.rect)



"""
### the following is experimental to rotate the ship
    def blitRotate(self, screen, pos, originPos, angle):
        # offset from pivot to center
        #bimage_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - self.rect.center

        # rotated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle_rotation)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # rotate and blit the image
        surf.blit(rotated_image, rotated_image_rect)

        # draw rectangle around the image
        pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()), 2)


def blitRotate2(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)


try:
    image = pygame.image.load('AirPlaneFront.png')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
    image = pygame.Surface((text.get_width() + 1, text.get_height() + 1))
    pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
    image.blit(text, (1, 1))
w, h = image.get_size()

angle = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width() / 2, screen.get_height() / 2)

    screen.fill(0)
    blitRotate(screen, image, pos, (w / 2, h / 2), angle)
    # blitRotate2(screen, image, pos, angle)
    angle += 1

    pygame.display.flip()

pygame.quit()
exit()
"""
