class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings self lifes
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 12.5
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly game speeds up
        self.speedup_scale = 2

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game. """
        self.ship_speed = 5.5
        self.bullet_speed = 8.0
        self.alien_speed = 2.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 2

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """ Increase speed settings and alien point values """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
