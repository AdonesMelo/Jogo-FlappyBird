from Service.constantes import IMAGEM_CHAO

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self._y = y
        self._chao_1 = 0
        self._chao_2 = self.LARGURA

    def mover(self):
        self._chao_1 -= self.VELOCIDADE
        self._chao_2 -= self.VELOCIDADE

        # se chao for menor que a tela ele vai para posição 1
        if self._chao_1 + self.LARGURA < 0:
            self._chao_1 = self._chao_2 + self.LARGURA
        elif self._chao_2 + self.LARGURA < 0:
            self._chao_2 = self._chao_1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self._chao_1, self._y))
        tela.blit(self.IMAGEM, (self._chao_2, self._y))