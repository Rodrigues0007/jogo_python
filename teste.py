
import pygame
import sys
import numpy as np

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
WIDTH = 400
HEIGHT = 400
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Define as cores
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cria a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Velha')

# Cria o tabuleiro
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Função para desenhar as linhas do tabuleiro
def draw_lines():
    screen.fill(WHITE)
    # Linhas horizontais
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    # Linhas verticais
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Função principal do jogo
def main():
    draw_lines()
    player = 1  # 1 é o jogador 1 e 2 é o jogador 2
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # X
                mouseY = event.pos[1]  # Y

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if board[clicked_row][clicked_col] == 0:
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        player = 2
                    elif player == 2:
                        mark_square(clicked_row, clicked_col, 2)
                        player = 1

                    draw_figures()

        pygame.display.update()

# Função para marcar o quadrado
def mark_square(row, col, player):
    board[row][col] = player

# Função para desenhar as figuras
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), SQUARE_SIZE//3, 15)
            elif board[row][col] == 2:
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE//4, row * SQUARE_SIZE + SQUARE_SIZE//4), (col * SQUARE_SIZE + 3*SQUARE_SIZE//4, row * SQUARE_SIZE + 3*SQUARE_SIZE//4), 15)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 3*SQUARE_SIZE//4, row * SQUARE_SIZE + SQUARE_SIZE//4), (col * SQUARE_SIZE + SQUARE_SIZE//4, row * SQUARE_SIZE + 3*SQUARE_SIZE//4), 15)

if __name__ == '__main__':
    main()
    