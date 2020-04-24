import pygame
pygame.init()
from logic import DrawCells, UpdateCells
from gui import *
from functools import partial

class ApplicationState:
    def __init__(self, file: str):
        self.width = 900
        self.height = 600
        self.LoadStateFromFile(file)

    def LoadStateFromFile(self, file: str):
        self.front_buffer = []
        with open(file, 'r') as f:
            self.dim = int(f.readline())
            for line in f:
                row = []
                for char in line:
                    if char == 'x':
                        row.append(True)
                    elif char == 'o':
                        row.append(False)
                self.front_buffer.append(row)

        self.back_buffer = [[False for i in range(self.dim)] for j in range(self.dim)]
        self.cell_dim = min(self.width // self.dim, self.height // self.dim)

    def SwapBuffers(self):
        temp = self.front_buffer
        self.front_buffer = self.back_buffer
        self.back_buffer = temp


# Initialize Application related data
app = ApplicationState("switch_engine.txt")

# Initialize pygame window and clock
window = pygame.display.set_mode((app.width, app.height))
pygame.display.set_caption("Test window")

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 50) # Update cells every 50 ms

# Initialize GUI

presets = ["switch_engine", "toad", "gun", "triangle"]
loaders = [partial(app.LoadStateFromFile, preset + ".txt") for preset in presets]

gui_system = GuiSystem(window)

for index, (preset, loader) in enumerate(zip(presets, loaders)):
    gui_system.AddButton(pygame.Rect(620, index * 80 + 10, 260, 60), name=preset, callback=loader)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        gui_system.OnEvent(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            window.fill(pygame.Color(112, 112, 112))
            UpdateCells(app.front_buffer, app.back_buffer)
            DrawCells(app.front_buffer, window, app.cell_dim)
            app.SwapBuffers()

        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            print(event)

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(0, 0, app.height, app.height).collidepoint(mouse_pos):
            x, y = (i // app.cell_dim for i in mouse_pos)
            app.front_buffer[y][x] = True

    gui_system.Draw()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()