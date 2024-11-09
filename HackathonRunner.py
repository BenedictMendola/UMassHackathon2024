import pygame
import VectorMath
import Renderer
import GameObjects
import TimeManager

renderer = Renderer.Renderer((600,800))


pygame.init()

gameObjects = [] # this contains all gameobjects, do not store any permanent game objects anywhere else
gameObjects.append(GameObjects.GameObject(VectorMath.Vector3(300,300,0)))

clock = pygame.time.Clock()
running = True # AWAYS TRUE WHEN GAME IS RUNNING



while running:





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    renderer.renderFrame(gameObjects)

    pygame.display.flip()

    TimeManager.TimeTracker.updateTime()
    print(TimeManager.TimeTracker.deltatime)
pygame.quit()
