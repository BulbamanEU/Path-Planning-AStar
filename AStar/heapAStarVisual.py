import pygame
import math
from queue import PriorityQueue
import time
from functools import wraps
from AStar import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (0, 255, 255)
ORANGE = (255, 165, 0)
PINK = (248, 131, 121)

WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))

class Cell():
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.color = WHITE

    def is_start(self):
        return self.color == GREEN

    def is_end(self):
        return self.color == RED

    def is_closed(self):
        return self.color == ORANGE

    def is_barrier(self):
        return self.color == GREY

    def is_open(self):
        return self.color == PINK

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = RED

    def make_barrier(self):
        self.color = GREY

    def make_closed(self):
        self.color = ORANGE

    def make_open(self):
        self.color = PINK

    def make_path(self):
        self.color = LIGHT_BLUE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 1 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 1 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])


def construct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def runtime_calculator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' took {runtime:.4f} seconds to execute.")
        return result
    return wrapper

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Cell(i, j, gap, rows)
            grid[i].append(cell)

    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, BLACK, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(window, BLACK, (j*gap, 0), (j*gap, width))

def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for cell in row:
            cell.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()

def read_grid(rows, grid):
    grid_matrix = []
    for i in range(rows):
        grid_matrix.append([])
        for j in range(rows):
            if grid[i][j].color == GREY:
                grid_matrix[i].append(0)
            else:
                grid_matrix[i].append(1)
                if grid[i][j].color == GREEN:
                    src = (i, j)
                if grid[i][j].color == RED:
                    dest = (i, j)

    return grid_matrix


def draw_heap_path(path, grid):
    for i in range(len(path)):
        row, col = path[i]
        grid[row][col].make_path()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    if y >= width:
        y = width-1
    elif y < 0:
        y = 0
    if x >= width:
        x = width-1
    elif x < 0:
        x = 0

    row = y // gap
    col = x // gap

    return row, col

def main(window, width):
    ROWS = 80
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                if not start:
                    start = cell
                    start.make_start()

                elif not end:
                    end = cell
                    end.make_end()

                elif cell != end and cell != start:
                    cell.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                cell.reset()
                if cell == start:
                    start = None
                elif cell == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    temp_grid = read_grid(ROWS, grid)

                    path, dest_found = a_star_search(temp_grid, start.get_pos(), end.get_pos())
                    if dest_found != "found":
                        print("didnt find")
                    else:
                        draw_heap_path(path, grid)

                    #algorithm(lambda: draw(window, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)


        draw(window, grid, ROWS, width)

    pygame.quit()


main(WINDOW, WIDTH)



