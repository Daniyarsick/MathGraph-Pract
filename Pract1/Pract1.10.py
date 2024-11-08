import pygame
import math

# Инициализация Pygame
pygame.init()

# Размер экрана
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Спираль улитки Паскаля")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметры спирали Паскаля
a = 100  # коэффициент
b = 50   # смещение
angle_step = 0.1  # шаг угла
max_angle = 10 * math.pi  # максимальный угол

# Центр экрана
center_x, center_y = width // 2, height // 2

# Список точек для спирали
points = []

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Расчет точек спирали
    for angle in range(0, int(max_angle / angle_step)):
        theta = angle * angle_step
        r = b + 2 * a * math.cos(theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        # Смещаем координаты относительно центра
        points.append((int(center_x + x), int(center_y + y)))

    # Рисуем линию, соединяющую все точки
    pygame.draw.lines(screen, BLACK, False, points, 1)

    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
