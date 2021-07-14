notechad is a free primitive text editor written in Python 3(.9) and Pygame.

## installation
there are two ways to run notechad.
### .exe file
running the .exe file should be all that is necessary. **THE EXECUTABLE MIGHT ONLY WORK ON WINDOWS 10.** the latest version of notechad can be found [here](https://github.com/qDihydrogen/notechad/releases)
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
| LEFT CTRL | Saves your lines and outputs them to a file output.txt. |
| RIGHT CTRL | Loads from output.txt after given permission through user input. |
| TAB | Jump to a line. |

## to do

 - general design improvement
 - more customization abilities such as changing colors
 - markdown support
 - put an actual icon
 - comment the code

## permissions
kinda do whatever? just don't claim that notechad is yours and i'll most likely be fine.
some things that you may do if you want include
 - translations
 - forks and other modifications
 - pull requests if you really want (though i might not accept them!)
 - make binaries for other OS's such as Mac OS X and Linux


**Last updated on JULY 9, 2021.**
