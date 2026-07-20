import pygame
from typing import TYPE_CHECKING
from settings import Settings

if TYPE_CHECKING:
    from main import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """
    class for the player ship

    handles, ship png, movement, position and drawing
    """
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """
        Initializes the player ship

        gets game instance containg settings and display data
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """
        Updates the ship postition and arsenal
        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        Updates the ship horizontal movement

        makes the ship move right or left, and also keeps it in the screen width
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """
        Draws the ship and its bullets on the screen.

        Renders arsenal(bullets) first, then display the ship image
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """
        fires a bullet from the ship

        returns the bullet object created by arsenal
        """
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        """
        checks for collisions for the ship sprite
        """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False