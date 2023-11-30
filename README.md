# Keystroke Generator

This is a Python program that simulates keystrokes based on the contents of a text file. The program uses the `pyautogui` library to send keystrokes to the active window. You can use this program for various purposes, such as automating text input or testing applications that rely on keyboard input.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Installation

Before using the program, you need to install the required Python packages. These dependencies are listed in the `requirements.txt` file. To install them, you can use pip:

```
pip install -r requirements.txt
```
## Usage
Once you've installed the required packages, you can run the program by executing the ```main.py``` script. Here's an example of how to use it:

```
python main.py
```

The program will read the contents of the ```text.txt``` file and simulate keystrokes for each character. By default, it uses a standard delay between keystrokes. However, you can configure it to add randomness to the delay for a more organic typing effect.
The script will wait for 2 seconds to give you time to place the cursor in the desired input field or application.
Once the cursor is in position, the script will start typing the contents of the specified text file using the configured settings.

## Configuration
You can configure the behavior of the keystroke generator by editing the variables in the script:

```FILE_PATH```: This variable specifies the path to the text file containing the text you want to type.

```ORGANIC```: Set this variable to True if you want to add randomness to the typing delay. If set to False, the program will use a standard delay.

```MIN_DELAY``` and ```MAX_DELAY```: These variables define the range of delay (in seconds) between keystrokes. If ORGANIC is set to True, the program will randomly select a delay within this range for each character.

```PROBABILITY_MULTIPLIER```: This variable determines the probability of adding extra delay for space and enter keystrokes when ORGANIC is True. A higher value increases the likelihood of additional delay. It must be greater than 0.1.

For example:
```
# Configuration
FILE_PATH = "text.txt"             # Path to the text file to type
ORGANIC = True                     # Enable organic typing (random delays)
MIN_DELAY, MAX_DELAY = 0.005, 0.1  # Minimum and maximum typing delays (in seconds)
PROBABILITY_MULTIPLIER = 0.5       # Probability multiplier for extra delays
```

## License
Do with this as you wish.

### Disclaimer
Please use AutoTyper responsibly and in compliance with all relevant laws and regulations. Automated typing should only be used for legitimate and ethical purposes.
Feel free to customize and use this keystroke generator according to your needs. If you have any questions or encounter issues, please don't hesitate to reach out to the developer or the community for assistance. Happy typing!
