
class Settings():
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """ initialize game's settings"""

        # screen settings
        self.bg_color = (230, 230, 230)
        self.screen_width = 1200
        self.screen_height = 800

        # bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_limit = 5

        # player settings
        self.lives = 3
        self.score = 0

        # alien settings
        self.points = 10
        self.drop_speed = 10

        # wave settings
        self.wave_number = 1

        # difficulty settings
        self.difficulty_scale = float(1+self.wave_number*0.1)
