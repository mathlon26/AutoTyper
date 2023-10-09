import pyautogui
import time
import random

FILE_PATH = "text.txt"
ORGANIC = True
MIN_DELAY, MAX_DELAY = 0.005, 0.1
PROBABILITY_MULTIPLIER = 0.5 # must be greater then 0.1

# Return delay according to specified min and max values
def get_delay(min:float, max:float):
    return random.uniform(min, max)

# Function to read text file and send keystrokes
def send_keystrokes(file_path:str, mode, minDelay, maxDelay, p):
    with open(file_path, "r") as text:
        lines = text.readlines()
        for line in lines:
            for char in line:
                pyautogui.press(char)
                
                if mode: # randomize delay if ORGANIC variable is True
                    if char == " " or char == "enter": # add extra chance of delay on space/enter keystroke
                        if random.randrange(0, int(round(10 * p))) == 1:
                            delay = get_delay(minDelay + 2, maxDelay + 2)
                            time.sleep(delay)
                            print(delay)
                        else:
                            delay = get_delay(minDelay, maxDelay)
                            time.sleep(delay)
                    else:
                        delay = get_delay(minDelay, maxDelay)
                        time.sleep(delay)
                else: # standard delay
                    time.sleep(minDelay)

if __name__ == '__main__':
    time.sleep(2) # gives time to place the cursor
    send_keystrokes(FILE_PATH, ORGANIC, MIN_DELAY, MAX_DELAY, PROBABILITY_MULTIPLIER)