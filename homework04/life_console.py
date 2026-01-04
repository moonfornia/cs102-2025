import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        height, width = screen.getmaxyx()
        screen.border()

        title = " Conway's Game of Life | q — выход "
        screen.addstr(0, max(1, (width - len(title)) // 2), title)

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                char = "█" if self.life.curr_generation[row][col] else " "
                screen.addch(row + 1, col + 1, char)

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)  # скрыть курсор
        screen.nodelay(True)  # неблокирующий ввод
        screen.keypad(True)

        try:
            while True:
                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()

                # обработка клавиш
                key = screen.getch()
                if key == ord("q"):  # ← ВЫХОД ПО КЛАВИШЕ
                    break

                # шаг игры
                self.life.step()

                # условия остановки (опционально)
                if not self.life.is_changing:
                    break
                if self.life.is_max_generations_exceeded:
                    break

                time.sleep(0.2)

        finally:
            curses.endwin()
