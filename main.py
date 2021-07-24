import pygame
import time
import math
pygame.init()  # innit pygame haha bri'ish funy why am i making this program

import cProfile
import pstats

# WINDOW ---------------------------------------------------------------------
width = 900
height = 900
window = pygame.display.set_mode((width, height))  # makes a 900x900 window
pygame.display.set_caption('Notechad')

# THIS THING ENSURES A 60FPS EXPERIENCE --------------------------------------
clock = pygame.time.Clock()
FPS = 60

# TEXT -----------------------------------------------------------------------
text = pygame.font.Font('font/dogicapixel.ttf', 14)
foot = pygame.font.Font('font/dogicapixel.ttf', 36)
back_color = (255, 255, 255)
text_color = (0, 0, 0)
foot_text = foot.render('Check the terminal!', True, text_color)

# BASICALLY THE TEXT FILE ----------------------------------------------------
lines = ['']

# TOO ATTACHED I GUESS TO DELETE THIS LMAO
# for i in range(10):
#     lines.append(f'words words words #{i+1}')  # Filler. COMMENT OUT ONCE READY TO.

# SELECTION, WILL USE LATER FOR MARKDOWN SUPPORT -----------------------------
selection = [0, 0]

action = 'scroll'

# SELECTIONS, LINES AND OPTIONS ----------------------------------------------
line_sel = 0
opt_sel = 0

dark_mode = False

# CUSTOMIZATION --------------------------------------------------------------
line_offset = 20
left_offset = 50
between_offset = 10
top_offset = 10
scroll_threshold = 650
border_thickness = 2

# KEYS -----------------------------------------------------------------------
keycheck = [1073741906, 1073741905, 1073741904, 1073741903, 13, 1073742049, 32, 27, 8, 9, 1073742048, 1073742052]
held = [False, False, False, False, False, False, False, False, False, False, False, False]

in_use = True

def formattime(time):
    """
    parameters:
    float time (seconds)

    returns a time in hours, minutes, and seconds rounded to seven decimal places through somewhat wet code
    """
    hour = str(math.floor(time / 3600))
    minute = str(math.floor(time / 60) % 60)
    second = str(time % 60)
    if float(minute) < 10:
        minute = '0' + minute
    if float(second) < 10:
        return hour + ':' + minute + ':' + f'0{float(second):.7f}'
    else:
        return hour + ':' + minute + ':' + f'{float(second):.7f}'

def checkterminal():
    """
    parameters:
    none

    displays a message saying to check the terminal.
    """
    window.blit(foot_text, foot_text.get_rect(center=(width/2, scroll_threshold + 120)))
    pygame.display.update()


while in_use:
    a = len(lines)  # this function takes time, best to store it in a variable to use for later
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If hit X button, game closes
            in_use = False

    back_color = (255, 255, 255) if not dark_mode else (0, 0, 0)
    window.fill(back_color)
    text_color = (0, 0, 0) if not dark_mode else (255, 255, 255)

    rect = pygame.Rect(0, scroll_threshold + 60, width, height - scroll_threshold - 60)
    border = pygame.Rect(0, scroll_threshold + 60, width, border_thickness)

    keys = pygame.key.get_pressed()

    if action == 'scroll':
        stats = [text.render(f'lines: {a:,}', True, text_color)]

        foo = line_offset*line_sel+top_offset - scroll_threshold if line_offset*line_sel+top_offset - scroll_threshold > 0 else 0
        start = foo // line_offset
        end = (foo + scroll_threshold) // line_offset if a - 1 > (foo + scroll_threshold) // line_offset else a - 1

        for i in range(start, end + 1):
                y = line_offset*i+top_offset if line_offset*line_sel+top_offset <= scroll_threshold else line_offset*i+top_offset - (line_offset*line_sel+top_offset - scroll_threshold)
                line_num = text.render(f'{i+1:,}', True, text_color)
                content = text.render(f'{lines[i]}', True, text_color)
                window.blit(line_num, line_num.get_rect(right=left_offset, top=y))
                window.blit(content, content.get_rect(left=left_offset+between_offset, top=y))

        line_arrow = text.render(f'< ({line_sel+1})', True, text_color)
        arrow_y = line_offset*line_sel+top_offset if line_offset*line_sel+top_offset <= scroll_threshold else line_offset*line_sel+top_offset - (line_offset*line_sel+top_offset - scroll_threshold)
        window.blit(line_arrow, line_arrow.get_rect(right=width, top=arrow_y))

        pygame.draw.rect(window, back_color, rect)
        pygame.draw.rect(window, text_color, border)

        for i, val in enumerate(stats):
            window.blit(val, val.get_rect(left=10, bottom=height-top_offset-(line_offset * i)))

        if keys[pygame.K_UP] and not held[0]:
            line_sel -= 1
            if line_sel < 0:
                lines.insert(0, '')
                line_sel = 0
        if keys[pygame.K_DOWN] and not held[1]:
            line_sel += 1
            if line_sel >= a:
                lines.append('')
        if keys[pygame.K_RETURN] and not held[4]:
            checkterminal()
            print(f'Contents of line {line_sel + 1}: {lines[line_sel]}')
            lines[line_sel] = input(f'New contents of line {line_sel + 1}: ')
        if keys[pygame.K_TAB] and not held[9]:
            while True:
                try:
                    foo = int(input('Jump to line: '))
                except ValueError:
                    print('Invalid input!')
                else:
                    if foo < 0:
                        line_sel = 0
                    elif foo > a - 1:
                        line_sel = a - 1
                    else:
                        line_sel = foo - 1
                    break
        if keys[pygame.K_SPACE] and not held[6]:
            lines.insert(line_sel+1, '')
        if keys[pygame.K_BACKSPACE] and not held[8]:
            if a > 1:
                lines.pop(line_sel)
                if line_sel >= a:
                    line_sel = a - 1
            else:
                lines[0] = ''
        if keys[pygame.K_LSHIFT] and not held[5]:
            action = 'customization'
        if keys[pygame.K_ESCAPE] and not held[7]:
            dark_mode = not dark_mode
        if keys[pygame.K_LCTRL] and not held[10]:
            starttime = time.time()
            with open('output.txt', 'w', encoding='utf-8') as f:
                for i, val in enumerate(lines):
                    f.write(val + '\n')
                print(f'Appended your current lines to output.txt\nTime: {formattime(time.time()-starttime)}')
        if keys[pygame.K_RCTRL] and not held[11]:
            checkterminal()
            while True:
                typing = input('Load file? All unsaved progress will be lost! (y/n): ').lower()
                accepted_inputs = ['y', 'yes']
                no_inputs = ['n', 'no']
                if typing in accepted_inputs:
                    starttime = time.time()
                    try:
                        with open('output.txt', 'r', encoding='utf-8') as f:
                            print('Clearing document:    ', end='')
                            lines = []
                            curtime = [time.time()]
                            print(f'{formattime(curtime[0]-starttime)}')
                            print('Reading lines:        ', end='')
                            lines = f.readlines()
                            curtime.append(time.time())
                            print(f'{formattime(curtime[-1]-curtime[-2])}')
                            print('Cleaning up lines:    ', end='')
                            for i in lines:
                                i = i.strip('\n')
                            curtime.append(time.time())
                            print(f'{formattime(curtime[-1]-curtime[-2])}')
                            print('-' * 79)
                            print(f'Loaded output.txt in  {formattime(time.time()-starttime)}')
                            if line_sel >= a:
                                line_sel = a - 1
                            break
                    except FileNotFoundError:
                        print('No file named output.txt exists in this directory')
                        break
                elif a in no_inputs:
                    break





    elif action == 'customization':
        opts = [text.render('Offset from the left', True, text_color),
                text.render('Offset from the top', True, text_color),
                text.render('Space between lines', True, text_color),
                text.render('Space from line numbers', True, text_color),
                text.render('Height of editor', True, text_color)]
        vals = [text.render(f'{left_offset}', True, text_color),
                text.render(f'{top_offset}', True, text_color),
                text.render(f'{line_offset}', True, text_color),
                text.render(f'{between_offset}', True, text_color),
                text.render(f'{scroll_threshold}', True, text_color)]

        for i in range(5):
            window.blit(opts[i], opts[i].get_rect(left=left_offset, top=line_offset*i+top_offset))
            window.blit(vals[i], vals[i].get_rect(right=width-left_offset, top=line_offset*i+top_offset))
            line_arrow = text.render(f'<', True, text_color)
            arrow_y = line_offset*opt_sel+top_offset
            window.blit(line_arrow, line_arrow.get_rect(right=width, top=arrow_y))
        if keys[pygame.K_UP] and not held[0]:
            opt_sel -= 1 if opt_sel > 0 else 0
        if keys[pygame.K_DOWN] and not held[1]:
            opt_sel += 1 if opt_sel < 5 - 1 else 0

        # UGHHHHHH THIS IS SO WET
        if keys[pygame.K_LEFT]:
            if opt_sel == 0:
                left_offset -= 1 if left_offset > 0 else 0
            elif opt_sel == 1:
                top_offset -= 1 if top_offset > 0 else 0
            elif opt_sel == 2:
                line_offset -= 1 if line_offset > 0 else 0
            elif opt_sel == 3:
                between_offset -= 1 if between_offset > 0 else 0
            elif opt_sel == 4:
                scroll_threshold -= 1 if scroll_threshold > 100 else 0

        if keys[pygame.K_RIGHT]:
            if opt_sel == 0:
                left_offset += 1
            elif opt_sel == 1:
                top_offset += 1
            elif opt_sel == 2:
                line_offset += 1
            elif opt_sel == 3:
                between_offset += 1
            elif opt_sel == 4:
                scroll_threshold += 1 if scroll_threshold < 700 else 0
        if keys[pygame.K_LSHIFT] and not held[5]:
            action = 'scroll'

    for i in range(len(keycheck)):
        if not keys[keycheck[i]]:
            held[i] = False
        else:
            held[i] = True

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()  # stops pygame
