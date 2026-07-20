from pathlib import Path
class Settings:
    """
    Stores values for the alien invasion game

    contains game window, fps, game images, ship properties and bullet behavior
    """
    def __init__(self):
        """
        Initializes all game settings

        defines most game values, for screen size, fps, ship movement, and laser behavior
        """
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'game_images' / 'background.png'

        self.ship_file = Path.cwd() / 'game_images' / 'player.png'
        self.ship_w = 64
        self.ship_h = 64
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'game_images' / 'laser_red.png'
        #will add later self.laser_sound = Path.cwd() /
        #will add later self.impact_sound = Path.cwd() /
        self.bullet_speed = 7
        self.bullet_w = 32
        self.bullet_h = 64
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'game_images' / 'alien.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 32