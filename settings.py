class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings IB
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (15, 15, 15)

        # Ship settings self lifes IB
        self.ship_limit = 3

        # Bullet settings IB
        self.bullet_speed = 14.5
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 10

        # Alien settings IB
        self.fleet_drop_speed = 1
        self.spawn_chance = 30

        # How quickly game speeds up IB
        self.ship_speedup_scale = 1.1
        self.alien_speedup_scale = 1.2
        self.bullet_speedup_scale = 1.5
        self.spawn_chance_speedup_scale = 3

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game. """
        self.ship_speed = 5.5
        self.bullet_speed = 10.0
        self.alien_speed = 2.0

        # fleet_direction of 1 represents right; -1 represents left. IB
        # self.fleet_direction = 2

        # Scoring
        self.alien_points = 50
    # Speedup with higher level IB
    def increase_speed(self):
        """ Increase speed settings and alien point values """
        self.ship_speed *= self.ship_speedup_scale
        self.bullet_speed *= self.bullet_speedup_scale
        self.alien_speed *= self.alien_speedup_scale
        self.spawn_chance += self.spawn_chance_speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
