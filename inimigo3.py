import pygame
import math

class Inimigo3(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/inimigo.png")
        self.image = pygame.transform.scale(self.image, [40, 35])
        self.rect = pygame.Rect(600, 150, 50, 50)


        self.timer = -1
    def update(self, *args):
        self.timer += 0.05
        self.rect.x = 200 + math.sin(self.timer) * 60
