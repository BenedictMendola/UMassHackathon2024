import pygame
import VectorMath


class Movement:
    def __init__(self, accel_amount=0.5):
        self.xdir = 0  # -1 for left, 1 for right
        self.ydir = 0  # -1 for up, 1 for down
        self.accel_amount = accel_amount

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.ydir = -1
            elif event.key == pygame.K_a:
                self.xdir = -1
            elif event.key == pygame.K_s:
                self.ydir = 1
            elif event.key == pygame.K_d:
                self.xdir = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                self.ydir = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                self.xdir = 0

    def get_acceleration(self):
        acceleration = VectorMath.Vector3(
            self.xdir * self.accel_amount, self.ydir * self.accel_amount, 0
        )
        return acceleration
