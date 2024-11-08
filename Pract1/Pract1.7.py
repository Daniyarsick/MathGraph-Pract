import pygame
import sys

pygame.init()

# Увеличение размера окна
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вращение треугольника")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Матрица вращения T для 90 градусов против часовой стрелки
T = [
    [0, 1],
    [-1, 0]
]

# Исходная матрица треугольника L, масштабированная на 100
L = [
    [3 * 100, -1 * 100],
    [4 * 100, 1 * 100],
    [2 * 100, 1 * 100]
]

def apply_transformation(x, y, matrix):
    """Применяет матричное преобразование к координатам (x, y)."""
    new_x = matrix[0][0] * x + matrix[0][1] * y
    new_y = matrix[1][0] * x + matrix[1][1] * y
    return new_x, new_y

# Применение преобразования к каждой точке в L
transformed_L = [apply_transformation(x, y, T) for x, y in L]

# Искусственное смещение исходного и преобразованного треугольников в видимую область
shift_x, shift_y = WIDTH // 4, HEIGHT // 4
shifted_L = [(x + shift_x, y + shift_y) for x, y in L]
shifted_transformed_L = [(x + shift_x, y + shift_y) for x, y in transformed_L]

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

    # Рисование исходного треугольника
    pygame.draw.polygon(screen, BLUE, [(WIDTH // 2 + x, HEIGHT // 2 - y) for x, y in shifted_L], 2)

    # Рисование преобразованного треугольника
    pygame.draw.polygon(screen, RED, [(WIDTH // 2 + x, HEIGHT // 2 - y) for x, y in shifted_transformed_L], 2)

    pygame.display.flip()

pygame.quit()