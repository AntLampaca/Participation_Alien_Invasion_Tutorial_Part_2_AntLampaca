from pathlib import Path
class Settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'game_images' / 'background.png'

        self.ship_file = Path.cwd() / 'game_images' / 'player.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5