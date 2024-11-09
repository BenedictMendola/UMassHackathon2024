import Transform
import VectorMath
import SpriteRenderer

class GameObject():

    def __init__(self,positon = VectorMath.Vector3(0,0,0), rotation = 0, scale = VectorMath.Vector3(3,3,3), sprite = "Assets/RedCircle1.png"):
        self.transform = Transform.Transform(positon,rotation,scale)
        self.sr = SpriteRenderer.SpriteRenderer(sprite)

