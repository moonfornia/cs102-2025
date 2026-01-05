import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.is_paused = False

        self.width = life.cols * cell_size
        self.height = life.rows * cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

    def draw_lines(self) -> None:
        # Copy from previous assignment
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, (200, 200, 200), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, (200, 200, 200), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        # Copy from previous assignment
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                if self.life.curr_generation[row][col]:
                    rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (0, 200, 0), rect)

    def run(self) -> None:
        # Copy from previous assignment
        running = True

        while running:
            self.clock.tick(self.speed)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                # ПАУЗА
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.is_paused = not self.is_paused

                # РЕДАКТИРОВАНИЕ КЛЕТОК — ТОЛЬКО НА ПАУЗЕ
                if event.type == MOUSEBUTTONDOWN and self.is_paused:
                    x, y = pygame.mouse.get_pos()
                    col = x // self.cell_size
                    row = y // self.cell_size

                    if 0 <= row < self.life.rows and 0 <= col < self.life.cols:
                        self.life.curr_generation[row][col] ^= 1

            # шаг игры ТОЛЬКО если не пауза
            if not self.is_paused:
                self.life.step()

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()

        pygame.quit()
