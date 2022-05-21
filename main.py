import pygame

WIDTH, HEIGHT = 800, 600
TITLE = "Impossible Pong"

running = True


def main():
    global running

    pygame.init()

    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    while running:

        surface.fill('black')
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
