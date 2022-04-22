import pygame
import sys
from bullets import Bullets
from aliens import Alien


def check_events(settings, screen, ship, bullets):
    """ checks for key/mouse events and responds"""
    # loop to check keypress events
    for event in pygame.event.get():
        # if escape key pressed, exit game
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            keyup_event(event, ship)


def keydown_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
    if event.key == pygame.K_q:
        ship.rotate_counterclockwise = True
    if event.key == pygame.K_e:
        ship.rotate_clockwise = True
    if event.key == pygame.K_SPACE and len(bullets) < settings.bullet_limit:
        new_bullet = Bullets(settings, screen, ship)
        bullets.add(new_bullet)
    if event.key == pygame.K_ESCAPE:
        print("Score:", str(settings.score))
        sys.exit()



def keyup_event(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False
    if event.key == pygame.K_q:
        ship.rotate_counterclockwise = False
    if event.key == pygame.K_e:
        ship.rotate_clockwise = False


def create_fleet(settings, screen, ship, aliens):
    """create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_of_aliens(settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x/(2*alien_width))
    return number_of_aliens


def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height - (3 * alien_height * settings.difficulty_scale) - ship_height
    number_of_rows = int(available_space_y/(2*alien_height))
    return number_of_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create and alien and place it on a row"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def update_fleet(settings, aliens):
    for alien in aliens:
        alien.direction = alien.direction * -1
        alien.rect.y += settings.alien_drop_speed


def update_aliens(settings,screen, ship, aliens):
    # draw fleet of aliens
    aliens.draw(screen)
    aliens.update()

    for alien in aliens:
        if alien.check_screen():
            update_fleet(settings, aliens)
            break

    new_wave(settings, screen, ship, aliens)
    alien_invasion(settings, aliens)

def check_collision(settings, bullets, aliens):
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        settings.score += int(settings.points)


def check_end(settings, screen, ship, aliens):
    if pygame.sprite.spritecollideany(ship, aliens):
        aliens.empty()
        settings.lives -= 1
        if settings.lives > 0:
            new_wave(settings, screen, ship, aliens)
        else:
            print("Game Over. Your score is", settings.score)


def alien_invasion(settings, aliens):
    for alien in aliens:
        if alien.rect.bottom > settings.screen_height:
            settings.score -= int(settings.points*len(aliens)/2)
            alien.empty()
            break


def update_bullets(bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        bullet.update()
        if bullet.rect.bottom < 0:
            bullet.kill()


def new_wave(settings, screen, ship, aliens):
    if len(aliens) == 0:
        create_fleet(settings, screen, ship, aliens)
        increase_difficulty(settings)


def increase_difficulty(settings):
    settings.wave_number += 1
    settings.alien_speed *= settings.difficulty_scale
    settings.alien_drop_speed += 1 * settings.difficulty_scale
    settings.points *= settings.difficulty_scale
    settings.scale *= 0.96


def update_screen(settings, screen, ship, bullets, aliens):
    # color the screen with background color
    screen.fill(settings.bg_color)

    update_aliens(settings,screen, ship, aliens)
    alien_invasion(settings, aliens)

    # draw new bullets on the screen; move bullets
    update_bullets(bullets)

    # update the ship
    ship.update()
    # draw the ship on the screen
    ship.blitme()

    check_collision(settings, bullets, aliens)

    check_end(settings, screen, ship, aliens)

    # update the display
    pygame.display.flip()
