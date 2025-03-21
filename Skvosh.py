import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Сквош")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройки игры
FPS = 60
clock = pygame.time.Clock()

# Класс для ракетки
class Paddle:
    def __init__(self, x, y):
        self.width = 100
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)  # Создание прямоугольника для ракетки
        self.speed = 8

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed  # Движение влево
        if direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed  # Движение вправо

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)  # Отрисовка ракетки

# Класс для мяча
class Ball:
    def __init__(self, x, y):
        self.radius = 10
        self.rect = pygame.Rect(x, y, self.radius * 2, self.radius * 2)  # Создание прямоугольника для мяча
        self.speed_x = 5 * random.choice((1, -1))  # Случайное направление по X
        self.speed_y = 5  # Направление по Y

    def move(self):
        self.rect.x += self.speed_x  # Движение по X
        self.rect.y += self.speed_y  # Движение по Y

        # Отскок от стен
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1  # Изменение направления по X
        if self.rect.top <= 0:
            self.speed_y *= -1  # Изменение направления по Y

    def draw(self):
        pygame.draw.circle(screen, RED, self.rect.center, self.radius)  # Отрисовка мяча

    def collide_with_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.speed_y *= -1  # Отскок от ракетки

# Основной игровой цикл
def main():
    paddle = Paddle(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50)  # Создание ракетки
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Создание мяча
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Выход из игры

        # Управление ракеткой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("left")  # Движение ракетки влево
        if keys[pygame.K_RIGHT]:
            paddle.move("right")  # Движение ракетки вправо

        # Обновление позиции мяча
        ball.move()
        ball.collide_with_paddle(paddle)

        # Проверка на проигрыш
        if ball.rect.bottom >= SCREEN_HEIGHT:
            running = False  # Конец игры, если мяч упал

        # Отрисовка
        screen.fill(BLACK)  # Заливка экрана черным цветом
        paddle.draw()  # Отрисовка ракетки
        ball.draw()  # Отрисовка мяча
        pygame.display.flip()  # Обновление экрана
        clock.tick(FPS)  # Ограничение FPS

    pygame.quit()

if __name__ == "__main__":
    main()