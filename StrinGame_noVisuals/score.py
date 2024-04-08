import json
import pygame
from config import *
from menu import textBox, Screen

def checkHighScore(score, filename="scores.json"):
    try:
        with open(filename, 'r') as file:
            top_scores = json.load(file)
    except FileNotFoundError:
        pass
    return score>top_scores[len(top_scores)-1]['score']

def update_scores(window, score, name="Player", filename='scores.json'):
    try:
        with open(filename, 'r') as file:
            top_scores = json.load(file)
    except FileNotFoundError:
        top_scores = []

        # Add the new score
    top_scores.append({'rank': -1, 'name': name, 'score': score})

    # Sort the scores by score in descending order
    top_scores.sort(key=lambda x: x['score'], reverse=True)

    # Keep only the top 10 scores
    top_scores = top_scores[:10]
    n=len(top_scores)
    for i in range(n):
        top_scores[i]['rank']=i+1

    # Save the updated scores to file
    with open(filename, 'w') as file:
        json.dump(top_scores, file)

def delete_scores(filename='scores.json'):
    try:
        with open(filename, 'w') as file:
            scores=[]
            for i in range(10):
                scores.append({'rank':i+1, 'name':"No One", 'score':0})
            # for i in range(10):
            #     scores.append({'rank'=i,'name'="No oNe", 'score'=-1})
            json.dump(scores, file)
    except FileNotFoundError:
        pass  # Handle the case where the file doesn't exist gracefully

def load_scores(filename='scores.json'):
    try:
        with open(filename, 'r') as file:
            top_scores = json.load(file)
    except FileNotFoundError:
        top_scores = []
    return top_scores

def highscoresScreen(window):
    highscores = load_scores(filename='scores.json')
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
    center_text.append("Press any key to return to main menu")
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
                if event.key==pygame.K_0:
                    delete_scores()
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

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
    delete_scores()
    # update_scores(window,20)
    pygame.display.set_caption("Main Window")
    
    highscoresScreen(window)

    pygame.quit()
