import pygame
import VectorMath
import Renderer
import GameObjects
import TimeManager
import Physics
import Movement

# Define screen dimensions
screen_width, screen_height = 1280, 720  # Updated resolution

renderer = Renderer.Renderer((screen_width, screen_height))

pygame.init()

gameObjects = (
    []
)  # this contains all gameobjects, do not store any permanent game objects anywhere else
ball = GameObjects.GameObject(VectorMath.Vector3(300, 300, 0), name='Player')
ball.rigidbody = Physics.RigidBody(
    velocity=VectorMath.Vector3(0, 0, 0), mass=1, angularVelocity=0, game_object=ball
)
# ball.rigidbody.top_speed = 5  # Remove or comment out this line
ball.addCollider(r= ball.sr.surface.get_height()/2)
gameObjects.append(ball)


# testing collision stuff
obstacle1 = GameObjects.GameObject(VectorMath.Vector3(500, 500, 0), name='Player', sprite="Assets/Rectangle.png")
obstacle1.rigidbody = Physics.RigidBody(
    velocity=VectorMath.Vector3(0, 0, 0), mass=1, angularVelocity=0, game_object=obstacle1
)

obstacle1.addCollider(upper=obstacle1.sr.surface.get_height()/2)
obstacle1.addCollider(left=obstacle1.sr.surface.get_width()/2)
gameObjects.append(obstacle1)

# obstacle1.addCollider(2,2,2,2) # random bullshit for now



clock = pygame.time.Clock()
running = True  # AWAYS TRUE WHEN GAME IS RUNNING

# Initialize Movement
movement = Movement.Movement()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            movement.handle_event(event)  # Handle movement events

    acceleration = movement.get_acceleration()

    if acceleration.magnitude() > 0:
        Physics.addforce(ball.rigidbody, acceleration)

    Physics.update(
        ball.rigidbody, TimeManager.TimeTracker.deltatime, screen_width, screen_height
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    renderer.renderFrame(gameObjects)

    pygame.display.flip()

    TimeManager.TimeTracker.updateTime()
    
    Physics.collision(ball, obstacle1)
pygame.quit()
