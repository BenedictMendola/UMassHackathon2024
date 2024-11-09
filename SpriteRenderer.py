import pygame

class SpriteRenderer:

    def __init__(self,imagePath: str):
        self.surface = pygame.image.load(imagePath)

    def setImage(self,imagePath: str):
        self.surface = pygame.image.load(imagePath)