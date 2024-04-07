import pygame
import math
import struct
import random

# Initialize Pygame
pygame.init()

# Set the sample rate and bit depth
sample_rate = 44100

from config import sample_rate, notes, burst_duration, half_note, quarter_note, whole_note


def victory_sound():
    # Generate a melody
    melody = [
        ('C4', quarter_note),
        ('D4', quarter_note),
        ('E4', quarter_note),
        ('C4', quarter_note),
        ('E4', quarter_note),
        ('F4', quarter_note),
        ('E4', half_note),
        ('F4', quarter_note),
        ('G4', quarter_note),
        ('A4', quarter_note),
        ('F4', quarter_note),
        ('G4', half_note),
        ('A4', quarter_note),
        ('B4', quarter_note),
        ('C5', whole_note)
    ]

    # Generate the sound buffer for the melody
    sound_buffer = bytearray()
    for note, duration in melody:
        frequency = notes[note]
        samples = [int(127 * math.sin(2 * math.pi * frequency * t / sample_rate)) for t in range(int(sample_rate * duration / 1000))]
        sound_buffer.extend(struct.pack('b' * len(samples), *samples))

    # Create a Pygame sound object
    sound= pygame.mixer.Sound(buffer=sound_buffer)

    # Play the melody
    sound.play()

    # Wait for the melody to finish playing
    pygame.time.wait(sum(duration for _, duration in melody)//11)


def generate_burst():
    # Function to generate a burst of noise
    burst_samples = [random.randint(0, 255) for _ in range(int(sample_rate * burst_duration / 1000))]
    return bytearray(burst_samples)


def thornSound():
    # Generate the sound buffer for the metal clinging effect
    sound_buffer = bytearray()
    for _ in range(10):  # Generate 10 bursts
        sound_buffer.extend(generate_burst())

    # Create a Pygame sound object
    sound = pygame.mixer.Sound(buffer=sound_buffer)

    
    sound.play()
    pygame.time.wait(len(sound_buffer) * 100 // sample_rate)

if __name__=="__main__":
    thornSound()
    victory_sound()

# Quit Pygame
pygame.quit()
