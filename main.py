import pygame
pygame.init()
pygame.font.init()
from logic import FromFile, DrawCells, UpdateCells
from gui import *

width = 800
height = 600

front_buffer, dim = FromFile("switch_engine.txt")
back_buffer = [[False for i in range(dim)] for j in range(dim)]
cell_dim = min(width // dim, height // dim)

window = pygame.display.set_mode((800, 600))
window.fill(pygame.Color(112, 112, 112))
pygame.display.set_caption("Test window")
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 100) # Update cells every 100 ms
running = True


def cb():
    print("Button pressed!")

gui_system = GuiSystem(window)
gui_system.AddButton(pygame.Rect(600,0,80,80), name="clear", callback=cb)

while running:

    for event in pygame.event.get():
        gui_system.OnEvent(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            UpdateCells(front_buffer, back_buffer)
            DrawCells(front_buffer, window, cell_dim)
            # swap buffers
            temp = front_buffer
            front_buffer = back_buffer
            back_buffer = temp

        gui_system.Draw()

        #print(event)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()