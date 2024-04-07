import pygame
import time


from config import *

from menu import textBox
from map import generate_random_matrix, fill_screen, start_pos

from sound import victory_sound, thornSound

from menuScreen import mainMenu, display_bars
from credits import creditsScreen

import pygame
import sys
import time

FPS=30
clock=pygame.time.Clock()
FONT_SIZE=50

life=1
def ouch( life,damage=1):
    life-=damage
    return life
def null():
    pass
def victory():
    pass

def removeThorn(matrix,x,y):
    if matrix[y][x]=="T":
        thornSound()
        matrix[y][x]="R"

def checkUp(map, pos_x, pos_y):
    if(pos_y<=0):
        return "NULL"
    else:
        temp=(map[pos_y-1][pos_x])
        if temp=="N":
            return "NULL"
        elif temp=="T":
            return "THORN"
        elif temp=="F":
            return "FINISH"
        elif temp=="S" or temp=="R":
            return "ROUTE"
        elif temp=="G":
            return "GOAL"
def checkDown(map, pos_x, pos_y):
    if(pos_y>=len(map)-1):
        return "NULL"
    else:
        temp=(map[pos_y+1][pos_x])
        if temp=="N":
            return "NULL"
        elif temp=="T":
            return "THORN"
        elif temp=="F":
            return "FINISH"
        elif temp=="S" or temp=="R":
            return "ROUTE"
        elif temp=="G":
            return "GOAL"
def checkLeft(map, pos_x, pos_y):
    if(pos_x<=0):
        return "NULL"
    else:
        temp=(map[pos_y][pos_x-1])
        if temp=="N":
            return "NULL"
        elif temp=="T":
            return "THORN"
        elif temp=="F":
            return "FINISH"
        elif temp=="S" or temp=="R":
            return "ROUTE"
        elif temp=="G":
            return "GOAL"
def checkRight(map, pos_x, pos_y):
    if(pos_x>=len(map[0])-1):
        return "NULL"
    else:
        temp=(map[pos_y][pos_x+1])
        if temp=="N":
            return "NULL"
        elif temp=="T":
            return "THORN"
        elif temp=="F":
            return "FINISH"
        elif temp=="S" or temp=="R":
            return "ROUTE"
        elif temp=="G":
            return "GOAL"

def nextLevel(level, score, life):
    victory_sound()
    global FONT_SIZE
    level+=1
    print("Current Level",level)
    print(FONT_SIZE)
    temp=level//5*5
    FONT_SIZE-=1
    new_level=generate_random_matrix(temp, temp, (level*level)//10)
    x,y =start_pos(new_level)# Store the initial time
    initial_time = pygame.time.get_ticks()
    return x,y,new_level, level, initial_time, score*life

def handle_movement(window, string, matrix, x, y):
    for char in string:
        if char=="w":
            up=checkUp(matrix, x,y)
            if up=="ROUTE":
                y-=1
                # moveUp(x,y)
            elif up=="THORN":
                removeThorn(matrix, x,y-1)
                ouch()
            elif up=="GOAL":
                y-=1
                x,y,matrix,level,initial_time=nextLevel(level)
            









    # Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
    # Set up the display
pygame.display.set_caption("StrinGame")

# Run the game loop
def play(screen):


    # Set up fonts
    font = pygame.font.Font(None, FONT_SIZE)

    # m=n=5
    # matrix = generate_random_matrix(m, n)

    level=4
    life=3
    score=1
    string=""
    moved=False
    ready=False
    x,y,matrix,level, initial_time, score=nextLevel(5, 1,1)
    visible=True
    typed=False

    # Initial position of the hero
    x,y=start_pos(matrix)

    hero=pygame.rect.Rect(x,y,50,50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:                #Key pressed *AND RELEASED*
                # handleMovement(matrix, event.key)
                pass
        if typed:
            for ch in string :
                if ch=="W":
                    up=checkUp(matrix, x,y)
                    if up=="ROUTE":
                        y-=1
                        # moveUp(x,y)
                    elif up=="THORN":
                        removeThorn(matrix, x,y-1)
                        life=ouch(life)
                    elif up=="GOAL":
                        y-=1
                        x,y,matrix,level,initial_time,score=nextLevel(level, life, score)
                        visible=True
                        typed=False
                        break
                        
                if ch=="S":
                    down=checkDown(matrix, x,y)
                    if down=="ROUTE":
                        y+=1
                        # moveUp(x,y)
                    elif checkDown(matrix, x,y)=="THORN":
                        removeThorn(matrix, x,y+1)
                        life=ouch(life)
                    elif down=="GOAL":
                        y+=1
                        x,y,matrix,level,initial_time,score=nextLevel(level, life, score)
                        visible=True
                        typed=False
                        break
                        
                if ch=="A":
                    left=checkLeft(matrix, x,y)
                    if left=="ROUTE":
                        x-=1
                        # moveUp(x,y)
                    elif checkLeft(matrix, x,y)=="THORN":
                        removeThorn(matrix, x-1,y)
                        life=ouch(life)
                    elif left=="GOAL":
                        x-=1
                        x,y,matrix,level,initial_time,score=nextLevel(level, life, score)
                        visible=True
                        typed=False
                        break
                        
                if ch=="D":
                    right=checkRight(matrix, x,y)
                    if right=="ROUTE":
                        x+=1
                        # moveUp(x,y)
                    elif checkRight(matrix, x,y)=="THORN":
                        removeThorn(matrix, x+1,y)
                        life=ouch(life)
                    elif right=="GOAL":
                        x+=1
                        x,y,matrix,level,initial_time,score=nextLevel(level, life, score)
                        visible=True
                        typed=False
                        break
                
                fill_screen(screen, matrix, (x,y), FONT_SIZE)
                display_bars(screen, level, score, life)      
                pygame.display.flip()
                time.sleep(0.3)
            string=""
    #string=enterString()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            x,y,matrix,level,initial_time=nextLevel(level)
            visible=True
            typed=False
            time.sleep(0.3)
            
        
            # Calculate the elapsed time
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - initial_time
        if elapsed_time>1000:
            visible=False
        
        if not visible and not typed:
            while string=="" or string[-1]!="\n":
                string=textBox(screen, (WIDTH*9)//10, HEIGHT//4, string, "ENTER YOUR STRING", limit=48)
                pygame.display.flip()
            typed=True
            visible=True
            # string=""
            
        else:
            fill_screen(screen, matrix, (x,y), FONT_SIZE)

        clock.tick(FPS)


        display_bars(screen, level, score, life)
        
        pygame.display.flip()
        if level>=50:
            return level, life

def homeScreen(screen):
    ans=(mainMenu(screen))
    if ans==1:
        curLevel, curLife= play(screen)
        addHighScore (curLevel, curLife)
    elif ans==4:
        if creditsScreen(screen):
            homeScreen(screen)

if __name__=="__main__":
    # pygame.init()
    homeScreen(screen)
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         break

# Quit Pygame
pygame.quit()
sys.exit()
