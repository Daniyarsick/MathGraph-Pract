import pygame
import sys
import math

pygame.init()

# Increase the window size
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Segment Transformation")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

T = [
    [1, 2],
    [3, 1]
]

L = [
    [50, 100],
    [250, 200],
    [50, 200],
    [250, 300]
]

def apply_transformation(x, y, matrix):
    """Applies matrix transformation to coordinates (x, y)."""
    new_x = matrix[0][0] * x + matrix[0][1] * y
    new_y = matrix[1][0] * x + matrix[1][1] * y
    return new_x, new_y

def calculate_slope(x1, y1, x2, y2):
    """Calculates the slope of a line segment."""
    if x2 - x1 == 0:
        return float('inf')
    return (y2 - y1) / (x2 - x1)

# Apply transformation to each point in L
transformed_L = [apply_transformation(x, y, T) for x, y in L]

# Calculate slopes
original_slope1 = calculate_slope(L[0][0], L[0][1], L[1][0], L[1][1])
original_slope2 = calculate_slope(L[2][0], L[2][1], L[3][0], L[3][1])
transformed_slope1 = calculate_slope(transformed_L[0][0], transformed_L[0][1], transformed_L[1][0], transformed_L[1][1])
transformed_slope2 = calculate_slope(transformed_L[2][0], transformed_L[2][1], transformed_L[3][0], transformed_L[3][1])

print(f"Original slopes: {original_slope1}, {original_slope2}")
print(f"Transformed slopes: {transformed_slope1}, {transformed_slope2}")

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

    # Draw original segments
    pygame.draw.line(screen, BLUE, (WIDTH // 2 + L[0][0], HEIGHT // 2 - L[0][1]), (WIDTH // 2 + L[1][0], HEIGHT // 2 - L[1][1]), 2)
    pygame.draw.line(screen, BLUE, (WIDTH // 2 + L[2][0], HEIGHT // 2 - L[2][1]), (WIDTH // 2 + L[3][0], HEIGHT // 2 - L[3][1]), 2)

    # Draw transformed segments
    pygame.draw.line(screen, RED, (WIDTH // 2 + int(transformed_L[0][0]), HEIGHT // 2 - int(transformed_L[0][1])), (WIDTH // 2 + int(transformed_L[1][0]), HEIGHT // 2 - int(transformed_L[1][1])), 2)
    pygame.draw.line(screen, RED, (WIDTH // 2 + int(transformed_L[2][0]), HEIGHT // 2 - int(transformed_L[2][1])), (WIDTH // 2 + int(transformed_L[3][0]), HEIGHT // 2 - int(transformed_L[3][1])), 2)

    pygame.display.flip()

pygame.quit()