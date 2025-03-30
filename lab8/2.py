import pygame
import time
import random

# Настройки игры
snake_speed = 15
window_x = 700
window_y = 500

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Инициализация Pygame
pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Начальные параметры змейки
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Появление еды
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Направление движения
direction = 'RIGHT'
change_to = direction

# Очки и уровень
score = 0
level = 1
food_count = 0  # сколько фруктов съедено для повышения уровня

# Функция отображения счёта и уровня
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    level_surface = score_font.render('Level : ' + str(level), True, color)
    score_rect = score_surface.get_rect()
    level_rect = level_surface.get_rect()
    game_window.blit(score_surface, score_rect)
    game_window.blit(level_surface, (window_x - level_rect.width - 10, 10))

# Функция завершения игры
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Главный цикл игры
while True:
    # Обработка событий (управление)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Исключаем движение в противоположную сторону
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Обновляем позицию головы змейки
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Вставляем новую позицию головы
    snake_body.insert(0, list(snake_position))

    # Проверка: съедена ли еда
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += level * 10
        food_count += 1
        fruit_spawn = False
    else:
        snake_body.pop()  # удаляем хвост, если еда не съедена

    # Генерация новой еды
    if not fruit_spawn:
        while True:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
            if fruit_position not in snake_body:
                break
    fruit_spawn = True

    # Отрисовка фона
    game_window.fill(black)

    # Отрисовка змейки
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Отрисовка еды
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Проверка столкновений со стенами
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Проверка столкновения с собой
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Повышение уровня после 4 фруктов
    if food_count >= 4:
        level += 1
        snake_speed += 2
        food_count = 0

    # Показываем счёт и уровень
    show_score(1, white, 'times new roman', 20)

    # Обновляем экран
    pygame.display.update()

    # Устанавливаем скорость игры
    fps.tick(snake_speed)
