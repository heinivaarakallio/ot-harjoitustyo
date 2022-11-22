import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode((550, 550))
    pygame.display.set_caption("Sudoku")
    window.fill("white")

    for i in range(0,10):
        if i % 3 == 0:
            pygame.draw.line(window, ("black"), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(window, ("black"), (50, 50 + 50*i), (500, 50 + 50*i), 4)

        pygame.draw.line(window, ("black"), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(window, ("black"), (50, 50 + 50*i), (500, 50 + 50*i), 2)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
