# Task 1: Your Mood Tracker

import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times_of_day = ['morning', 'afternoon', 'evening']
moods = ['happy', 'sad', 'energetic', 'calm']

for day in days:
    for time in times_of_day:
        random_mood = random.choice(moods)
        print(f"On {day} {time}, you were {random_mood}.")