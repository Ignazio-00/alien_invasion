import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        
        # Define Alien types IB
        self.alien_health = 1
        randint_random = randint(0, 100)
        if randint_random <= 20:
            self.alien_health = 3
        elif randint_random >= 21 and randint_random <= 51:
            self.alien_health = 2

        # Load the alien image and set its rect attribute IB
        self.update_image()
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)


        # Update image dependend on health IB
    
    def update_image(self):
        '''Update image dependent on health'''
        if self.alien_health == 1:
            self.image = pygame.image.load("images/assets/pixel_ship_green_small.png")
        elif self.alien_health == 2:
            self.image = pygame.image.load("images/assets/pixel_ship_blue_small.png")
        elif self.alien_health == 3:
            self.image = pygame.image.load("images/assets/pixel_ship_red_small.png")

    # IB
    def update(self):
        """Move alien right or left."""
        # self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        # self.rect.x = self.x
        self.rect.y += self.settings.fleet_drop_speed
        
    # No use because no check needed for edges IB
    #def check_edges(self):
        #"""Return True if alien is at the edge of the screen."""
        #screen_rect = self.screen.get_rect()
        #if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            #return True
