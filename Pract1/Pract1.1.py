import sys

import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Матрица преобразования")

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
    """Применяет матричное преобразование к координатам (x, y)."""
    new_x = matrix[0][0] * x + matrix[0][1] * y
    new_y = matrix[1][0] * x + matrix[1][1] * y
    return new_x, new_y


try:
    x = int(input("Введите координату X: "))
    y = int(input("Введите координату Y: "))
except ValueError:
    print("Пожалуйста, введите целые числа.")
    sys.exit()

new_x, new_y = apply_transformation(x, y, T)

print(f"Начальные координаты: ({x}, {y})")
print(f"Новые координаты: ({new_x}, {new_y})")

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
        pygame.draw.line(screen, BLACK, (WIDTH // 2 + i, HEIGHT // 2 - 5), (WIDTH // 2 + i, HEIGHT // 2 + 5),
                         1)

    for i in range(-HEIGHT // 2, HEIGHT // 2, 50):
        pygame.draw.line(screen, GRAY, (0, HEIGHT // 2 + i), (WIDTH, HEIGHT // 2 + i), 1)
        pygame.draw.line(screen, BLACK, (WIDTH // 2 - 5, HEIGHT // 2 + i), (WIDTH // 2 + 5, HEIGHT // 2 + i),
                         1)

    pygame.draw.circle(screen, BLUE, (WIDTH // 2 + x, HEIGHT // 2 - y), 5)

    pygame.draw.circle(screen, RED, (WIDTH // 2 + int(new_x), HEIGHT // 2 - int(new_y)), 5)

    pygame.display.flip()

pygame.quit()
