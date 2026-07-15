import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import AlienInvasion

class Bullet(Sprite):
    """
    class for the bullet being fired by the player ship

    handles bullet png, postition, movement and rendering on the game screen
    """
    def __init__(self, game: 'AlienInvasion'):
        """
        Initializes a bullet

        creates the bullet image, positions it at the top of the players ship,
        and stores the position of the bullet
        """
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings
        
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """
        responsible for the bullet movement
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draws bullet on screen using its current position
        """
        self.screen.blit(self.image, self.rect)