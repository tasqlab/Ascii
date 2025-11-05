import pyfiglet
from pyfiglet import FigletFont
from ascii_magic import AsciiArt
import time
import sys

def write(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

mode = input("What mode? Text or Image? ")

if mode.lower() == "text": 
    write('Enter your text. Type "fonts" for fonts (while in what font)')
    text = input("What text? ")
    font = input("What font? Enter nothing for default. ")
    if font == "fonts":
        font = FigletFont.getFonts()
        print("Available fonts:", font)
    font = input("What font? Enter nothing for default. ")
    if font == "":
        font = "standard"
    ascii_art = pyfiglet.figlet_format(text, font=font)
    write(ascii_art, 0.001)

elif mode.lower() == "image":
    file = input("Enter file name. Example: icon.png ")
    ascii_art = AsciiArt.from_image(file)
    ascii_art.to_terminal(columns=60)
