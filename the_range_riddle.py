# Task 1

import random

moods = ['happy', 'sad', 'energetic', 'calm']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
    todays_mood = random.choice(moods)
    print(f"On {day}, you were feeling {todays_mood}")

