import VectorMath
import GameObjects
import math
import TimeManager


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
    
def collsionForce(objectToMove):
    objectToMove.transform.position = VectorMath.Vector3(objectToMove.transform.position.x - objectToMove.rigidbody.velocity.x * TimeManager.TimeTracker.deltatime * 2,objectToMove.transform.position.y - objectToMove.rigidbody.velocity.y * 2* TimeManager.TimeTracker.deltatime,objectToMove.transform.position.z)
    objectToMove.rigidbody.velocity = VectorMath.Vector3(-objectToMove.rigidbody.velocity.x,-objectToMove.rigidbody.velocity.y,-objectToMove.rigidbody.velocity.z)
    
    #objectToMove.rigidbody.velocity = VectorMath.Vector3(0,0,0)


def collision(object1, object2):
    collision = False

    r = object1.sr.surface.get_width() * object1.transform.scale.x /2

    object2HalfWidth = object2.sr.surface.get_width() /2 * object2.transform.scale.x
    object2HalfHeight = object2.sr.surface.get_height() /2 * object2.transform.scale.y

    obj1Pos = object1.transform.position
    obj2Pos = object2.transform.position

    yOverlap = ((obj1Pos.y + r) > (obj2Pos.y - object2HalfHeight)) and (obj1Pos.y -r ) < (obj2Pos.y + object2HalfHeight)

    xOverlap = ((obj1Pos.x + r) > (obj2Pos.x - object2HalfWidth)) and (obj1Pos.x -r ) < (obj2Pos.x + object2HalfWidth)

    if(xOverlap and yOverlap):
        if(object2.name == "killBox"):
            object1.transform.position = VectorMath.Vector3(100,100,0)
            return
        collsionForce(object1)
    # print(f"radius = {r}")  
    # print(f"obj2 half width = {object2HalfWidth}")      
    # print(f"obj2 half hight = {object2HalfHeight}")        
    # print(collision)
        
        
def updateCollision(gameObjects):
    playerObject = None
    for ob in gameObjects:
        if ob.name == "Player":
            playerObject = ob
    for obj in gameObjects:
        if obj.name != 'Player':
            collision(playerObject,obj)
    
        
        
    
        
    
    
    