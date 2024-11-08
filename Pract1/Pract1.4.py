import pygame
import sys

pygame.init()

# Increase the window size
WIDTH, HEIGHT = 1920,1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Segment Transformation")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

T = [
    [1, 2],
    [3, 1]
]

def apply_transformation(x, y, matrix):
    """Applies matrix transformation to coordinates (x, y)."""
    new_x = matrix[0][0] * x + matrix[0][1] * y
    new_y = matrix[1][0] * x + matrix[1][1] * y
    return new_x, new_y

# Original segment coordinates
x1, y1 = 0, 100
x2, y2 = 200, 300

# Apply transformation
new_x1, new_y1 = apply_transformation(x1, y1, T)
new_x2, new_y2 = apply_transformation(x2, y2, T)

# Calculate midpoints
mid_x1, mid_y1 = (x1 + x2) / 2, (y1 + y2) / 2
mid_x2, mid_y2 = (new_x1 + new_x2) / 2, (new_y1 + new_y2) / 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw coordinate axes
    pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)

    # Draw grid
    for i in range(-WIDTH // 2, WIDTH // 2, 50):
        pygame.draw.line(screen, GRAY, (WIDTH // 2 + i, 0), (WIDTH // 2 + i, HEIGHT), 1)
        pygame.draw.line(screen, BLACK, (WIDTH // 2 + i, HEIGHT // 2 - 5), (WIDTH // 2 + i, HEIGHT // 2 + 5), 1)

    for i in range(-HEIGHT // 2, HEIGHT // 2, 50):
        pygame.draw.line(screen, GRAY, (0, HEIGHT // 2 + i), (WIDTH, HEIGHT // 2 + i), 1)
        pygame.draw.line(screen, BLACK, (WIDTH // 2 - 5, HEIGHT // 2 + i), (WIDTH // 2 + 5, HEIGHT // 2 + i), 1)

    # Draw original segment
    pygame.draw.line(screen, BLUE, (WIDTH // 2 + x1, HEIGHT // 2 - y1), (WIDTH // 2 + x2, HEIGHT // 2 - y2), 2)
    # Draw transformed segment
    pygame.draw.line(screen, RED, (WIDTH // 2 + int(new_x1), HEIGHT // 2 - int(new_y1)), (WIDTH // 2 + int(new_x2), HEIGHT // 2 - int(new_y2)), 2)
    # Draw midpoints
    pygame.draw.circle(screen, GREEN, (WIDTH // 2 + int(mid_x1), HEIGHT // 2 - int(mid_y1)), 5)
    pygame.draw.circle(screen, GREEN, (WIDTH // 2 + int(mid_x2), HEIGHT // 2 - int(mid_y2)), 5)
    # Draw line connecting midpoints
    pygame.draw.line(screen, GREEN, (WIDTH // 2 + int(mid_x1), HEIGHT // 2 - int(mid_y1)), (WIDTH // 2 + int(mid_x2), HEIGHT // 2 - int(mid_y2)), 2)

    pygame.display.flip()

pygame.quit()