import pygame

# Constants
from config import *
from menu import Screen, menuBox


# Functions
def creditsScreen(window):
    CREDITS_TEXT = [
    ("Credits:",100),  # Tuple containing text and font size for title
    "",
    ("Programmed by: Me",50),
    "Using Pygame library",
    "Made with Visual Studio",
    "Still in progress","","","","","","",
    ("Press any key to return to main menu",30)
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

def mainMenu(window):
    running = True
    while running:
        window.fill((0, 0, 0))
        menu = menuBox(window, 400, 300, "Main Menu", WHITE, 50, top_region_color=GREY)
        menu_rect = menu.get_rect(center=(REAL_WIDTH // 2, REAL_HEIGHT // 2))
        options = ["Play", "ShowHighScores", "Settings", "Credits and stuffs","How To Play", "Exit"]
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
                    return 1
                    # Perform action for Play option
                elif event.key == pygame.K_2:
                    return 2
                    # Perform action for ShowHighScores option
                elif event.key == pygame.K_3:
                    # Perform action for Settings option
                    return 3
                elif event.key == pygame.K_4:
                    # Perform action for Credits and stuffs option
                    return 4
                elif event.key == pygame.K_5:
                    return 5
                elif event.key == pygame.K_6:
                    return 6
                    pygame.quit()
                    running = False

def highscoresScreen(window, highscores):
    center_text=[
        ("High Scores:" ,100),
        ("", 50)
    ]
    left_text=[
        ("", 100),
        ("", 50)
    ]
    right_text=[
        ("", 100),
        ("",50)
    ]
    for i in range(len(highscores)):
        center_text.append( str(highscores[i]['name']) )
        left_text.append(str(i+1)+".")
        right_text.append(str(highscores[i]['score']))
    center_text.append(("Press Delete to delete HIghScores and any other key to return to main menu",30))
    running = True
    center_text_surfaces, center_text_rects=Screen(window, center_text)
    left_text_surfaces, left_text_rects=Screen(window, left_text, aling='left')
    right_text_surfaces, right_text_rects=Screen(window, right_text, aling='right')
    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                crossed = True
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_DELETE:
                    return -1
                running = False  # Return to main menu on any key press
                crossed = False

        for text_surface, text_rect in zip(center_text_surfaces, center_text_rects):
            window.blit(text_surface, text_rect)
        for text_surface, text_rect in zip(left_text_surfaces, left_text_rects):
            window.blit(text_surface, text_rect)
        for text_surface, text_rect in zip(right_text_surfaces, right_text_rects):
            window.blit(text_surface, text_rect)

        pygame.display.flip()

    if not crossed:
        return 1
    else:
        return 0

def howToPlay(window):
    TEXT=[
    ("How To Play:",80),  # Tuple containing text and font size for title
    "","",
    ("A random maze will appear on the screen made with",40),
    " colored rectangles and some characters on it","",
    "Their meanings are S:'Start' (Yellow), T:'Trap' (Red)",
    " R:'Route' (White), N:'Null' (Grey), G:'Goal' (Green)",
    "The player is represented by 'I'","",
    "Player starts at START and the goal is to reach GOAL",
    " while avoiding TRAPS that traps you on the ROUTE fon the route that I will take","","","","",
    ("Press 0 to view more or any other key to go to MainMenu", 30)
]
    
    running = True
    text_surfaces, text_rects=Screen(window, TEXT,height=40)
    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                crossed = True
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    TEXT=[
    ("How To Play:",80),"","",  # Tuple containing text and font size for title
    ("A random maze will appear on the screen made with",40),
    " colored rectangles and some characters on it","",
    "Their meanings are S:'Start' (Yellow), T:'Trap' (Red)",
    " R:'Route' (White), N:'Null' (Grey), G:'Goal' (Green)",
    "The player is represented by 'I'","",
    "Player starts at START and the goal is to reach GOAL",
    " while avoiding TRAPS that traps you on the ROUTE fon the route that I will take","","","","",
    ("Press 0 to view more or any other key to go to MainMenu",30)
]
                    text_surfaces, text_rects=Screen(window, TEXT, height=40)
                    
                elif event.key==pygame.K_0:
                    TEXT=[
    ("How To Play:",80),"","",  # Tuple containing text and font size for title
    ("When the maze is in view, focus on it with focus",40),"",
    "When the time reaches 0, you will no longer be able to watch the maze","",
    "Enter the string of WASDs, corresponding to the Up, Left",
    "Down, Right direction respectively, and press Enter","",
    "It will start moving acoording to the string provided","",
    "If the player reaches Goal, next, more difficult will appear",
    "Else if you have attempts left, the time will restart",
    "and the process continues, till you have reached goal, ended your attempts, or life","",
    ("Press 1 to go back, or any other key to go to MainMenu", 30)
                    ]    
                    text_surfaces, text_rects=Screen(window, TEXT, height=40)
                else:              
                    running = False  # Return to main menu on any key press
                    crossed = False

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            window.blit(text_surface, text_rect)

        pygame.display.flip()

    if not crossed:
        return 1
    else:
        return 0
    