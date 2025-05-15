import pygame as pg
from constants import *


def main():
    # init
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # logic

        # render
        screen.fill(pg.Color(0, 0, 0))

        pg.display.flip()

    # quit


if __name__ == "__main__":
    main()
