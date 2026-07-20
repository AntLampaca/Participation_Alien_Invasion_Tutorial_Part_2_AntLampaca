import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
#from alien import Alien
from alien_fleet import AlienFleet

class AlienInvasion:
    """
    Main class that manages the game

    Initializes the pygame environment, creates the game window,
    handles the game loop, processes user input, and updates display.
    """
    def __init__(self):
        """
        Initializes the game, and creates all objects

        Sets up pygame, loads settings, creates the display window,
        loads background image, initializes game clock, and creates
        the player ship.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        #pygame.mixer.init()
        #self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        #self.laser_sound.set_volume(0,7)

        #self.impact = pygame.mixer.Sound(self.settings.impact)
        #self.impact.set_volume(0,7)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet (self)
        self.alien_fleet.create_fleet()
    
    def run_game(self):
        """
        Starts the main game loop

        checks for player input, updates game objects,
        refreshes the screen, and controls game fps
        """
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._reset_level()
            #subtract one life if possible

        #check collisions for projectiles and aliens
        if self.alien_fleet.check_fleet_bottom():
            self._reset_level()

        #check collisions for aliens bottom of screen
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        #if collisions
            #self.impact.play()
            #self.impact.fadeout(500)

    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self):
        """
        Updates the game display

        draws the background, renders game objects, and refreshes
        the game window
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self):
        """
        handles pygame events like key presses
        and quit game
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        Looks for keys being pressed

        controls ship movement, firing, and quiting the game
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire()
                #self.laser_sound.play()
                #self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """
        Looks for keys being not pressed anymore

        stops ship movent when a key is not pressed anymore
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()