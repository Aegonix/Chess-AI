import pygame
from pygame.image import load

pygame.init()

WIDTH = 1000
HEIGHT = 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess AI")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)
BG_COLOR = (224, 220, 220)

square_size = 70
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

PIECES = {
    "white": {
        "pawn": load("Assets/w_pawn.svg"),
        "rook": load("Assets/w_rook.svg"),
        "knight": load("Assets/w_knight.svg"),
        "bishop": load("Assets/w_bishop.svg"),
        "queen": load("Assets/w_queen.svg"),
        "king": load("Assets/w_king.svg"),
    },
    "black": {
        "pawn": load("Assets/b_pawn.svg"),
        "rook": load("Assets/b_rook.svg"),
        "knight": load("Assets/b_knight.svg"),
        "bishop": load("Assets/b_bishop.svg"),
        "queen": load("Assets/b_queen.svg"),
        "king": load("Assets/b_king.svg"),
    },
}


def draw():
    win.fill(BG_COLOR)
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(
                win,
                WHITE if (i + j) % 2 != 0 else BLACK,
                (
                    (i * square_size) + 50,
                    (j * square_size) + 70,
                    square_size,
                    square_size,
                ),
            )


def main():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
