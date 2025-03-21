import pygame  # Импорт библиотеки Pygame для создания игры
import random  # Импорт модуля random для генерации случайных чисел

# Инициализация Pygame
pygame.init()  # Запуск всех модулей Pygame

# Настройки экрана
SCREEN_WIDTH = 800  # Ширина экрана
SCREEN_HEIGHT = 600  # Высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создание окна игры
pygame.display.set_caption("Змейка")  # Установка заголовка окна

# Цвета
BLACK = (0, 0, 0)  # Черный цвет для фона
WHITE = (255, 255, 255)  # Белый цвет (не используется в текущей версии)
GREEN = (0, 255, 0)  # Зеленый цвет для змейки
RED = (255, 0, 0)  # Красный цвет для яблока

# Настройки игры
FPS = 10  # Количество кадров в секунду
BLOCK_SIZE = 20  # Размер одного блока змейки и яблока
clock = pygame.time.Clock()  # Создание объекта для контроля FPS

# Класс для змейки
class Snake:
    def __init__(self):
        # Начальная позиция змейки (вытянутая горизонтально)
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                     (SCREEN_WIDTH // 2 - BLOCK_SIZE, SCREEN_HEIGHT // 2),
                     (SCREEN_WIDTH // 2 - 2 * BLOCK_SIZE, SCREEN_HEIGHT // 2)]
        self.direction = (1, 0)  # Начальное направление движения (вправо)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0] * BLOCK_SIZE, head_y + self.direction[1] * BLOCK_SIZE)  # Новая позиция головы

        # Проверка на столкновение с границами экрана
        if new_head[0] < 0:
            new_head = (SCREEN_WIDTH - BLOCK_SIZE, new_head[1])  # Появление с другой стороны (левая граница)
        elif new_head[0] >= SCREEN_WIDTH:
            new_head = (0, new_head[1])  # Появление с другой стороны (правая граница)
        if new_head[1] < 0:
            new_head = (new_head[0], SCREEN_HEIGHT - BLOCK_SIZE)  # Появление с другой стороны (верхняя граница)
        elif new_head[1] >= SCREEN_HEIGHT:
            new_head = (new_head[0], 0)  # Появление с другой стороны (нижняя граница)

        self.body.insert(0, new_head)  # Добавление новой головы
        self.body.pop()  # Удаление хвоста

    def change_direction(self, new_direction):
        # Запрет на разворот на 180 градусов
        if (new_direction[0] != -self.direction[0]) and (new_direction[1] != -self.direction[1]):
            self.direction = new_direction  # Изменение направления

    def grow(self):
        self.body.append(self.body[-1])  # Увеличение длины змейки

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))  # Отрисовка змейки

    def check_collision(self):
        # Проверка столкновения с собой
        head = self.body[0]
        if head in self.body[1:]:
            return True  # Возвращает True, если змейка столкнулась с собой
        return False

# Класс для яблока
class Apple:
    def __init__(self):
        self.position = self.random_position()  # Случайная позиция яблока

    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE  # Случайная координата X
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE  # Случайная координата Y
        return (x, y)  # Возвращает координаты яблока

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))  # Отрисовка яблока

# Основной игровой цикл
def main():
    snake = Snake()  # Создание объекта змейки
    apple = Apple()  # Создание объекта яблока
    running = True  # Флаг для работы игрового цикла

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Выход из игры при закрытии окна
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and snake.direction != (0, 1):  # Кнопка A для движения вверх
                    snake.change_direction((0, -1))
                if event.key == pygame.K_z and snake.direction != (0, -1):  # Кнопка Z для движения вниз
                    snake.change_direction((0, 1))
                if event.key == pygame.K_LEFT and snake.direction != (1, 0):  # Левая стрелка для движения влево
                    snake.change_direction((-1, 0))
                if event.key == pygame.K_RIGHT and snake.direction != (-1, 0):  # Правая стрелка для движения вправо
                    snake.change_direction((1, 0))

        snake.move()  # Движение змейки

        # Проверка на съедание яблока
        if snake.body[0] == apple.position:
            snake.grow()  # Увеличение длины змейки
            apple = Apple()  # Создание нового яблока

        # Проверка на столкновение с собой
        if snake.check_collision():
            running = False  # Конец игры

        # Отрисовка
        screen.fill(BLACK)  # Заливка экрана черным цветом
        snake.draw()  # Отрисовка змейки
        apple.draw()  # Отрисовка яблока
        pygame.display.flip()  # Обновление экрана
        clock.tick(FPS)  # Ограничение FPS

    pygame.quit()  # Завершение работы Pygame

if __name__ == "__main__":
    main()  # Запуск игры