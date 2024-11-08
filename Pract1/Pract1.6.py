import pygame
import sys

pygame.init()

# Увеличение размера окна
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Преобразование отрезков")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Матрица преобразования T
T = [
    [1, 2],
    [1, -3]
]

# Исходная матрица отрезков L, масштабированная на 100
L = [
    [-0.5 * 100, 1.5 * 100],
    [3 * 100, -2 * 100],
    [-1 * 100, -1 * 100],
    [3 * 100, (5/3) * 100]
]

def apply_transformation(x, y, matrix):
    """Применяет матричное преобразование к координатам (x, y)."""
    new_x = matrix[0][0] * x + matrix[0][1] * y
    new_y = matrix[1][0] * x + matrix[1][1] * y
    return new_x, new_y

# Применение преобразования к каждой точке в L
transformed_L = [apply_transformation(x, y, T) for x, y in L]

# Искусственное смещение преобразованных отрезков в видимую область
shift_x, shift_y = WIDTH // 4, HEIGHT // 4
transformed_L = [(x + shift_x, y + shift_y) for x, y in transformed_L]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Рисование координатных осей
    pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)

    # Рисование сетки
    for i in range(-WIDTH // 2, WIDTH // 2, 50):
        pygame.draw.line(screen, GRAY, (WIDTH // 2 + i, 0), (WIDTH // 2 + i, HEIGHT), 1)
        pygame.draw.line(screen, BLACK, (WIDTH // 2 + i, HEIGHT // 2 - 5), (WIDTH // 2 + i, HEIGHT // 2 + 5), 1)

    for i in range(-HEIGHT // 2, HEIGHT // 2, 50):
        pygame.draw.line(screen, GRAY, (0, HEIGHT // 2 + i), (WIDTH, HEIGHT // 2 + i), 1)
        pygame.draw.line(screen, BLACK, (WIDTH // 2 - 5, HEIGHT // 2 + i), (WIDTH // 2 + 5, HEIGHT // 2 + i), 1)

    # Рисование исходных отрезков
    pygame.draw.line(screen, BLUE, (WIDTH // 2 + L[0][0], HEIGHT // 2 - L[0][1]), (WIDTH // 2 + L[1][0], HEIGHT // 2 - L[1][1]), 2)
    pygame.draw.line(screen, BLUE, (WIDTH // 2 + L[2][0], HEIGHT // 2 - L[2][1]), (WIDTH // 2 + L[3][0], HEIGHT // 2 - L[3][1]), 2)

    # Рисование преобразованных отрезков
    pygame.draw.line(screen, RED, (WIDTH // 2 + int(transformed_L[0][0]), HEIGHT // 2 - int(transformed_L[0][1])), (WIDTH // 2 + int(transformed_L[1][0]), HEIGHT // 2 - int(transformed_L[1][1])), 2)
    pygame.draw.line(screen, RED, (WIDTH // 2 + int(transformed_L[2][0]), HEIGHT // 2 - int(transformed_L[2][1])), (WIDTH // 2 + int(transformed_L[3][0]), HEIGHT // 2 - int(transformed_L[3][1])), 2)

    pygame.display.flip()

pygame.quit()