import random
import copy
import pygame
from config import *


def is_path_exists(maze):
    matrix=copy.deepcopy(maze)
    def dfs(row, col):
        # Check if the current position is outside the matrix or is a wall
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 'N'or matrix[row][col] == 'T':
            return False

        # Mark the current position as visited
        if matrix[row][col] == 'G':
            return True

        matrix[row][col] = 'N'  # Mark as visited

        # Recursively explore adjacent positions
        return (dfs(row + 1, col) or
                dfs(row - 1, col) or
                dfs(row, col + 1) or
                dfs(row, col - 1))

    # Find the start position (1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                # Start DFS from the start position
                return dfs(i, j)

    # If start (1) is not found
    return False


def generate_random_matrix(m, n, num_minus_ones=None):
    if num_minus_ones==None:
        num_minus_ones = (m*n)//4
    # print("M:",m,"N:",n,"factor:",num_minus_ones)
    matrix = [['R' for _ in range(n)] for _ in range(m)]  # Initialize matrix with all zeros
    # Generate random positions for 1, 2, and -1
    S_row= random.randint(0, (m-1)//2)
    S_col= random.randint(0, (n-1)//2)
    G_row= random.randint(2*(((m-1)//2)), m-1)
    G_col= random.randint(2*(((n-1)//2)),n-1)
    
    matrix[S_row][S_col] = 'S'
    matrix[G_row][G_col] = 'G'
    
    # Generate random positions for -1
    for _ in range(num_minus_ones):
        row, col = random.randint(0, m-1), random.randint(0, n-1)
        while row == G_row and col == G_col or  row == S_row and col == S_col:
            row, ccol = random.randint(0, m-1), random.randint(0, n-1)
        matrix[row][col] = 'N'
        row, col = random.randint(0, m-1), random.randint(0, n-1)
        while row == G_row and col == G_col or  row == S_row and col == S_col:
            row, ccol = random.randint(0, m-1), random.randint(0, n-1)
        matrix[row][col] = 'T'
        
    if is_path_exists(matrix):
        return matrix
    else:
        return generate_random_matrix(m, n, num_minus_ones)


# Function to fill the screen with colored squares
def fill_screen(screen, colors_matrix, hero_pos, FONT_SIZE):
    font = pygame.font.Font(None, FONT_SIZE)
    screen.fill(grey)  # Fill the background with a default color

    # Get the size of each square based on the screen size and the number of columns and rows
    cell_width = WIDTH // len(colors_matrix[0])
    cell_height = HEIGHT // len(colors_matrix)

    for row_idx, row in enumerate(colors_matrix):
        for col_idx, color_name in enumerate(row):
            color = color_mapping.get(color_name, grey)  # Get color from the mapping or default to grey
            cell_Xpos=col_idx * cell_width
            cell_Ypos=row_idx * cell_height
            pygame.draw.rect(screen, color, (cell_Xpos,cell_Ypos, cell_width, cell_height))

            # Render the character text
            text_surface = font.render(color_name, True, WHITE)
    
    # Get the position to center the text within the rectangle
            text_rect = text_surface.get_rect(center=(cell_Xpos + cell_width // 2, cell_Ypos + cell_height // 2))

    # Draw the character text on the screen
            screen.blit(text_surface, text_rect)

            # Render the text 'I'
        text_surface = font.render('I', True, BLACK)  # Adjust the color as needed

# Create a rect for the text surface
        text_rect = text_surface.get_rect(center=(hero_pos[0] * cell_width+cell_width // 2, hero_pos[1] * cell_height+ cell_height // 2))

# Blit the text surface onto the screen
        screen.blit(text_surface, text_rect)
            
def start_pos(colors_matrix):
    for i in range(len(colors_matrix[0])):
        for j in range(len(colors_matrix)):
            if colors_matrix[j][i]=='S':
                return [i,j]
    return[1,1]


pygame.init()
if __name__=="__main__":
    M=generate_random_matrix(5,5)
    for i in M:
        print(i)