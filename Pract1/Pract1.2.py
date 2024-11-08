import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graphical Primitives")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (150, 200), 50)

    pygame.draw.line(screen, GREEN, (300, 100), (500, 100), 5)
    pygame.draw.line(screen, BLUE, (300, 150), (500, 300), 5)

    pygame.draw.rect(screen, YELLOW, (50, 300, 100, 50))

    text = font.render("Hello world!", True, BLACK)
    screen.blit(text, (200, 50))

    pygame.display.flip()

pygame.quit()
