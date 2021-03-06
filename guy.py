import pygame


class Guy (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/TestGuy.png.png")
        self.image = pygame.transform.scale(self.image, [60, 60])
        self.rect = pygame.Rect(150, 500, 100, 100)

    def update(self, *args):
        # movimentacao
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 4
        elif keys[pygame.K_s]:
            self.rect.y += 4
        elif keys[pygame.K_d]:
            self.rect.x += 4
        elif keys[pygame.K_a]:
            self.rect.x -= 4

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 600:
            self.rect.bottom = 600