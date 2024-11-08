import pygame
import numpy as np
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Масштабирование треугольника")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Исходные координаты треугольника
L = np.array([
    [5, 1],
    [5, 2],
    [3, 2]
])

# Матрица масштабирования
T = np.array([
    [2, 0],
    [0, 2]
])

# Масштабируем для визуализации
L_scaled = (L @ T) * 80  # Умножаем на 80 для масштаба (наглядности)

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

    # Отрисовка исходного треугольника
    pygame.draw.polygon(screen, BLUE, [to_pygame_coords(pt) for pt in L * 80], 1)

    # Отрисовка масштабированного треугольника
    pygame.draw.polygon(screen, RED, [to_pygame_coords(pt) for pt in L_scaled], 1)

    # Обновление экрана
    pygame.display.flip()
