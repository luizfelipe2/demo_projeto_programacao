import pygame

class Mago (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Mago.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(400, 50, 200, 200)