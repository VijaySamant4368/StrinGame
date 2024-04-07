import pygame

from config import *

# Function to get user input in real-time
# import sys

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
