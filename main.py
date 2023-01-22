import pygame
from pygame.image import load
pygame.init()

WIDTH = 1000
HEIGHT = 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess AI")

PIECES = {
    "white": {
        "pawn": load("Assets/w_pawn.svg"),
        "rook": load("Assets/w_rook.svg"),
        "knight": load("Assets/w_knight.svg"),
        "bishop": load("Assets/w_bishop.svg"),
        "queen": load("Assets/w_queen.svg"),
        "king": load("Assets/w_king.svg")
    },
    "black": {
        "pawn": load("Assets/b_pawn.svg"),
        "rook": load("Assets/b_rook.svg"),
        "knight": load("Assets/b_knight.svg"),
        "bishop": load("Assets/b_bishop.svg"),
        "queen": load("Assets/b_queen.svg"),
        "king": load("Assets/b_king.svg"),
    }
}

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

if __name__ == "__main__":
    main()