import time
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Get the countdown time from user input
countdown_time = int(input("Enter countdown time in seconds: "))

# Countdown loop
while countdown_time:
    mins, secs = divmod(countdown_time, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    countdown_time -= 1

# Play alarm sound when countdown is complete
print("Time's up!")
pygame.mixer.music.load(os.path.abspath("alarm.mp3"))
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()
