import pygame as pg
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_angle = random.uniform(20, 50)

        split1 = Asteroid(self.position.x, self.position.y, split_radius)
        split1.velocity = self.velocity.rotate(split_angle) * 1.2
        split2 = Asteroid(self.position.x, self.position.y, split_radius)
        split2.velocity = self.velocity.rotate(-split_angle) * 1.2

    def draw(self, screen):
        pg.draw.circle(screen, pg.Color(255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
