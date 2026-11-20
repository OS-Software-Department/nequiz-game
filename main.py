import pygame

from config import WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH
from game import Game


def main() -> None:
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(WINDOW_TITLE)

    game = Game(window)
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
