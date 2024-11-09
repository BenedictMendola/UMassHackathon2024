import VectorMath

class Transform():
    
    def __init__(self,postion:VectorMath.Vector3,rotation: int, scale:VectorMath.Vector3):
        self.position = postion
        self.rotation = rotation
        self.scale = scale