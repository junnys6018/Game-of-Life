import pygame
from typing import Tuple, List
# Type alias
Grid = List[List[bool]]

def FromFile(filename: str) -> Tuple[Grid, int]:
    ret = []
    with open(filename, 'r') as f:
        dim = int(f.readline())
        for line in f:
            row = []
            for char in line:
                if char == 'x':
                    row.append(True)
                elif char == 'o':
                    row.append(False)
            ret.append(row)
    return ret, dim

def DrawCells(cells: Grid, window: pygame.Surface, width: int):
    rect = pygame.Rect(0, 0, width - 1, width - 1)
    for x, row in enumerate(cells):
        for y, flag in enumerate(row):
            color = (0,0,0) if flag else (255, 255, 255)
            pygame.draw.rect(window, color, rect.move(y * width, x * width))

def Neighbours(cells: Grid, x: int, y: int) -> int:
    count = 0
    dim = len(cells)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if i + x < 0 or j + y < 0 or i + x >= dim or j + y >= dim:
                continue
            if cells[i + x][j + y]:
                count = count + 1
    return count

def UpdateCells(current: Grid, new: Grid):
    for x, row in enumerate(current):
        for y, flag in enumerate(row):
            new[x][y] = flag
            neighbours = Neighbours(current, x, y)
            if flag:
                if neighbours < 2 or neighbours > 3:
                    new[x][y] = False
            elif neighbours == 3:
                new[x][y] = True