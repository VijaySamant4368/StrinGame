import pygame

pygame.init()

# Initialize text input variable

from menu import menuBox
from config import *

def mainMenu(window):
    running = True
    while running:
        window.fill((0, 0, 0))
        menu = menuBox(window, 400, 300, "Main Menu", WHITE, 50, top_region_color=GREY)
        menu_rect = menu.get_rect(center=(REAL_WIDTH // 2, REAL_HEIGHT // 2))
        options = ["Play", "ShowHighScores", "Settings", "Credits and stuffs", "Exit"]
        option_rects = []
        for i, option in enumerate(options):
            option_text = pygame.font.Font(None, 30).render(f"{i+1}: {option}", True, BLACK)
            option_rect = option_text.get_rect(center=(menu_rect.centerx, menu_rect.centery  + (i-2) * 40+20))
            option_rects.append(option_rect)
            window.blit(option_text, option_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("User selected option 1: Play")
                    return 1
                    # Perform action for Play option
                elif event.key == pygame.K_2:
                    print("User selected option 2: ShowHighScores")
                    return 2
                    # Perform action for ShowHighScores option
                elif event.key == pygame.K_3:
                    print("User selected option 3: Settings")
                    # Perform action for Settings option
                    return 3
                elif event.key == pygame.K_4:
                    print("User selected option 4: Credits and stuffs")
                    # Perform action for Credits and stuffs option
                    return 4
                elif event.key == pygame.K_0:
                    print("User selected option 0: Exit")
                    return 0
                    pygame.quit()
                    running = False

def level_bar(window, level):
    level_text=str(level)
    menuBox(window, 100, 100, "level", text=level_text, x=WIDTH+(REAL_WIDTH-WIDTH)//2, y=100)
    level=int(level)
    pygame.display.flip()
    
def score_bar(window, score):
    score_text=str(score)
    menuBox(window, 100, 100, "score", text=score_text, x=WIDTH+(REAL_WIDTH-WIDTH)//2, y=300)
    score=int(score)
    pygame.display.flip()
    
def life_bar(window, life):
    life_text=str(life)
    menuBox(window, 100, 100, "life", text=life_text, x=WIDTH+(REAL_WIDTH-WIDTH)//2, y=500)
    life=int(life)
    pygame.display.flip()
    
def display_bars(window, level, score, life):
    life_bar(window, life)
    score_bar(window, score)
    level_bar(window, level)
    
# Main loop
def main():
    level=0
    while level<500:
        window = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
        pygame.display.set_caption("Main Menu Example")
        level_bar(window, level)
        # mainMenu(window)

if __name__ == "__main__":
    main()
