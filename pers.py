from dataclasses import dataclass

import pygame

from config import POINTS


@dataclass(frozen=True)
class GameConfig:
    width: int = 100
    height: int = 60
    initial_x: int = 465
    initial_y: int = 605


class Pers:
    def __init__(
        self,
        window: pygame.Surface,
        image_path: str,
        number: int = 0,
        config: GameConfig = GameConfig(),
    ):
        self.window = window
        self.number = number
        self.config = config

        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(
            image,
            (config.width, config.height),
        )

        self.rect = self.image.get_rect(
            center=(
                config.initial_x + 100 * number,
                config.initial_y,
            )
        )

        self.cur_point = -1

    def move(self, direction: int) -> None:
        self.cur_point = max(
            0,
            min(self.cur_point + direction, len(POINTS) - 1),
        )

        self.rect.center = POINTS[self.cur_point]

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            self.move(1)

        elif event.key == pygame.K_DOWN:
            self.move(-1)

    def draw(self) -> None:
        self.window.blit(self.image, self.rect)
