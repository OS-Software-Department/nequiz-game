from dataclasses import dataclass

import pygame


@dataclass(frozen=True)
class GameConfig:
    width: int = 100
    height: int = 60
    initial_x: int = 465
    initial_y: int = 605
    movement_delay: int = 100


POINTS = [
    (160, 668),
    (98, 540),
    (249, 500),
    (314, 376),
    (415, 340),
    (560, 361),
    (647, 272),
    (736, 200),
    (845, 176),
    (951, 212),
    (1055, 272),
    (1179, 201),
    (1279, 315),
    (1398, 214),
    (1500, 287),
    (1478, 476),
    (1581, 554),
    (1704, 465),
    (1812, 519),
    (1805, 748),
    (1679, 717),
    (1623, 852),
    (1541, 881),
    (1459, 955),
    (1324, 953),
    (1228, 878),
    (1209, 710),
    (1102, 656),
    (979, 657),
    (939, 818),
    (859, 872),
    (770, 925),
    (635, 944),
    (511, 885),
    (428, 811),
    (352, 772),
    (240, 764),
]


class Pers:
    def __init__(
        self,
        window: pygame.Surface,
        image_path: str = "images/bear.png",
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
        self.last_move = 0

    def move(self, direction: int) -> None:
        self.cur_point = max(
            0,
            min(self.cur_point + direction, len(POINTS) - 1),
        )

        self.rect.center = POINTS[self.cur_point]

    def handle_event(self, event: pygame.event.Event, active: bool) -> None:
        if not active or event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            self.move(1)

        elif event.key == pygame.K_DOWN:
            self.move(-1)

    def draw(self) -> None:
        self.window.blit(self.image, self.rect)
