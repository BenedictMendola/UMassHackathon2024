import math


class Vector3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def normalized(self):
        mag = self.magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def magnitude(self):
        return round(math.sqrt(self.x**2 + self.y**2 + self.z**2), 10)

    def scale(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self


def addVector(v1: Vector3, v2: Vector3):
    return Vector3(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
