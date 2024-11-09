import VectorMath


class RigidBody:
    def __init__(self, velocity, mass, angularVelocity, game_object):
        self.velocity = velocity
        self.mass = mass
        self.angularVelocity = angularVelocity
        self.game_object = game_object


def addforce(rb, force):
    rb.velocity = rb.velocity + force


def update(rb, delta_time):
    displacement = rb.velocity.scale(delta_time)
    rb.game_object.transform.position = rb.game_object.transform.position + displacement
    rb.velocity = rb.velocity.scale(0.5)  # Reduced damping from 0.99 to 0.999
