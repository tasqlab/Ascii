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

title = """ █████╗ ███████╗ ██████╗██╗██╗
██╔══██╗██╔════╝██╔════╝██║██║
███████║███████╗██║     ██║██║
██╔══██║╚════██║██║     ██║██║
██║  ██║███████║╚██████╗██║██║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝"""
write(title, 0.001)
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
    write("""Enter filename. Example: icon.png
or C:/users/user/pictures/icon.png: """)
    file = input("> ")
    column = input("Columns? Enter nothing for default. ")
    if column.strip() == "":
        column = 120
    else:
        column = int(column)

    ascii_art = AsciiArt.from_image(file)
    ascii_art.to_terminal(columns=column, char="█")
