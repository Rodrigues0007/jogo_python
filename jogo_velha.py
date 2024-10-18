# Example file showing a basic pygame "game loop"
import pygame

# pygame setup (configuração)
pygame.init() #inicialização do 
pygame.font.init() #inicialização do pacote de fontes no pygame

pygame.display.set_caption("JOGO DA VELHA") #nome da janela do jogo
screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
clock = pygame.time.Clock() #biblioteca tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100, True, True) #importar fonte
running = True #variavel de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'red')
cor_fundo = 1

while running:
    # poll for events controle de eventos no jogo
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #pygame.MOUSEBUTTONDOWN e vento de click do mouse
            print('Clicou')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1

                                       #origem    destino
    # desenha o tabuleiro              (x , y)    (x , y) 
    pygame.draw.line(screen, 'white', (200, 0), (200, 600), 10)
    pygame.draw.line(screen, 'white', (400, 0), (400, 600), 10)
    pygame.draw.line(screen, 'white', (0, 200), (600, 200), 10)
    pygame.draw.line(screen, 'white', (0, 400),(600, 400), 10)

    screen.blit(personagem_x,(60,30))
    screen.blit(personagem_y,(260,30))
    screen.blit(personagem_x,(460,30))
       
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  #limita o fps para 60

pygame.quit()