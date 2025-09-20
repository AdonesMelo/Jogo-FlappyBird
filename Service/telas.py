import pygame
from Service.constantes import TELA_LARGURA, TELA_ALTURA, IMAGEM_FUNDO, FONTE_PONTOS

def desenha_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_FUNDO, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f'Pontuação: {pontos}', 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()

def tela_inicio(tela):
    esperando = True
    while esperando:
        tela.blit(IMAGEM_FUNDO, (0, 0))
        texto = FONTE_PONTOS.render('Pressione espaço para começar', 1, (255, 255, 255))
        tela.blit(texto, ((TELA_LARGURA - texto.get_width()) // 2, TELA_ALTURA // 2))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                esperando = False

def tela_game_over(tela, pontos):
    esperando = True
    while esperando:
        tela.blit(IMAGEM_FUNDO, (0, 0))
        texto1 = FONTE_PONTOS.render('Game Over', 1, (255, 0, 0))
        texto2 = FONTE_PONTOS.render(f'Pontuação: {pontos}', 1, (255, 255, 255))
        texto3 = FONTE_PONTOS.render('Pressione espaço para reiniciar', 1, (255, 255, 255))
        tela.blit(texto1, ((TELA_LARGURA - texto1.get_width()) // 2, TELA_ALTURA // 2 - 100))
        tela.blit(texto2, ((TELA_LARGURA - texto2.get_width()) // 2, TELA_ALTURA // 2))
        tela.blit(texto3, ((TELA_LARGURA - texto3.get_width()) // 2, TELA_ALTURA // 2 + 100))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                esperando = False