import pygame

from config import PERSONS
from pers import Pers
from renderer import Renderer


class Game:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.renderer = Renderer(window)

        self.persons = [
            Pers(
                self.renderer.scene,
                image_path=f"assets/players/{name}.png",
                number=i,
            )
            for i, name in enumerate(PERSONS)
        ]

        self.active_pers = 0
        self.number_input = ""
        self.running = True

    def select_person(self, number: int) -> None:
        if 0 <= number < len(self.persons):
            self.active_pers = number

    def handle_number_input(self, key: int) -> None:
        if pygame.K_0 <= key <= pygame.K_9:
            digit = str(key - pygame.K_0)

            if self.number_input == "":
                if digit == "1":
                    self.number_input = digit
                else:
                    self.select_person(int(digit))

            elif self.number_input == "1":
                if digit in ("0", "1"):
                    self.select_person(int("1" + digit))
                    self.number_input = ""
                else:
                    self.number_input = ""

        elif key == pygame.K_BACKSPACE:
            self.number_input = self.number_input[:-1]

        elif key == pygame.K_RETURN:
            if self.number_input:
                self.select_person(int(self.number_input))
                self.number_input = ""

        elif key == pygame.K_ESCAPE:
            self.number_input = ""

    def handle_mouse_click(self, position: tuple[int, int]) -> None:
        position = self.renderer.window_to_scene(position)

        if position is None:
            return

        self.number_input = ""

        for i, person in enumerate(self.persons):
            if person.rect.collidepoint(position):
                self.select_person(i)
            return

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.KEYDOWN:
            if pygame.K_0 <= event.key <= pygame.K_9:
                self.handle_number_input(event.key)
                return

            if event.key in (
                pygame.K_BACKSPACE,
                pygame.K_RETURN,
                pygame.K_ESCAPE,
            ):
                self.handle_number_input(event.key)
                return

            if self.number_input:
                self.handle_number_input(pygame.K_RETURN)

            self.persons[self.active_pers].handle_event(event)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handle_mouse_click(event.pos)

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.renderer.draw(
                self.persons,
                self.active_pers,
                self.number_input,
            )
