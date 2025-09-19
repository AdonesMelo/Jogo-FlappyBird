from Service.constantes import IMAGENS_PASSARO
import pygame

class Passaro:
    IMGS = IMAGENS_PASSARO
    # Animações de rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._angulo = 0
        self._velocidade = 0
        self._altura = self._y
        self._tempo = 0
        self._contagem_imagem = 0
        self._imagem = self.IMGS[0]

    def pular(self):
        self._velocidade = -10.5
        self._tempo = 0
        self._altura = self._y

    def mover(self):
        # calcular o deslocamento
        self._tempo += 1
        deslocamento = 1.5 * (self._tempo ** 2) + self._velocidade * self._tempo # Formula S = so + vot + at²/2
        
        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0: # para da uma ganho na hora de pular
            deslocamento -= 2

        self._y += deslocamento

        # o angulo do passaro
        if deslocamento < 0 or self._y < (self._altura + 50): # Para questões de animações
            if self._angulo < self.ROTACAO_MAXIMA:
                self._angulo = self.ROTACAO_MAXIMA
        else:
            if self._angulo > -90:
                self._angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # definir qual imagem do passaro vai usar
        self._contagem_imagem += 1
        if self._contagem_imagem < self.TEMPO_ANIMACAO:
            self._imagem = self.IMGS[0]
        elif self._contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self._imagem = self.IMGS[1]
        elif self._contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self._imagem = self.IMGS[2]
        elif self._contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self._imagem = self.IMGS[1]
        elif self._contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
            self._imagem = self.IMGS[0]
            self._contagem_imagem = 0

        # se o passaro estiver caindo não vou bater asa
        if self._angulo <= -80:
            self._imagem = self.IMGS[1]
            self._contagem_imagem = self.TEMPO_ANIMACAO * 2

        # desenhar imagem
        imagem_rotacionada = pygame.transform.rotate(self._imagem, self._angulo)
        pos_centro_imagem = self._imagem.get_rect(topleft=(self._x, self._y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    # Para saber se o passarro colidio com o cano
    def get_mask(self):
        return pygame.mask.from_surface(self._imagem)