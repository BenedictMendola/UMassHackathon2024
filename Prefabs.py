import GameObjects
import VectorMath
import Physics

def makePlayer(position = VectorMath.Vector3(100,100,0),name = "Player", velocity = VectorMath.Vector3(0,0,0),mass = 1,angularV = 0):
    player = GameObjects.GameObject(position,name=name)
    player.rigidbody = Physics.RigidBody(velocity,mass,angularV,player)
    player.addCollider(r= player.sr.surface.get_height()/2)
    player.addPlayerController()
    return player

def makeKillBox(positon = VectorMath.Vector3(0,0,0),scale = VectorMath.Vector3(3,3,3)):
    killBox = GameObjects.GameObject(positon,name = "killBox", sprite="Assets/Rectangle1.png",scale=scale)
    killBox.rigidbody = Physics.RigidBody(velocity=VectorMath.Vector3(0, 0, 0), mass=1, angularVelocity=0, game_object=killBox)
    killBox.addCollider(upper=killBox.sr.surface.get_height()/2)
    killBox.addCollider(left=killBox.sr.surface.get_width()/2)
    return killBox

def makeBox(positon = VectorMath.Vector3(0,0,0),scale = VectorMath.Vector3(3,3,3)):
    Box = GameObjects.GameObject(positon, sprite="Assets/Rectangle.png",scale=scale)
    Box.rigidbody = Physics.RigidBody(velocity=VectorMath.Vector3(0, 0, 0), mass=1, angularVelocity=0, game_object=Box)
    Box.addCollider(upper=Box.sr.surface.get_height()/2)
    Box.addCollider(left=Box.sr.surface.get_width()/2)
    return Box