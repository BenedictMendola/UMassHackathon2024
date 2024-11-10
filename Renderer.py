import pygame


class Renderer:

    def __init__(self, screenSize: tuple):
        self.screenSize = screenSize
        self.screen = pygame.display.set_mode(screenSize)
        self.backgroundColor = pygame.Color(250, 250, 250)

    def renderFrame(self, objects: list):
        self.screen.fill(self.backgroundColor)

        for object in objects:
            if object.sr != None:
                objectSurface = object.sr.surface
                objectSurface = pygame.transform.scale(
                    objectSurface,
                    (
                        objectSurface.get_width() * object.transform.scale.x,
                        objectSurface.get_height() * object.transform.scale.y,
                    ),
                )

                # this is the topright conner of the sprite, subtract half the hight and width
                xPlacement = object.transform.position.x - objectSurface.get_width() / 2
                yPlacement = (
                    object.transform.position.y - objectSurface.get_height() / 2
                )

                self.screen.blit(objectSurface, (xPlacement, yPlacement))
