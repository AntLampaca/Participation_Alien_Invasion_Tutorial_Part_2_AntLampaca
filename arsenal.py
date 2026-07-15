import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import AlienInvasion

class Arsenal:
    """
    class manages the players bullets

    creates bullets, updates their movement and removes them
    """
    def __init__(self, game: 'AlienInvasion'):
        """
        Initializes the arsenal
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """
        Updates all active bullets

        moves bullets, and removes them offscreen
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """
        removes the bullets that went offscreen
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """
        Draws all bullets on screen

        calls bullet drawing method to render it
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """
        Creates and fires a new bullet
        if there is less bullets than specified in the settings (normally 5)
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False