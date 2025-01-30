import time
import pyautogui
import keyboard
import threading

def readline(filename, line):
    """
    Reads a specific line from a file.
    :param filename: The name of the file to read from.
    :param line: The line number to read (1-based index).
    :return: The content of the specified line, or None if the line does not exist.
    """
    try:
        with open(filename, 'r') as file:
            for current_line_number, content in enumerate(file, start=1):
                if current_line_number == line:
                    return content.strip()  # Strip removes trailing newline
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")
    
    return None

# Declare tile positions at the start
try:
    tile_positions = [
        (int(readline("Positions.txt", 1)), int(readline("Positions.txt", 2))),
        (int(readline("Positions.txt", 3)), int(readline("Positions.txt", 4))),
        (int(readline("Positions.txt", 5)), int(readline("Positions.txt", 6))),
        (int(readline("Positions.txt", 7)), int(readline("Positions.txt", 8)))
    ]
except Exception as e:
    print(f"Error: {e}")

def start_tiles():
    """
    Moves to each tile position, checks for a specific color, and clicks if found.
    """
    try:
        for x, y in tile_positions:
            pyautogui.moveTo(x, y)
            pixel_color = pyautogui.pixel(x, y)
            print(f"Pixel at ({x}, {y}): {pixel_color}")
            if pixel_color == (54, 159, 198):
                pyautogui.click(x, y)
                print(f"Clicked on tile at ({x}, {y})")
                break
    except Exception as e:
        print(f"Error: {e}")

def check_tile(x, y):
    """
    Continuously checks a single tile and clicks it if necessary.
    """
    while True:
        if keyboard.is_pressed('q'):
            break
        pixel_color = pyautogui.pixel(x, y)
        if pixel_color == (0, 0, 0):  # If the tile matches the color
            pyautogui.click(x, y)
            print(f"Clicked on tile at ({x}, {y})")
        time.sleep(0.01)  # Small delay to avoid overloading the CPU

# Initial loop waiting for 's' to start
while True:
    if keyboard.is_pressed('s'):
        break

# Execute the `start_tiles()` function first
start_tiles()

# Start checking all tiles simultaneously
tile_threads = []
for x, y in tile_positions:
    thread = threading.Thread(target=check_tile, args=(x, y))
    thread.start()
    tile_threads.append(thread)

# Wait for all threads to finish when 'q' is pressed
for thread in tile_threads:
    thread.join()

print("Exited.")
