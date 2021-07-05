import pygame
pygame.init()

width = 900
height = 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('notechad')

clock = pygame.time.Clock()
FPS = 60

text = pygame.font.Font('font/dogicapixel.ttf', 14)
foot = pygame.font.Font('font/dogicapixel.ttf', 36)

lines = ['']
# for i in range(10):
#     lines.append(f'words words words #{i+1}')  # Filler. COMMENT OUT ONCE READY TO.
selection = [0, 0]
action = 'scroll'
line_sel = 0
opt_sel = 0

dark_mode = False

line_offset = 20
left_offset = 50
between_offset = 10
top_offset = 10

scroll_threshold = 650

border_thickness = 2

keycheck = [1073741906, 1073741905, 1073741904, 1073741903, 13, 1073742049, 32, 27, 8]
held = [False, False, False, False, False, False, False, False, False]

in_use = True


while in_use:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_use = False

    back_color = (255, 255, 255) if not dark_mode else (0, 0, 0)
    window.fill(back_color)
    text_color = (0, 0, 0) if not dark_mode else (255, 255, 255)

    rect = pygame.Rect(0, scroll_threshold + 60, width, height - scroll_threshold - 60)
    border = pygame.Rect(0, scroll_threshold + 60, width, border_thickness)

    keys = pygame.key.get_pressed()

    if action == 'scroll':
        chars = 0
        for i in lines:
            chars += len(i)
        stats = [text.render(f'lines: {len(lines):,}', True, text_color),
                 text.render(f'length: {chars:,} ({chars/len(lines):,.3f} per line)', True, text_color)]

        for i, val in enumerate(lines):
            line_num = text.render(f'{i+1:,}', True, text_color)
            content = text.render(f'{val}', True, text_color)
            y = line_offset*i+top_offset if line_offset*line_sel+top_offset <= scroll_threshold else line_offset*i+top_offset - (line_offset*line_sel+top_offset - scroll_threshold)
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
            if line_sel >= len(lines):
                lines.append('')
        if keys[pygame.K_RETURN] and not held[4]:
            print(f'Contents of line {line_sel + 1}: {lines[line_sel]}')
            lines[line_sel] = input(f'New contents of line {line_sel + 1}: ')
        if keys[pygame.K_SPACE] and not held[6]:
            lines.insert(line_sel+1, '')
        if keys[pygame.K_BACKSPACE] and not held[8]:
            if len(lines) > 1:
                lines.pop(line_sel)
                if line_sel >= len(lines):
                    line_sel = len(lines) - 1
            else:
                lines[0] = ''
        if keys[pygame.K_LSHIFT] and not held[5]:
            action = 'customization'
        if keys[pygame.K_ESCAPE] and not held[7]:
            dark_mode = not dark_mode







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

        for i in range(len(opts)):
            window.blit(opts[i], opts[i].get_rect(left=left_offset, top=line_offset*i+top_offset))
            window.blit(vals[i], vals[i].get_rect(right=width-left_offset, top=line_offset*i+top_offset))
            line_arrow = text.render(f'<', True, text_color)
            arrow_y = line_offset*opt_sel+top_offset
            window.blit(line_arrow, line_arrow.get_rect(right=width, top=arrow_y))
        if keys[pygame.K_UP] and not held[0]:
            opt_sel -= 1 if opt_sel > 0 else 0
        if keys[pygame.K_DOWN] and not held[1]:
            opt_sel += 1 if opt_sel < len(opts) - 1 else 0

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
pygame.quit()
