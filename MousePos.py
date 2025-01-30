import pyautogui
import time
import winsound
import numpy as np
import sounddevice as sd

def beep(frequency=1000, duration=0.3, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()




with open("Positions.txt", "w"):
    pass  # Opening in "w" mode clears the file



for i in range(4):
    time.sleep(3)
    # Get the current mouse position
    x, y = pyautogui.position()
    beep()
    # Open the file in append mode and write both x and y values
    with open("Positions.txt", "a") as file:
        file.write(f"{x}\n")  # Write the x position and move to the next line
        file.write(f"{y}\n")  # Write the y position and move to the next line
        print("Position: ", x, y)   # Print the position on the console
