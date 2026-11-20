import pygame

from config import WINDOW_HEIGHT, WINDOW_WIDTH
from pers import Pers


class Renderer:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.scene = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background = pygame.transform.scale(
            pygame.image.load("assets/map_2.png").convert(),
            (WINDOW_WIDTH, WINDOW_HEIGHT),
        )
        self.font = pygame.font.SysFont("Arial", 32)

    def draw(
        self,
        persons: list[Pers],
        active_pers: int,
        number_input: str,
    ) -> None:
        self.scene.blit(self.background, (0, 0))

        for person in persons:
            person.draw()

        self.draw_active_person(persons[active_pers])
        self.draw_number_input(number_input)

        self.window.fill((0, 0, 0))

        scale = self.window.get_width() / WINDOW_WIDTH

        scaled_height = int(WINDOW_HEIGHT * scale)

        scaled_scene = pygame.transform.scale(
            self.scene,
            (self.window.get_width(), scaled_height),
        )

        y = (self.window.get_height() - scaled_height) // 2

        self.window.blit(scaled_scene, (0, y))

        pygame.display.flip()

    def draw_active_person(self, person: Pers) -> None:
        icon_size = 100
        padding = 20

        x = self.scene.get_width() - icon_size - padding - 20
        y = padding

        background = pygame.Rect(
            x,
            y,
            icon_size + 20,
            icon_size + 20,
        )

        pygame.draw.rect(
            self.scene,
            (40, 40, 40),
            background,
            border_radius=12,
        )

        icon = pygame.transform.scale(
            person.image,
            (icon_size, icon_size),
        )

        self.scene.blit(icon, (x + 10, y + 10))

    def draw_number_input(self, number: str) -> None:
        if not number:
            return

        text = self.font.render(
            f"Номер: {number}",
            True,
            (255, 255, 255),
        )

        background = pygame.Rect(160, 20, 180, 60)

        pygame.draw.rect(
            self.scene,
            (40, 40, 40),
            background,
            border_radius=12,
        )

        self.scene.blit(text, (175, 32))

    def window_to_scene(
        self,
        position: tuple[int, int],
    ) -> tuple[int, int] | None:
        scale = self.window.get_width() / WINDOW_WIDTH

        y_offset = (self.window.get_height() - WINDOW_HEIGHT * scale) / 2

        x = position[0] / scale
        y = (position[1] - y_offset) / scale

        if not (0 <= x < WINDOW_WIDTH and 0 <= y < WINDOW_HEIGHT):
            return None

        return int(x), int(y)
