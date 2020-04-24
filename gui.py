import pygame
from typing import Callable
class Button:
    font = pygame.font.Font("Consola.ttf", 25)

    def __init__(self, rect: pygame.Rect, name: str, callback: Callable[[], None]):
        self.rect = rect

        # self.text is a pygame surface
        self.text = self.font.render(name, True, (0, 0, 0))
        self.callback = callback

class GuiSystem:
    HOVER_COLOR = (102, 140, 255)
    COLOR = (130, 161, 255)

    def __init__(self, window):
        self.buttons = []
        self.window = window

    def AddButton(self, rect: pygame.Rect, *, name: str, callback: Callable[[], None]):
        self.buttons.append(Button(rect, name, callback))

    def OnEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    button.callback()
                    break
    
    def Draw(self):
        for button in self.buttons:
            color = self.HOVER_COLOR if button.rect.collidepoint(pygame.mouse.get_pos()) else self.COLOR
            pygame.draw.rect(self.window, color, button.rect)
            anchor = [bc - 0.5 * fc for bc, fc in zip(button.rect.center, button.text.get_size())]
            self.window.blit(button.text, anchor)