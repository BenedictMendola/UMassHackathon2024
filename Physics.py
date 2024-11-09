import VectorMath
import GameObjects
import math


class RigidBody:
    def __init__(self, velocity, mass, angularVelocity, game_object):
        self.velocity = velocity
        self.mass = mass
        self.angularVelocity = angularVelocity
        self.game_object = game_object


def addforce(rb, force):
    rb.velocity = rb.velocity + force


def update(rb, delta_time, screen_width, screen_height):
    displacement = rb.velocity.scale(delta_time)
    rb.game_object.transform.position = rb.game_object.transform.position + displacement
    rb.velocity = rb.velocity.scale(0.75)  # Reduced damping from 0.99 to 0.75

    # Wrap around horizontally
    if rb.game_object.transform.position.x < 0:
        rb.game_object.transform.position.x += screen_width
    elif rb.game_object.transform.position.x > screen_width:
        rb.game_object.transform.position.x -= screen_width

    # Wrap around vertically
    if rb.game_object.transform.position.y < 0:
        rb.game_object.transform.position.y += screen_height
    elif rb.game_object.transform.position.y > screen_height:
        rb.game_object.transform.position.y -= screen_height

class Collider:
    def __init__(self, upper, lower, left, right, r=0):
        self.upper = upper
        self.lower = lower
        self.left = left
        self.right = right
        self.r = r
    
    
def collision(object1, object2):
    collision = False
    # above 
    if object1.transform.position.y < object2.transform.position.y + object2.collider.upper:
        if (math.sqrt((object1.transform.position.y)**2 + (object2.transform.position.y + object2.collider.upper)**2)):
            collision = True
    elif object1.transform.position.y > object2.transform.position.y - object2.collider.lower:
        if (math.sqrt((object1.transform.position.y)**2 + (object2.transform.position.y + object2.collider.upper)**2)):
            collision = True
    elif object1.transform.position.x < object2.transform.position.x + object2.collider.right:
        if (math.sqrt((object1.transform.position.x)**2 + (object2.transform.position.x + object2.collider.right)**2)):
            collision = True
    elif object1.game_object.transform.position.x > object2.game_object.transform.position.x - object2.collider.left:
        if (math.sqrt((object1.transform.position.x)**2 + (object2.transform.position.x + object2.collider.left)**2)):
            collision = True
            
    print(collision)
        
        
def updateCollision():
    pass
    
        
        
    
        
    
    
    