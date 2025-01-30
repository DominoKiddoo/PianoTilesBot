import pyautogui
import time
import winsound


with open("Positions.txt", "w"):
    pass  # Opening in "w" mode clears the file



for i in range(4):
    time.sleep(3)
    winsound.Beep(500, 200)
    # Get the current mouse position
    x, y = pyautogui.position()
    
    # Open the file in append mode and write both x and y values
    with open("Positions.txt", "a") as file:
        file.write(f"{x}\n")  # Write the x position and move to the next line
        file.write(f"{y}\n")  # Write the y position and move to the next line
        print("Position: ", x, y)   # Print the position on the console
