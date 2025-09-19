import pygame
import os

# definir constantes
TELA_LARGURA = 500
TELA_ALTURA = 800
# Usar o 'pygame.transform.scale2x' para aumentar o tamanho da imagem
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png'))) # bg de brackground(FUNDO)
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

# Definir a fonte e o tamanho do texto
pygame.font.init() # inicialiaz a fonte
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
