import sys
import pygame
from settings import Settings
from ship import Ship


class AlienAttack:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Alien Attack')
        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = (self.settings.bg_color)

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.ship.blitme()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienAttack()
    ai.start_game()