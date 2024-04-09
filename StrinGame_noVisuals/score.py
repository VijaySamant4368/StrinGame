import json
import pygame
from config import *
from screen import highscoresScreen

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

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
    delete_scores()
    # update_scores(window,20)
    pygame.display.set_caption("Main Window")
    
    highscoresScreen(window, load_scores(filename='scores.json'))

    pygame.quit()
