import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Segment Transformation")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

T = [
    [1, 3],
    [4, 1]
]

def apply_transformation(x, y, matrix):
    """Applies matrix transformation to coordinates (x, y)."""
    new_x = matrix[0][0] * x + matrix[0][1] * y
    new_y = matrix[1][0] * x + matrix[1][1] * y
    return new_x, new_y

try:
    x1 = int(input("Enter X1 coordinate: "))
    y1 = int(input("Enter Y1 coordinate: "))
    x2 = int(input("Enter X2 coordinate: "))
    y2 = int(input("Enter Y2 coordinate: "))
except ValueError:
    print("Please enter integer values.")
    sys.exit()

new_x1, new_y1 = apply_transformation(x1, y1, T)
new_x2, new_y2 = apply_transformation(x2, y2, T)

print(f"Original coordinates: ({x1}, {y1}), ({x2}, {y2})")
print(f"Transformed coordinates: ({new_x1}, {new_y1}), ({new_x2}, {new_y2})")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)

    for i in range(-WIDTH // 2, WIDTH // 2, 50):
        pygame.draw.line(screen, GRAY, (WIDTH // 2 + i, 0), (WIDTH // 2 + i, HEIGHT), 1)
        pygame.draw.line(screen, BLACK, (WIDTH // 2 + i, HEIGHT // 2 - 5), (WIDTH // 2 + i, HEIGHT // 2 + 5), 1)

    for i in range(-HEIGHT // 2, HEIGHT // 2, 50):
        pygame.draw.line(screen, GRAY, (0, HEIGHT // 2 + i), (WIDTH, HEIGHT // 2 + i), 1)
        pygame.draw.line(screen, BLACK, (WIDTH // 2 - 5, HEIGHT // 2 + i), (WIDTH // 2 + 5, HEIGHT // 2 + i), 1)

    pygame.draw.line(screen, BLUE, (WIDTH // 2 + x1, HEIGHT // 2 - y1), (WIDTH // 2 + x2, HEIGHT // 2 - y2), 2)
    pygame.draw.line(screen, RED, (WIDTH // 2 + int(new_x1), HEIGHT // 2 - int(new_y1)), (WIDTH // 2 + int(new_x2), HEIGHT // 2 - int(new_y2)), 2)

    pygame.display.flip()

pygame.quit()