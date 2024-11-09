import pygame
import VectorMath
import Renderer
import TimeManager
import Physics
import Prefabs

def game():

    # Define screen dimensions
    screen_width, screen_height = 1280, 720  # Updated resolution

    renderer = Renderer.Renderer((screen_width, screen_height))

    pygame.init()

    gameObjects = []  # this contains all gameobjects, do not store any permanent game objects anywhere else

    gameObjects.append(Prefabs.makePlayer()) # Creates the player Object
    gameObjects.append(Prefabs.makePlayer(position=VectorMath.Vector3(150,150,200)))


    gameObjects.append(Prefabs.makeKillBox(VectorMath.Vector3(300,600,300),VectorMath.Vector3(20,5,3)))

    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(300,300,300),VectorMath.Vector3(10,10,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(500,300,300),VectorMath.Vector3(3,20,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(900,300,300),VectorMath.Vector3(50,3,3)))






    running = True  # AWAYS TRUE WHEN GAME IS RUNNING

    # Initialize Movement


    while running:

        PlayerList = [ob for ob in gameObjects if (ob.name == "Player")]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                for player in PlayerList:
                    player.controller.handle_event(event)
                #movement.handle_event(event)  # Handle movement events


        for player in PlayerList:
            acceleration = player.controller.get_acceleration()
            
            if acceleration.magnitude() > 0:
                Physics.addforce(player.rigidbody, acceleration)

        # acceleration = movement.get_acceleration()

        # if acceleration.magnitude() > 0:
        #     Physics.addforce(gameObjects[0].rigidbody, acceleration)

        for player in PlayerList:
            Physics.update(player.rigidbody, TimeManager.TimeTracker.deltatime, screen_width, screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Physics.updateCollision(gameObjects)


        renderer.renderFrame(gameObjects)

        pygame.display.flip()

        TimeManager.TimeTracker.updateTime()
        
        
    pygame.quit()


game() # TURN OFF WHEN USING AI