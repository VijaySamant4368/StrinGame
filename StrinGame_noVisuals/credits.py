import pygame

# Constants
from config import *
CREDITS_TEXT = [
    "Credits:",
    "Programmed by: Me",
    "Using Pygame library",
    "Made with Visual Studio",
    "Still in progress",
    "Press any key to return to main menu"
]


# Functions
def creditsScreen(window):
    running = True
    font = pygame.font.Font(None, 30)
    text_surfaces = [font.render(line, True, WHITE) for line in CREDITS_TEXT]
    text_rects = [text_surface.get_rect(center=(WIDTH // 2, (i + 1) * 40)) for i, text_surface in enumerate(text_surfaces)]

    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                crossed=True
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False  # Return to main menu on any key press
                crossed=False

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            window.blit(text_surface, text_rect)

        pygame.display.flip()
    if not crossed:
        return 1
    else:
        return 0
pygame.init()
def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Credits Screen Example")
    creditsScreen(window)

if __name__ == "__main__":
    main()
