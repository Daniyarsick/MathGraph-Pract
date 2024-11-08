import pygame
import numpy as np
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Отражение треугольника относительно y = x")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Исходные координаты треугольника
L = np.array([
    [8, 1],
    [7, 3],
    [6, 2]
])

# Матрица отражения относительно линии y = x
T = np.array([
    [0, 1],
    [1, 0]
])

# Масштабируем для визуализации
scale = 80
L_scaled = L * scale
L_reflected = (L @ T) * scale

# Смещение для центра экрана
offset_x, offset_y = width // 10, height // 10

# Функция для преобразования координат (удобство отрисовки)
def to_pygame_coords(point):
    x, y = point
    return int(x + offset_x), int(height - (y + offset_y))

# Главный цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заливка фона
    screen.fill(WHITE)

    # Сетка
    for x in range(0, width, 50):
        pygame.draw.line(screen, GRAY, (x, 0), (x, height))
    for y in range(0, height, 50):
        pygame.draw.line(screen, GRAY, (0, y), (width, y))

    # Оси
    pygame.draw.line(screen, BLACK, (0, height // 2), (width, height // 2), 2)  # X ось
    pygame.draw.line(screen, BLACK, (width // 2, 0), (width // 2, height), 2)  # Y ось

    # Линия y = x
    pygame.draw.line(screen, BLACK, (0, height - offset_y), (width - offset_x, 0), 1)

    # Отрисовка исходного треугольника
    pygame.draw.polygon(screen, BLUE, [to_pygame_coords(pt) for pt in L_scaled], 1)

    # Отрисовка отраженного треугольника
    pygame.draw.polygon(screen, RED, [to_pygame_coords(pt) for pt in L_reflected], 1)

    # Обновление экрана
    pygame.display.flip()
