import math

class Vector3():
    def __init__(self,x:int,y:int,z:int):
        self.x = x
        self.y = y
        self.z = z
    
    def normalized(self):
        mag = self.magnitude()
        return Vector3(self.x/mag,self.y/mag,self.z/mag)

    def magnitude(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2),10)
        