import pygame

class Cube:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width))