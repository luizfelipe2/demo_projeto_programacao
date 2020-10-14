import pygame
from guy import Guy
from mago import Mago
pygame.init()

janela = pygame.display.set_mode([920, 600])
pygame.display.set_caption("Meu Primeiro Jogo")
drawGroup = pygame.sprite.Group()

#fundo
fundo = pygame.sprite.Sprite(drawGroup)
fundo.image = pygame.image.load("data/teste.png")
fundo.image = pygame.transform.scale(fundo.image, [900, 700])
fundo.rect = fundo.image.get_rect()

#objetoss
guy = Guy(drawGroup)
mago = Mago(drawGroup)

#music
pygame.mixer.music.load("data/musica.mp3")
pygame.mixer.music.play(-1)


#janela
janela_aberta = True
clock = pygame.time.Clock()
while janela_aberta :
    clock.tick(60)
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False


    #draw
    janela.fill ([46, 46, 46])
    drawGroup.update()
    drawGroup.draw(janela)
    pygame.display.update()