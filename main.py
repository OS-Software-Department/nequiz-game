import pygame

from pers import Pers

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

PERSONS = [
    "bear",
    "cat",
    "cow",
    "dog",
    "fox",
    "koala",
    "monkey",
    "lion",
    "mouse",
    "tiger",
    "sova",
    "zayats",
]


def create_persons(window: pygame.Surface) -> list[Pers]:
    return [
        Pers(
            window,
            image_path=f"assets/players/{name}.png",
            number=i,
        )
        for i, name in enumerate(PERSONS)
    ]


def draw_active_person(
    window: pygame.Surface,
    persons: list[Pers],
    active_pers: int,
) -> None:
    person = persons[active_pers]

    icon_size = 100
    padding = 20

    background = pygame.Rect(
        padding,
        padding,
        icon_size + 20,
        icon_size + 20,
    )

    pygame.draw.rect(
        window,
        (40, 40, 40),
        background,
        border_radius=12,
    )

    icon = pygame.transform.scale(
        person.image,
        (icon_size, icon_size),
    )

    window.blit(icon, (padding + 10, padding + 10))


def main() -> None:
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Неквиз")

    bg_image = pygame.transform.scale(
        pygame.image.load("assets/map_2.png").convert(),
        (WINDOW_WIDTH, WINDOW_HEIGHT),
    )

    persons = create_persons(window)

    active_pers = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9:
                    digit = event.key - pygame.K_0

                    if active_pers == 1 and digit == 0:
                        active_pers = 10

                    elif active_pers == 1 and digit == 1:
                        active_pers = 11

                    else:
                        active_pers = digit

                for i, person in enumerate(persons):
                    person.handle_event(
                        event,
                        active=(i == active_pers),
                    )

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

        window.blit(bg_image, (0, 0))

        for person in persons:
            person.draw()

        draw_active_person(window, persons, active_pers)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
