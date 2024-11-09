import pygame
import VectorMath
import Renderer
import TimeManager
import Physics
import Prefabs
import AINetworking

def game():

    # Define screen dimensions
    screen_width, screen_height = 1280, 720  # Updated resolution

    renderer = Renderer.Renderer((screen_width, screen_height))

    pygame.init()

    gameObjects = []  # this contains all gameobjects, do not store any permanent game objects anywhere else

    gameObjects.append(Prefabs.makePlayer()) # Creates the player Object
    #gameObjects.append(Prefabs.makePlayer())


    gameObjects.append(Prefabs.makeKillBox(VectorMath.Vector3(300,600,300),VectorMath.Vector3(20,5,3)))

    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(300,500,300),VectorMath.Vector3(100,100,3)))
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

def AIGame(networks): #pass in a list of AI networks, will return the score of each after method is over

    # Define screen dimensions
    screen_width, screen_height = 1280, 720  # Updated resolution

    renderer = Renderer.Renderer((screen_width, screen_height))

    pygame.init()

    gameObjects = []  # this contains all gameobjects, do not store any permanent game objects anywhere else

    for i in range(len(networks)):
        x = Prefabs.makePlayer(VectorMath.Vector3(150,150,0))
        x.addAINewtwork(networks[i])
        x.network.score = 0
        gameObjects.append(x) # Creates the player Object with network
    


    #gameObjects.append(Prefabs.makeKillBox(VectorMath.Vector3(400,150,300),VectorMath.Vector3(5,5,3)))

    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(600,650,300),VectorMath.Vector3(10,10,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(900,300,300),VectorMath.Vector3(3,20,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(360,355,300),VectorMath.Vector3(3,10,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(700,300,300),VectorMath.Vector3(40,3,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(000,000,300),VectorMath.Vector3(300,3,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(000,720,300),VectorMath.Vector3(300,3,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(000,0,300),VectorMath.Vector3(3,300,3)))
    gameObjects.append(Prefabs.makeBox(VectorMath.Vector3(1280,0,300),VectorMath.Vector3(3,300,3)))






    running = True  # AWAYS TRUE WHEN GAME IS RUNNING

    # Initialize Movement

    TimeManager.TimeTracker.setStartTime()
    while (running):

        PlayerList = [ob for ob in gameObjects if (ob.name == "Player")]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "STOP"
            
        for player in PlayerList:
            inputs = AINetworking.Network.getInputs(player.transform.position,gameObjects,player.rigidbody.velocity)
            movementNumber = player.network.calculateInput(inputs)
            moveDir = (movementNumber)
            #print(moveDir)
            # if (moveDir <= 7.8):
            #     player.controller.is_a_pressed = True
            #     player.controller.is_d_pressed = False
            #     player.controller.is_w_pressed = False
            #     player.controller.is_s_pressed = False
            # elif(moveDir <=8.1):
            #     player.controller.is_a_pressed = False
            #     player.controller.is_d_pressed = True
            #     player.controller.is_w_pressed = False
            #     player.controller.is_s_pressed = False
            # elif(moveDir <=8.4):
            #     player.controller.is_a_pressed = False
            #     player.controller.is_d_pressed = False
            #     player.controller.is_w_pressed = True
            #     player.controller.is_s_pressed = False
            # else:
            #     player.controller.is_a_pressed = False
            #     player.controller.is_d_pressed = False
            #     player.controller.is_w_pressed = False
            #     player.controller.is_s_pressed = True

            if (moveDir <= 6.5 or moveDir >= 8.5): player.controller.is_d_pressed = True
            else: player.controller.is_d_pressed = False
            if (6 <= moveDir <= 7.5): player.controller.is_s_pressed = True
            else:player.controller.is_s_pressed = False
            if(7.3 <= moveDir <= 8.3):  player.controller.is_a_pressed = True
            else: player.controller.is_a_pressed = False
            if(8.1<= moveDir): player.controller.is_w_pressed = True
            else: player.controller.is_w_pressed = False



        for player in PlayerList:
            acceleration = player.controller.get_acceleration()
            
            if acceleration.magnitude() > 0:
                Physics.addforce(player.rigidbody, acceleration)



        for player in PlayerList:
            Physics.update(player.rigidbody, TimeManager.TimeTracker.deltatime, screen_width, screen_height)
            player.network.setScore(player.transform.position)
        if (TimeManager.TimeTracker.timeSinceStart() > 17.5):
            running = False

        Physics.updateCollision(gameObjects)


        renderer.renderFrame(gameObjects)

        pygame.display.flip()

        TimeManager.TimeTracker.updateTime()
        

    
    pygame.quit()
    return [(player.network) for player in PlayerList]
    #Return a list of tuples, index 0 being the network, and index 1 being the score, lower score is better

