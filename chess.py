import pygame
import chess
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 480, 480
DIM = 8  # Dimensions of the board (8x8)
SQ_SIZE = WIDTH // DIM

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
LIGHT_BROWN = (222, 184, 135)

# Load piece images
PIECE_IMAGES = {}
for piece in ['b', 'k', 'n', 'p', 'q', 'r', 'B', 'K', 'N', 'P', 'Q', 'R']:
    PIECE_IMAGES[piece] = pygame.image.load(f'images/{piece}.png')

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Self-Playing Chess')

# Initialize board
board = chess.Board()

def draw_board(screen):
    """ Draw the chess board """
    for row in range(DIM):
        for col in range(DIM):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    """ Draw the pieces on the board """
    board_fen = board.board_fen().split('/')
    for row in range(DIM):
        col = 0
        for char in board_fen[row]:
            if char.isdigit():
                col += int(char)
            else:
                piece_image = PIECE_IMAGES[char]
                piece_rect = piece_image.get_rect()
                piece_rect.topleft = (col * SQ_SIZE, row * SQ_SIZE)
                screen.blit(piece_image, piece_rect)
                col += 1

def random_move(board):
    """ Make a random legal move """
    legal_moves = list(board.legal_moves)
    move = random.choice(legal_moves)
    board.push(move)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Draw the board and pieces
    draw_board(screen)
    draw_pieces(screen, board)
    pygame.display.flip()
    
    # Make a random move for both sides
    if not board.is_game_over():
        random_move(board)
        pygame.time.wait(1000)  # Wait 1 second between moves

    # Check for game over
    if board.is_game_over():
        print("Game over!")
        pygame.time.wait(3000)  # Wait 3 seconds before closing
        running = False

pygame.quit()
