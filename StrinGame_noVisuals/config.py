grey=GREY = (255 // 2, 255 // 2, 255 // 2)
red=RED=(255,0,0)
yellow=(255,255,0)
green=GREEN=(0,255,0)
BLACK=(0,0,0)
white=WHITE=(255,255,255)
FPS=30

WIDTH=1300
HEIGHT=650

REAL_WIDTH=WIDTH+200
REAL_HEIGHT=HEIGHT+100


cursor_visible=True
cursor_timer=0
text=""
level=5

color_mapping = {
    "N": grey,
    "T": red,
    "S": yellow,
    "R": white,
    "G": green
}

# Define durations (in milliseconds)
burst_duration = 100  # Duration of each burst in milliseconds
# Set the sample rate and bit depth
sample_rate = 44100
# Define musical notes frequencies (in Hz) - halved frequencies for a deeper sound
notes = {
    'C4': 130.81,
    'D4': 146.83,
    'E4': 164.81,
    'F4': 174.61,
    'G4': 196.00,
    'A4': 220.00,
    'B4': 246.94,
    'C5': 261.63
}

# Define durations (in milliseconds)
quarter_note = 500
half_note = 2 * quarter_note
whole_note = 4 * quarter_note
