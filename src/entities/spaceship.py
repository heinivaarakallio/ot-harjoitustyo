import pygame
import os

dirname = os.path.dirname(__file__)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "spaceship.png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
