import pygame
import numpy as np
import math

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
m = 0.9  # Коэффициент масштабирования
alpha = math.pi / 32  # Угол поворота в радианах
iterations = 20

# Начальные координаты квадрата (масштабированные на 100)
square_points = np.array([
    [2, -2],
    [-2, -2],
    [-2, 2],
    [2, 2]
]) * 100

# Функция для масштабирования точек
def scale(points, factor):
    return points * factor

# Функция для поворота точек
def rotate(points, angle):
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])
    return points @ rotation_matrix.T

# Создание окна Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transforming Square")

# Список для хранения всех квадратов
squares = []

# Главный цикл
running = True
for i in range(iterations):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Масштабируем и поворачиваем квадрат
    square_points = scale(square_points, m)
    square_points = rotate(square_points, alpha)

    # Смещение для центрирования квадрата в окне
    offset_x = WIDTH // 2
    offset_y = HEIGHT // 2

    # Добавляем текущий квадрат в список с учетом смещения
    squares.append([(point[0] + offset_x, point[1] + offset_y) for point in square_points])

    # Отрисовываем все квадраты из списка
    for sq in squares:
        pygame.draw.polygon(screen, (0, 0, 255), sq, width=3)  # Увеличиваем толщину линии до 3 пикселей

    # Обновление дисплея
    pygame.display.flip()
    pygame.time.delay(500)  # Задержка для видимости

pygame.quit()