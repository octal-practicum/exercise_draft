import sys
from random import choice

import pygame

# Constants for field and grid sizes:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Directions of movement:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Background color - black:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Border color of the cell
BORDER_COLOR = (93, 216, 228)

# Apple color
APPLE_COLOR = (255, 0, 0)

# Snake color
SNAKE_COLOR = (0, 255, 0)

# Snake movement speed:
SPEED = 5

# Game window settings:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Game window title:
pygame.display.set_caption("Snake")

# Time settings:
clock = pygame.time.Clock()


class GameObject:
    """Template for all game objects."""

    def __init__(self):
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self):
        """Empty method to override."""


class Apple(GameObject):
    """An apple tamplate."""

    def __init__(self):
        super().__init__()
        self.body_color = APPLE_COLOR
        self.position = self.randomize_position()

    def draw(self):
        """Draw apple object."""
        self.apple_rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, self.apple_rect)
        pygame.draw.rect(screen, BORDER_COLOR, self.apple_rect, 1)

    # @property
    def randomize_position(self):
        """Randomaize apple position"""
        position = (
            choice(range(GRID_WIDTH)) * GRID_SIZE,
            choice(range(GRID_HEIGHT)) * GRID_SIZE,
        )
        # self.position = position
        return position


class Snake(GameObject):
    """Snake template."""

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

    def draw(self):
        """Draw snake objects and reduce extra rects."""
        # Draw head
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)
        # Draw tails
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        # Reduce extra tails
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Head position coordinats"""
        # head_position = self.positions[0]
        # return head_position
        return self.positions[0]

    def get_opposite_coordinats(self, head_position):
        """Return snake frome one side screen to other side screen."""
        rect_to_check = pygame.Rect(head_position, (GRID_SIZE, GRID_SIZE))
        if rect_to_check.bottom <= 0:
            rect_to_check.top = SCREEN_HEIGHT
        elif rect_to_check.top >= SCREEN_HEIGHT:
            rect_to_check.bottom = 0
        if rect_to_check.left >= SCREEN_WIDTH:
            rect_to_check.right = 0
        elif rect_to_check.right <= 0:
            rect_to_check.left = SCREEN_WIDTH
        self.positions[0] = (rect_to_check[0], rect_to_check[1])
        return self.positions

    def get_grow(self):
        """Add new rect to snake tail."""
        self.positions.append(
            (
                self.positions[0][0] + GRID_SIZE,
                self.positions[0][1],
            )
        )
        self.length += 1

    def update_direction(self):
        """Change object direction after arrow key press"""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Chenge snake direction."""
        direction_x = (RIGHT, LEFT)
        direction_y = (UP, DOWN)
        curent_position_x, curent_position_y = self.get_head_position()
        if self.direction in direction_x:
            new_x = (curent_position_x + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH
            new_head_position = (new_x, curent_position_y)
        elif self.direction in direction_y:
            new_y = (curent_position_y + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT
            new_head_position = (curent_position_x, new_y)
        self.positions.insert(
            0,
            (new_head_position),
        )
        self.last = self.positions.pop()
        return self.positions

    def reset(self):
        """Reset all game objects."""
        screen.fill(BOARD_BACKGROUND_COLOR)
        self.length = 1
        self.positions = [
            self.position,
        ]
        self.direction = RIGHT


class EndOfGameError(Exception):
    """Custom exception raise when user quit."""

    # def __str__(self):
    #    """Describe exception."""
    #    return "Game loop has interrupted by User."


def handle_keys(game_object):
    """Key handler."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            raise EndOfGameError
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Main game function process all main events in while loop."""
    # Intialisation PyGame:
    pygame.init()
    # Game objects
    apple = Apple()
    snake = Snake()
    game_continue = True
    while game_continue:
        clock.tick(SPEED)
        try:
            handle_keys(snake)
        except EndOfGameError:
            # pygame.quit()
            sys.exit("Game loop has interrupted by User.")
        apple.draw()
        snake.move()
        snake.update_direction()
        snake_head = snake.get_head_position()
        # Snake eat apple
        if snake_head == apple.position:
            apple.randomize_position()
            snake.get_grow()
        # Snake eat own tail
        if snake.positions[0] in snake.positions[1:]:
            snake.reset()
        # Snake walk troygh the wall
        snake.get_opposite_coordinats(snake_head)
        snake.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
