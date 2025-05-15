# ruff: noqa
import sys
import pygame as pg
import player as pl
import shot as sh
import asteroid as ast
import asteroidfield as fld
from constants import *


def main():
    # init
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    pl.Player.containers = (updatable, drawable)
    ast.Asteroid.containers = (asteroids, updatable, drawable)
    fld.AsteroidField.containers = updatable
    sh.Shot.containers = (shots, updatable, drawable)

    player = pl.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = fld.AsteroidField()

    dt = 0
    while True:
        # input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # logic
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.colliding(asteroid):
                    shot.kill()
                    asteroid.kill()

        # render
        screen.fill(pg.Color(0, 0, 0))
        for item in drawable:
            item.draw(screen)

        pg.display.flip()

        dt = clock.tick(60) / 1000

    # quit
    pg.quit()


if __name__ == "__main__":
    main()
