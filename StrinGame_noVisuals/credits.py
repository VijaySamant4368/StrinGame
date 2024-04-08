import pygame

# Constants
from config import *
from menu import Screen

# Functions
def creditsScreen(window):
    CREDITS_TEXT = [
    ("Credits:",100),  # Tuple containing text and font size for title
    "",
    ("Programmed by: Me",50),
    "Using Pygame library",
    "Made with Visual Studio",
    "Still in progress",
    "Press any key to return to main menu"
]
    
    running = True
    text_surfaces, text_rects=Screen(window, CREDITS_TEXT)
    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                crossed = True
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False  # Return to main menu on any key press
                crossed = False

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            window.blit(text_surface, text_rect)

        pygame.display.flip()

    if not crossed:
        return 1
    else:
        return 0

def main():
    pygame.init()
    window = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
    pygame.display.set_caption("Credits Screen Example")
    creditsScreen(window)

if __name__ == "__main__":
    main()
