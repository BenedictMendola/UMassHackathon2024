import pygame
import VectorMath
import Renderer
import GameObjects
import TimeManager
import Physics
import Movement

renderer = Renderer.Renderer((600, 800))


pygame.init()

gameObjects = (
    []
)  # this contains all gameobjects, do not store any permanent game objects anywhere else
ball = GameObjects.GameObject(VectorMath.Vector3(300, 300, 0))
ball.rigidbody = Physics.RigidBody(
    velocity=VectorMath.Vector3(0, 0, 0), mass=1, angularVelocity=0, game_object=ball
)
# ball.rigidbody.top_speed = 5  # Remove or comment out this line
gameObjects.append(ball)

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

    Physics.update(ball.rigidbody, TimeManager.TimeTracker.deltatime)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    renderer.renderFrame(gameObjects)

    pygame.display.flip()

    TimeManager.TimeTracker.updateTime()
    print(TimeManager.TimeTracker.deltatime)
pygame.quit()
