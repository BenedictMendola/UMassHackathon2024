import Transform
import VectorMath
import SpriteRenderer
import Physics


class GameObject:

    def __init__(
        self,
        position=VectorMath.Vector3(0, 0, 0),
        rotation=0,
        scale=VectorMath.Vector3(3, 3, 3),
        sprite="Assets/RedCircle1.png",
    ):
        self.transform = Transform.Transform(position, rotation, scale)
        self.sr = SpriteRenderer.SpriteRenderer(sprite)
        self.rigidbody = Physics.RigidBody(
            velocity=VectorMath.Vector3(0, 0, 0),
            mass=1,
            angularVelocity=0,
            game_object=self,
        )
