AutoTyper README
AutoTyper is a Python script that simulates keyboard input by reading a text file and sending keystrokes to the active application. This can be useful for automating tasks that involve typing text, such as filling out forms or generating repetitive content. AutoTyper also offers the option to add a level of randomness to the typing to make it appear more organic.

Usage
To use AutoTyper, follow these steps:

Make sure you have Python installed on your system. You can download it from python.org.

Install the required packages by running the following command:

shell
Copy code
pip install pyautogui
Place the text you want to type in a text file and specify its path in the FILE_PATH variable.

Configure the script's behavior by adjusting the following variables:

ORGANIC: Set this to True if you want to introduce randomness in typing to make it appear more natural. Set it to False for standard, consistent typing.
MIN_DELAY and MAX_DELAY: These variables control the minimum and maximum delay (in seconds) between keystrokes. Adjust these values to control the typing speed.
PROBABILITY_MULTIPLIER: This variable influences the probability of adding an extra delay on space or enter keystrokes when ORGANIC is set to True. Increase this value to increase the chances of extra delays.
Run the script by executing the following command in your terminal:

shell
Copy code
python autotyper.py
The script will wait for 2 seconds to give you time to place the cursor in the desired input field or application.

Once the cursor is in position, the script will start typing the contents of the specified text file using the configured settings.

Example
Here's an example of how to use AutoTyper with an explanation of the settings:

python
Copy code
# Configuration
FILE_PATH = "text.txt"             # Path to the text file to type
ORGANIC = True                     # Enable organic typing (random delays)
MIN_DELAY, MAX_DELAY = 0.005, 0.1  # Minimum and maximum typing delays (in seconds)
PROBABILITY_MULTIPLIER = 0.5       # Probability multiplier for extra delays

# ... (other settings)

if __name__ == '__main__':
    time.sleep(2)  # Wait for 2 seconds before typing
    send_keystrokes(FILE_PATH, ORGANIC, MIN_DELAY, MAX_DELAY, PROBABILITY_MULTIPLIER)
In this example, the script will type the content of text.txt with organic typing, randomizing delays between keystrokes, and introducing extra delays on space or enter keystrokes with a 50% probability multiplier.

Feel free to modify the configuration to suit your specific needs.

Disclaimer
Please use AutoTyper responsibly and in compliance with all relevant laws and regulations. Automated typing should only be used for legitimate and ethical purposes.
