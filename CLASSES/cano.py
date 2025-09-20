from Service.constantes import IMAGEM_CANO
import pygame
import random

class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self._x = x
        self._altura = 0
        self._pos_topo = 0
        self._pos_base = 0
        self._CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self._CANO_BASE = IMAGEM_CANO
        self._passou = False
        self.definir_altura()

    def definir_altura(self):
        self._altura = random.randrange(50, 450)
        self._pos_topo = self._altura - self._CANO_TOPO.get_height()
        self._pos_base = self._altura + self.DISTANCIA
    
    def mover(self):
        self._x -= self.VELOCIDADE
    
    def desenhar(self, tela):
        tela.blit(self._CANO_TOPO, (self._x, self._pos_topo))
        tela.blit(self._CANO_BASE, (self._x, self._pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self._CANO_TOPO)
        base_mask = pygame.mask.from_surface(self._CANO_BASE)

        # Corrigido: usar _x e _y
        distancia_topo = (self._x - passaro._x, self._pos_topo - round(passaro._y))
        distancia_base = (self._x - passaro._x, self._pos_base - round(passaro._y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        return topo_ponto or base_ponto