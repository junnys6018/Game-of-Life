import pygame
width = 800
height = 600

dim = 30
cell_dim = min(width // dim, height // dim)

front_buffer = [[i == 4 and j >= 3 and j <= 20 for i in range(dim)] for j in range(dim)]
back_buffer = [[False for i in range(dim)] for j in range(dim)]

def DrawCells(cells):
    rect = pygame.Rect(0, 0, cell_dim - 1, cell_dim - 1)
    for row, x in zip(cells, range(dim)):
        for flag, y in zip(row, range(dim)):
            color = (0,0,0) if flag else (255, 255, 255)
            pygame.draw.rect(window, color, rect.move(x * cell_dim, y * cell_dim))

def Neighbours(cells, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if cells[(i + x) % dim][(j + y) % dim]:
                count = count + 1
    return count


def UpdateCells(current, new):
    for row, x in zip(current, range(dim)):
        for flag, y in zip(row, range(dim)):
            new[x][y] = flag
            neighbours = Neighbours(current, x, y)
            if flag:
                if neighbours < 2 or neighbours > 3:
                    new[x][y] = False
            elif neighbours == 3:
                new[x][y] = True

window = pygame.display.set_mode((800, 600))
window.fill(pygame.Color(112, 112, 112))
pygame.display.set_caption("Test window")
clock = pygame.time.Clock()
running = False
while not running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    UpdateCells(front_buffer, back_buffer)
    DrawCells(front_buffer)
    temp = front_buffer
    front_buffer = back_buffer
    back_buffer = temp

    pygame.display.update()
    clock.tick(3)

pygame.quit()
quit()