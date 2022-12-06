import pygame
import random
from pygame.locals import *

# função aleatória para gerar sempre um grid


def grid():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    # divisão por 10 para que o grid fique sempre alinhado, sem sobras
    return (x//10 * 10, y//10 * 10)

# função para pegar a colisão


def colisao(cobra, comida):
    # se a cabeça da cobra for igual a comida, retorna verdadeiro
    return (cobra[0] == comida[0]) and (cobra[1] == comida[1])


# Variaveis de Direção
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
# definindo a tela
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
def gameloop():
    # modelo da snake
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_model = pygame.Surface((10, 10))
    snake_model.fill((255, 255, 255))

    # modelo da comida
    comida_pos = grid()
    comida = pygame.Surface((10, 10))
    comida.fill((255, 0, 0))

    direcao = LEFT

    # loop do jogo, limitado a 30 frames por segundo
    clock = pygame.time.Clock()

    # definindo o score e o game over
    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0
    game_over = False
    while not game_over:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # movimentação da snake com as setas
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    direcao = UP
                if event.key == K_DOWN:
                    direcao = DOWN
                if event.key == K_LEFT:
                    direcao = LEFT
                if event.key == K_RIGHT:
                    direcao = RIGHT

        # pegando a colisão
        if colisao(snake[0], comida_pos):
            comida_pos = grid()
            snake.append((0, 0))
            score += 1

        # colisão com a parede
        if snake[0][0] == 500 or snake[0][0] < 0 or snake[0][1] == 500 or snake[0][1] < 0:
            game_over = True
            break

        if game_over:
            break

        # movimentação da snake
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        if direcao == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if direcao == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if direcao == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        if direcao == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])

        # limpando a tela pois teremos uma nova posição da snake
        screen.fill((0, 0, 0))
        screen.blit(comida, comida_pos)

        # mostrando o score
        score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (500 - 110, 10)
        screen.blit(score_font, score_rect)

        for pos in snake:
            screen.blit(snake_model, pos)

        pygame.display.update()


    while game_over:
        # loop para o fim do jogo
        game_over_font = pygame.font.Font('freesansbold.ttf', 30)
        game_over_screen = game_over_font.render(
            'Game Over', True, (255, 255, 255))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (500 / 2, 10)

        # mostrando o texto caso queira continuar jogando
        continue_font = pygame.font.Font('freesansbold.ttf', 20)
        continue_screen = continue_font.render(
            'Continuar(C)', True, (255, 255, 255))
        continue_rect = continue_screen.get_rect()
        continue_rect.midtop = (500 / 2, 50)

        # mostrando o texto caso queira sair do jogo
        exit_font = pygame.font.Font('freesansbold.ttf', 20)
        exit_screen = exit_font.render('Sair(S)', True, (255, 255, 255))
        exit_rect = exit_screen.get_rect()
        exit_rect.midtop = (500 / 2, 80)

        # desenhando o texto na tela
        screen.blit(game_over_screen, game_over_rect)
        screen.blit(continue_screen, continue_rect)
        screen.blit(exit_screen, exit_rect)

        pygame.display.update()
        pygame.time.wait(500)

        # loop para reiniciar o jogo
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_c:
                        gameloop()                                        
                    if event.key == K_s:
                        pygame.quit()
                        exit()
gameloop()

"""
# verifica se a cobra atingiu a si mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break
"""