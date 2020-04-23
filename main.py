import pygame
pygame.init()
from logic import FromFile, DrawCells, UpdateCells
from gui import *
from functools import partial

width = 900
height = 600

front_buffer = []
back_buffer = []
cell_dim = 0

def load(path):
    global front_buffer, back_buffer, cell_dim
    front_buffer, dim = FromFile(path)
    back_buffer = [[False for i in range(dim)] for j in range(dim)]
    cell_dim = min(width // dim, height // dim)

load("toad.txt")

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test window")
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 50) # Update cells every 50 ms
running = True

presets = ["switch_engine", "toad", "gun", "triangle"]
loaders = [partial(load, preset + ".txt") for preset in presets]

gui_system = GuiSystem(window)

for index, (preset, loader) in enumerate(zip(presets, loaders)):
    gui_system.AddButton(pygame.Rect(620, index * 80 + 10, 260, 60), name=preset, callback=loader)

while running:

    for event in pygame.event.get():
        gui_system.OnEvent(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            window.fill(pygame.Color(112, 112, 112))
            UpdateCells(front_buffer, back_buffer)
            DrawCells(front_buffer, window, cell_dim)
            # swap buffers
            temp = front_buffer
            front_buffer = back_buffer
            back_buffer = temp

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(0, 0, height, height).collidepoint(mouse_pos):
            x, y = (i // cell_dim for i in mouse_pos)
            front_buffer[y][x] = True

    gui_system.Draw()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()