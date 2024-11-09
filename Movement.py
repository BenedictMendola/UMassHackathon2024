import pygame
import VectorMath


class Movement:
    def __init__(self, accel_amount=100):  # Increased from 0.5 to 100
        # Track individual key states
        self.is_a_pressed = False  # Track 'A' key
        self.is_d_pressed = False  # Track 'D' key
        self.is_w_pressed = False  # Track 'W' key
        self.is_s_pressed = False  # Track 'S' key
        self.accel_amount = accel_amount

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.is_w_pressed = True
            elif event.key == pygame.K_a:
                self.is_a_pressed = True
            elif event.key == pygame.K_s:
                self.is_s_pressed = True
            elif event.key == pygame.K_d:
                self.is_d_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.is_w_pressed = False
            elif event.key == pygame.K_a:
                self.is_a_pressed = False
            elif event.key == pygame.K_s:
                self.is_s_pressed = False
            elif event.key == pygame.K_d:
                self.is_d_pressed = False

    def get_acceleration(self):
        # Determine direction based on key states
        xdir = (1 if self.is_d_pressed else 0) - (1 if self.is_a_pressed else 0)
        ydir = (1 if self.is_s_pressed else 0) - (1 if self.is_w_pressed else 0)

        acceleration = VectorMath.Vector3(
            xdir * self.accel_amount, ydir * self.accel_amount, 0
        )
        return acceleration
