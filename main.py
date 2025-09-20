import pygame
from CLASSES.passaro import Passaro
from CLASSES.chao import Chao
from CLASSES.cano import Cano
from Service.constantes import TELA_LARGURA, TELA_ALTURA
from Service.telas import desenha_tela, tela_inicio, tela_game_over

def main():
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    tela_inicio(tela)

    passaros = [Passaro(230, 350)]
    chao = Chao(670)
    canos = [Cano(700)]
    pontos = 0
    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        relogio.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                for passaro in passaros:
                    passaro.pular()

        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []

        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    tela_game_over(tela, pontos)
                    return
                if not cano._passou and passaro._x > cano._x:
                    cano._passou = True
                    adicionar_cano = True
            cano.mover()
            if cano._x + cano._CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if len(passaros) == 0:
            tela_game_over(tela, pontos)
            return

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))

        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro._y + passaro._imagem.get_height()) > chao._y or passaro._y < 0:
                tela_game_over(tela, pontos)
                return

        desenha_tela(tela, passaros, canos, chao, pontos)

def menu_principal():
    pygame.init()
    while True:
        main()
        if not mostrar_menu_reinicio():
            break

def mostrar_menu_reinicio():
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    fonte = pygame.font.SysFont('Arial', 40)
    texto = fonte.render('R - Reiniciar  |  S - Sair', True, (255, 255, 255))
    tela.fill((0, 0, 0))
    tela.blit(texto, (100, 350))
    pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                elif evento.key == pygame.K_s:
                    pygame.quit()
                    return False

if __name__ == '__main__':
    menu_principal()
