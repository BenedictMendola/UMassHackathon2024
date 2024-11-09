import pygame


class SpriteRenderer:
    def __init__(self, sprite_path):
        self.surface = pygame.image.load(sprite_path)

    def setImage(self, imagePath: str):
        self.surface = pygame.image.load(imagePath)
