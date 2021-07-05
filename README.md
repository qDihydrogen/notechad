notechad is a free primitive text editor written in Python 3(.9) and Pygame.

## installation
there are two ways to run notechad.
### .exe file
running the .exe file should be all that is necessary. the latest version of notechad can be found [here](https://github.com/qDihydrogen/notechad/releases)
### .py file
to run the python file, you should have the most recent version of Python 3 ([download](https://python.org/downloads)). it is likely that some less recent versions of Python will work. do note that it will not work if you have a version of Python 3 that is below 3.5 as this program uses f-strings which were introduced in 3.5.

using pip in the terminal, you may now enter one of the following to install Pygame:

`pip install pygame`

`pip3 install pygame`

`python -m pip install pygame`

`python3 -m pip install pygame`

this is the library that notechad uses for graphics to show.

you may now run the .py file through the terminal or by double-clicking in the file explorer.

## controls
| KEY | FUNCTION |
|--|--|
| UP | Navigates through lines of text and navigates through settings. If navigating through lines out of range, new lines will be created in place. |
| DOWN | Same as up. |
| LEFT | Used to change settings. |
| RIGHT | Same as left. |
| ENTER | Will allow people to change a specific line in the terminal. |
| LEFT SHIFT | Toggles between document and settings. |
| SPACE | Creates new lines below the selected line. |
| BACKSPACE | Deletes the selected line. |
| ESCAPE | Toggles dark mode. Light mode is on by default. |

## to do

 - general design improvement
 - more customization abilities such as changing colors
 - markdown support
 - put an actual icon for the thing
 - save and load


**Last updated on JULY 5, 2021.**
