# ruff: noqa
import pygame as pg
from constants import *


def main():
    # init
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    while True:
        # input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # logic

        # render
        screen.fill(pg.Color(0, 0, 0))

        pg.display.flip()

        dt = clock.tick(60) / 1000

    # quit
    pg.quit()


if __name__ == "__main__":
    main()
