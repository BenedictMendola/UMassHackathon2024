import pygame
import VectorMath

vectorCool = VectorMath.Vector3(5,3,2)
print(vectorCool.normalized().magnitude())

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
