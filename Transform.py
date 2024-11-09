import VectorMath


class Transform:

    def __init__(
        self, position: VectorMath.Vector3, rotation: int, scale: VectorMath.Vector3
    ):
        self.position = position
        self.rotation = rotation
        self.scale = scale
