import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid_1 = self.velocity.rotate(random_angle)
        asteroid_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_obj_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_obj_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_obj_1.velocity = asteroid_1 * 1.2
        asteroid_obj_2.velocity = asteroid_2 * 1.2
