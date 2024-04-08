import pygame

from config import *

# Function to get user input in real-time
# import sys


def typeHere(screen,title="TITLE", size='normal',screen_width=REAL_WIDTH, screen_height=REAL_HEIGHT, view_all=True):
    input_text = ""
    font = pygame.font.Font(None, 32)  # Change the font size as needed
    screen_width, screen_height = screen.get_size() 
    if size=='normal':
        text_area_width = 700
        text_area_height = 70
        limit=32
    elif size=='big':
        text_area_width = 700
        text_area_height = 70*6
        limit=32*16
        
    
    text_area_x = (screen_width - text_area_width) // 2
    text_area_y = (screen_height - text_area_height) // 2
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key==pygame.K_DELETE:
                    input_text=""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                if len(input_text)<limit:
                    if view_all:
                        if event.unicode.isalnum():
                            input_text +=event.unicode  # Convert WASD to uppercase
                        elif event.key == pygame.K_MINUS:
                            if pygame.key.get_mods() & pygame.KMOD_SHIFT:  # Check for shift modifier
                                input_text += "_"  # Add underscore if shift is pressed
                    else:
                        if event.key==pygame.K_w or event.key==pygame.K_a or event.key==pygame.K_s or event.key==pygame.K_d:
                            input_text +=event.unicode.upper()  # Convert WASD to uppercase
                            
                # else:
                #     input_text = input_text[:-1]

        screen.fill((50, 50, 50))  # Fill the screen with grey color
        pygame.draw.rect(screen, (255//2,255//2,255//2), (text_area_x - 10, text_area_y, text_area_width + 20, text_area_height+50))  # Draw grey rectangle around the white rectangle
        pygame.draw.rect(screen, (255,255,255), (text_area_x, text_area_y+50, text_area_width, text_area_height-30))  # Draw white rectangle
        
        text_surface = font.render(title, True, (255, 255, 255))  # Render text with white color
        
        text_rect = text_surface.get_rect(center=(screen_width // 2, text_area_y+30))  # Align text to center
        y = text_area_y + 70        
        lines = input_text.split('\n')  # Split input_text by newline character
        screen.blit(text_surface, text_rect)  # Blit text surface at the calculated position

        
        for i in range(16):
            text_surface = font.render(input_text[i*32:(i+1)*32], True, (0,0,0))  # Render text with white color
            text_rect = text_surface.get_rect(center=(screen_width // 2, y))  # Align text to center
            screen.blit(text_surface, text_rect)  # Blit text surface at the calculated position
            y += font.get_linesize()  # Increment y coordinate by line height

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)  # Set desired FPS


def level_bar(window, level):
    level_text=str(level)
    menuBox(window, 100, 100, "level", text=level_text, x=WIDTH+(REAL_WIDTH-WIDTH)//4, y=50)
    
def score_bar(window, score):
    score_text=str(score)
    menuBox(window, 100, 100, "score", text=score_text, x=WIDTH+(REAL_WIDTH-WIDTH)//4, y=250)
    
def life_bar(window, life):
    life_text=str(life)
    menuBox(window, 100, 100, "life", text=life_text, x=WIDTH+(REAL_WIDTH-WIDTH)//4, y=450)
    
def time_bar(window, total_time, elapsed_time):
    life_text=str(int((total_time-elapsed_time)/1000))
    menuBox(window, 100, 100, "time", text=life_text, x=WIDTH+(REAL_WIDTH-WIDTH)//4, y=650)
    
def string_bar(window, string):
    string_text=string[:32]
    menuBox(window, 750, 100, "String", text=string_text, x=(REAL_WIDTH-WIDTH), y=650)
    
def display_bars(window, level, score, life, total_time, elapsed_time, string):
    life_bar(window, life)
    score_bar(window, score)
    level_bar(window, level)
    time_bar(window, total_time, elapsed_time)
    string_bar(window, string)


def enterString(input_text, limit=16):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # Check if the key pressed is alphanumeric
            if event.unicode.isalnum() and len(input_text)<limit:
                return input_text + event.unicode
            elif event.key == pygame.K_BACKSPACE:
                # If backspace is pressed, remove the last character from input_text
                if len(input_text) > 0:
                    return input_text[:-1]
            elif event.key == pygame.K_DELETE:
                return ""
            elif event.key==pygame.K_RETURN:
                return input_text+"\n"
    return input_text

def enterDirection(input_text, limit=16):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d) and len(input_text) < limit:
                return input_text + event.unicode.upper()
            elif event.key == pygame.K_BACKSPACE:
                if len(input_text) > 0:
                    return input_text[:-1]
            elif event.key == pygame.K_DELETE:
                return ""
            elif event.key == pygame.K_RETURN:
                return input_text + "\n"
    return input_text

def enterNum(input_text):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # Check if the key pressed is alphanumeric
            if event.unicode.isdigit() and len(input_text)<2:
                return input_text + event.unicode
            elif event.key == pygame.K_BACKSPACE:
                # If backspace is pressed, remove the last character from input_text
                if len(input_text) > 0:
                    return input_text[:-1]
            elif event.key == pygame.K_DELETE:
                return ""
    return input_text

def menuBox(window, width, height, title="title", color=GREY, text_size=32, x=None, y=None, top_region_color=WHITE, text=None):
    if x is None:
        x = (REAL_WIDTH // 2 - width // 2)
    if y is None:
        y = (REAL_HEIGHT // 2 - height // 2)
    menu_surface = pygame.Surface((width, height), pygame.SRCALPHA)  # Create a surface with per-pixel alpha for transparency
    menu_surface.fill((0, 0, 0, 0))  # Fill with transparent color
    
    # Fill top region with a different color
    top_region_rect = pygame.Rect(text_size // 2, 0 + 10, width - text_size, text_size)
    pygame.draw.rect(menu_surface, top_region_color, top_region_rect)
    
    # Draw round-edged rectangle
    round_rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(menu_surface, color, round_rect, border_radius=10)  # Draw the round-edged rectangle
    
    # Render text
    font = pygame.font.Font(None, text_size)  # You can specify a font file or use None for default font
    title_surface = font.render(title, True, (0, 0, 0))  # Text, antialiasing, color
    text_rect = title_surface.get_rect(center=(width // 2, text_size // 2 + 10))  # Center the text
    
    # Blit text onto menu surface
    menu_surface.blit(title_surface, text_rect)
    
    # Draw textbox
    textbox_rect = pygame.Rect(text_size // 2, text_size * 1.5, width - text_size, text_size)  # Define the rect for the textbox
    # Blit text onto menu surface
    menu_surface.blit(title_surface, textbox_rect)
    pygame.draw.rect(menu_surface, WHITE, textbox_rect, border_radius=10)  # Draw the textbox
    
    if text!=None:
        input_text_surface=font.render(text, True, BLACK)  # Text, antialiasing, color
        input_text_rect =pygame.Rect(text_size, text_size * 1.7, width - text_size, text_size)
        menu_surface.blit(input_text_surface,input_text_rect)
        

    window.blit(menu_surface, (x, y))
    
    return menu_surface


def textBox(window, width, height,text, title="title", color=GREY, text_size=32, x=None, y=None, top_region_color=WHITE, limit=16):
    # global text
    if x is None:
        x = (WIDTH // 2 - width // 2)
    if y is None:
        y = (HEIGHT // 2 - height // 2)
    menu_surface = pygame.Surface((width, height), pygame.SRCALPHA)  # Create a surface with per-pixel alpha for transparency
    menu_surface.fill((0, 0, 0, 0))  # Fill with transparent color
    
    # Fill top region with a different color
    top_region_rect = pygame.Rect(text_size // 2, 0 + 10, width - text_size, text_size)
    pygame.draw.rect(menu_surface, top_region_color, top_region_rect)
    
    # Draw round-edged rectangle
    round_rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(menu_surface, color, round_rect, border_radius=10)  # Draw the round-edged rectangle
    
    # Render text
    font = pygame.font.Font(None, text_size)  # You can specify a font file or use None for default font
    title_surface = font.render(title, True, (0, 0, 0))  # Text, antialiasing, color
    text_rect = title_surface.get_rect(center=(width // 2, text_size // 2 + 10))  # Center the text
    
    # Blit text onto menu surface
    menu_surface.blit(title_surface, text_rect)
    
    # Draw textbox
    textbox_rect = pygame.Rect(text_size // 2, text_size * 1.5, width - text_size, text_size)  # Define the rect for the textbox
    # Blit text onto menu surface
    menu_surface.blit(title_surface, textbox_rect)
    pygame.draw.rect(menu_surface, WHITE, textbox_rect, border_radius=10)  # Draw the textbox
    
    text=enterDirection(text, limit)
    if text=="":
        input_text_surface=font.render("Start Typing", True, GREY)  # Text, antialiasing, color
    else:
        input_text_surface=font.render(text, True, BLACK)  # Text, antialiasing, color
    input_text_rect =pygame.Rect(text_size, text_size * 1.7, width - text_size, text_size)
    menu_surface.blit(input_text_surface,input_text_rect)

    window.blit(menu_surface, (x, y))
    
    return text







def Screen(window, text_to_show, aling='center'):
    font = pygame.font.Font(None, 30)
    text_surfaces = []
    text_rects = []

    for line in text_to_show:
        if isinstance(line, tuple):  # Check if the line contains text and font size
            text = line[0]
            font_size = line[1]
            font = pygame.font.Font(None, font_size)
            text_surface = font.render(text, True, WHITE)
        else:
            text_surface = font.render(line, True, WHITE)

        text_surfaces.append(text_surface)
        if aling=='center':
            text_rect = text_surface.get_rect(center=(REAL_WIDTH // 2, (len(text_surfaces) + 1) * 50))
        elif aling=='left':
            text_rect = text_surface.get_rect(center=(REAL_WIDTH // 10, (len(text_surfaces) + 1) * 50))
        if aling=='right':
            text_rect = text_surface.get_rect(center=(9*REAL_WIDTH // 10, (len(text_surfaces) + 1) * 50))
        
        text_rects.append(text_rect)
        
    return text_surfaces, text_rects


if __name__=="__main__":
# Example usage
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Main Window")






    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window.fill((255, 0, 0))  # Fill main window with white
        # Blit the menu surface onto the main window
        text=textBox(window,400, 100, text, "Enter your name")  # Creating menu surface
        pygame.display.flip()

    pygame.quit()
