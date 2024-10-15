from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 5

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption("Змейка")

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    def __init__(self):
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self):
        pass


class Apple(GameObject):
    def __init__(self):
        super().__init__()
        self.body_color = APPLE_COLOR
        self.position = self.randomize_position
        self.new_position = None
        self.apple_rect = None

    def draw(self):
        # pygame.display.update()
        if not self.new_position:
            self.apple_rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        else:
            self.apple_rect = pygame.Rect(self.new_position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, self.apple_rect)
        pygame.draw.rect(screen, BORDER_COLOR, self.apple_rect, 1)

    # could be a static method
    @property
    def randomize_position(self):
        position = (
            choice(range(GRID_WIDTH)) * GRID_SIZE,
            choice(range(GRID_HEIGHT)) * GRID_SIZE,
        )
        rect_to_check = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        if rect_to_check.top < 0:
            rect_to_check.top = 0
        if rect_to_check.bottom > SCREEN_HEIGHT:
            rect_to_check.bottom = SCREEN_HEIGHT
        if rect_to_check.right > SCREEN_WIDTH:
            rect_to_check.bottom = SCREEN_HEIGHT
        if rect_to_check.left < 0:
            rect_to_check.left = 0
        print(rect_to_check[0], rect_to_check[1], rect_to_check[2])
        return (rect_to_check[0], rect_to_check[1])

    def position_chenger(self):
        last_rect = self.apple_rect
        pygame.draw.rect(screen, "blue", last_rect)
        self.new_position = self.randomize_position


class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.length = 1
        self.positions = [
            self.position,
        ]
        self.last = None
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.head_rect = None

    def draw(self):
        self.head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, self.head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, self.head_rect, 1)
        if self.length > 1:
            # self.get_body_rects()
            for position in self.positions[:-1]:
                rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
                # print(rect)
                pygame.draw.rect(screen, self.body_color, rect)
                pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        head_position = self.positions[0]
        rect_to_check = pygame.Rect(head_position, (GRID_SIZE, GRID_SIZE))
        if rect_to_check.top < 0:
            rect_to_check.top = SCREEN_HEIGHT
        if rect_to_check.bottom > SCREEN_HEIGHT + 20:
            rect_to_check.bottom = 0
        if rect_to_check.right > SCREEN_WIDTH:
            rect_to_check.left = -20
        if rect_to_check.right < 0:
            rect_to_check.right = SCREEN_WIDTH + 20
        # return head_position
        return (rect_to_check[0], rect_to_check[1])

    # def get_head_position(self):
    #    head_position = self.positions[0]
    #    rect_to_check = pygame.Rect(head_position, (GRID_SIZE, GRID_SIZE))
    #    if rect_to_check.bottom >= SCREEN_HEIGHT:
    #        rect_to_check.top = 0
    #    elif rect_to_check.top <= 0:
    #        rect_to_check.top = SCREEN_HEIGHT
    #    if rect_to_check.right >= SCREEN_WIDTH:
    #        rect_to_check.left = 0
    #    elif rect_to_check.left < 0:
    #        rect_to_check.right = SCREEN_WIDTH
    #    # return head_position
    #    return (rect_to_check.left, rect_to_check.top)
    # def get_head_position(self):
    #    head_position = self.positions[0]
    #    return head_position
    #    # print(rect_to_check)

    # def get_body_rects(self):
    #    list_coordinats = []
    #    for position in self.positions[:-1]:
    #        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
    #        # print(rect)
    #        pygame.draw.rect(screen, self.body_color, rect)
    #        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
    #        list_coordinats.append(rect)
    #    return list_coordinats
    #    # print(list_coordinats)

    def grow(self):
        self.positions.append(
            (
                self.positions[0][0] + 20,
                self.positions[0][1],
            )
        )
        self.length += 1

    # def key_handle_keys(self):
    #    for event in pygame.event.get():
    #        print(event)
    #        if event.type == pygame.KEYDOWN:
    #            if event.key == pygame.K_UP and self.direction != DOWN:
    #                self.next_direction = UP
    #                print("up")
    #            elif event.key == pygame.K_DOWN and self.direction != UP:
    #                self.next_direction = DOWN
    #            elif event.key == pygame.K_LEFT and self.direction != RIGHT:
    #                self.next_direction = LEFT
    #            elif event.key == pygame.K_RIGHT and self.direction != LEFT:
    #                self.next_direction = RIGHT

    def update_direction(self):
        # self.key_handle_keys()
        if self.next_direction:
            # print(self.next_direction)
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        self.update_direction()
        head_position = self.get_head_position()
        if self.direction == RIGHT:
            new_head_position = (head_position[0] + 20, head_position[1])
        if self.direction == LEFT:
            new_head_position = (head_position[0] - 20, head_position[1])
        if self.direction == UP:
            new_head_position = (head_position[0], head_position[1] - 20)
        if self.direction == DOWN:
            new_head_position = (head_position[0], head_position[1] + 20)
        self.positions.insert(0, new_head_position)
        self.last = self.positions.pop()
        return self.positions

    def reset(self):
        screen.fill(BOARD_BACKGROUND_COLOR)
        self.length = 1
        self.positions = [
            self.position,
        ]
        self.direction = RIGHT


def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
                # print("up")
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        apple.draw()
        snake.draw()
        # snake.update_direction()
        snake.move()

        #     Тут опишите основную логику игры.
        colide = pygame.Rect.colliderect(snake.head_rect, apple.apple_rect)
        if colide:

            apple.position_chenger()
            snake.grow()
            # apple.draw()

            print("colide")
        if snake.positions[0] in snake.positions[1:]:
            snake.reset()
            print("body_cus")
        # for body_part in snake.get_body_rects()[1:]:
        #    colide = pygame.Rect.colliderect(snake.head_rect, body_part)
        #    if colide:
        #        print("body_cus")
        # print(body_part)

        pygame.display.update()


if __name__ == "__main__":
    main()


# Метод draw класса Apple
# def draw(self):
#     rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, rect)
#     pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

# # Метод draw класса Snake
# def draw(self):
#     for position in self.positions[:-1]:
#         rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
#         pygame.draw.rect(screen, self.body_color, rect)
#         pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

#     # Отрисовка головы змейки
#     head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, head_rect)
#     pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

#     # Затирание последнего сегмента
#     if self.last:
#         last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
#         pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

# Функция обработки действий пользователя
# def handle_keys(game_object):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and game_object.direction != DOWN:
#                 game_object.next_direction = UP
#             elif event.key == pygame.K_DOWN and game_object.direction != UP:
#                 game_object.next_direction = DOWN
#             elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
#                 game_object.next_direction = LEFT
#             elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
#                 game_object.next_direction = RIGHT

# Метод обновления направления после нажатия на кнопку
# def update_direction(self):
#     if self.next_direction:
#         self.direction = self.next_direction
#         self.next_direction = None
