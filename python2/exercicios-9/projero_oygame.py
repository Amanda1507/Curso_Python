import pygame
import random

def mudanca_cor():
    vermelho = random.randint(0,255)
    verde = random.randint(0,255)
    azul = random.randint(0,255)
    return(vermelho,verde,azul)

#Inicializa o pygame:
pygame.init()


#Variáveis para as cores:
vermelho = 0
verde = 0
azul = 0

#Configuerações da janela:
LARGURA = 800
ALTURA = 600
TAMANH0 = 25
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Exemplo com Pygame.")

#Definindo um clock para controlae FPS:
clock = pygame.time.Clock()
FPS = 60

#Definindo a posição x e y como no centro da tela.
posicao_x_retangulo = LARGURA // 2
posicao_y_retangulo = ALTURA // 2

#Definindo a velocidade em x e y do retangulo.
velocidade_x_retangulo = 2
velocidade_y_retangulo = 2
tamanho = 25

rodando = True
while rodando:
    #Inicio do loop - Procurando eventos
    for evento in pygame.event.get(): #Devolve uma lista dos eventos que o usuário realizou
        if evento.type == pygame.QUIT:
            #Se o evento for fechar o jogo
            rodando = False
    #Fim do loop de eventos

    #Lógica de movimento:
    posicao_x_retangulo += velocidade_x_retangulo
    posicao_y_retangulo += velocidade_y_retangulo

    #Detecção de Colisão com as bordas da tela:
    if posicao_x_retangulo >= LARGURA -30 or posicao_x_retangulo <= 0:
        velocidade_x_retangulo *= -1
        if velocidade_x_retangulo <= 0:
            velocidade_x_retangulo -= 1
        else:
            velocidade_x_retangulo += 2
        vermelho,verde,azul = mudanca_cor()
        tamanho += 1
    
    if posicao_y_retangulo >= ALTURA -30 or posicao_y_retangulo <= 0:
        velocidade_y_retangulo *= -1
        if velocidade_y_retangulo <= 0:
            velocidade_y_retangulo -= 1
        else:
            velocidade_x_retangulo +=2
        vermelho,verde,azul = mudanca_cor()


    #Pinta toda a tela de branco
    tela.fill((25,250,250))

                    #tela,cor (coordenada_x, coordenada_y, largura,altura)
    pygame.draw.rect(tela,(vermelho,verde,azul),(posicao_x_retangulo,posicao_y_retangulo,tamanho,tamanho))

    #Aqui desenhamos os elementos gráficos.

    #Atualizando com fFPS
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()