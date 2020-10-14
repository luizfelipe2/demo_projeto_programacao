import pygame
class Tiro (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/tiro.png")
        Tiro = pygame.mouse.get_pos()