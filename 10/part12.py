machines = list()
# Reading the input
with open("10/input.txt") as file_input:
    for line in file_input.readlines():
        tokens = line.split()
        # Converting the lights into a integer
        lights_str = tokens[0].replace('[','').replace(']','')
        lights = 0
        for i in range(len(lights_str)):
            if lights_str[i] == '#':
                lights += (1 << i)
        # Converting the buttons into a list of integers
        buttons = list()
        for button_str in tokens[1:-1]:
            button_str = button_str.replace('(','').replace(')','')
            button_int = 0
            for i in [int(v) for v in button_str.split(',')]:
                button_int += (1 << i)
            buttons.append(button_int)
        # Converting the joltage into a list of integers
        joltage_str = tokens[-1].replace('{','').replace('}','')
        joltage = tuple([int(v) for v in joltage_str.split(',')])
        machines.append([lights, buttons, joltage])
        #print(lights, buttons, joltage)
        
# Now let's process the machines

fewer_button_presses = 0
for lights, buttons, _ in machines:
    button_presses = None
    # Trying every combination of buttons
    # With 1 button
    for b in buttons:
        if b == lights:
            button_presses = 1
            #print(f"{lights}: {b}")
            break
    if button_presses is not None:
        fewer_button_presses += 1
        continue
    # With 2 buttons
    for b1 in range(len(buttons)-1):
        for b2 in range(b1,len(buttons)):
            if buttons[b1] ^ buttons[b2] == lights:
                button_presses = 2
                #print(f"{lights}: {buttons[b1]} ^ {buttons[b2]}")
                break
        if button_presses is not None:
            break
    if button_presses is not None:
        fewer_button_presses += 2
        continue
    # With 3 buttons
    for b1 in range(len(buttons)-2):
        for b2 in range(b1,len(buttons)-1):
            for b3 in range(b2,len(buttons)):
                if buttons[b1] ^ buttons[b2] ^ buttons[b3] == lights:
                    button_presses = 3
                    #print(f"{lights}: {buttons[b1]} ^ {buttons[b2]} ^ {buttons[b3]}")
                    break
            if button_presses is not None:
                break
        if button_presses is not None:
            break
    if button_presses is not None:
        fewer_button_presses += 3
        continue
    # With 4 buttons
    for b1 in range(len(buttons)-3):
        for b2 in range(b1,len(buttons)-2):
            for b3 in range(b2,len(buttons)-1):
                for b4 in range(b3,len(buttons)):
                    if buttons[b1] ^ buttons[b2] ^ buttons[b3] ^ buttons[b4] == lights:
                        button_presses = 4
                        #print(f"{lights}: {buttons[b1]} ^ {buttons[b2]} ^ {buttons[b3]} ^ {buttons[b4]}")
                        break
                if button_presses is not None:
                    break
            if button_presses is not None:
                break
        if button_presses is not None:
            break
    if button_presses is not None:
        fewer_button_presses += 4
        continue
    # With 5 buttons
    for b1 in range(len(buttons)-4):
        for b2 in range(b1,len(buttons)-3):
            for b3 in range(b2,len(buttons)-2):
                for b4 in range(b3,len(buttons)-1):
                    for b5 in range(b4,len(buttons)):
                        if buttons[b1] ^ buttons[b2] ^ buttons[b3] ^ buttons[b4] ^ buttons[b5] == lights:
                            #print(f"{lights}: {buttons[b1]} ^ {buttons[b2]} ^ {buttons[b3]} ^ {buttons[b4]} ^ {buttons[b5]}")
                            button_presses = 5
                            break
                    if button_presses is not None:
                        break
                if button_presses is not None:
                    break
            if button_presses is not None:
                break
        if button_presses is not None:
            break
    if button_presses is not None:
        fewer_button_presses += 5
        continue   
    # With 6 buttons
    for b1 in range(len(buttons)-5):
        for b2 in range(b1,len(buttons)-4):
            for b3 in range(b2,len(buttons)-3):
                for b4 in range(b3,len(buttons)-2):
                    for b5 in range(b4,len(buttons)-1):
                        for b6 in range(b5,len(buttons)):
                            if buttons[b1] ^ buttons[b2] ^ buttons[b3] ^ buttons[b4] ^ buttons[b5] ^ buttons[b6] == lights:
                                button_presses = 6
                                #print(f"{lights}: {buttons[b1]} ^ {buttons[b2]} ^ {buttons[b3]} ^ {buttons[b4]} ^ {buttons[b5]} ^ {buttons[b6]}")
                                break
                        if button_presses is not None:
                            break
                    if button_presses is not None:
                        break
                if button_presses is not None:
                    break
            if button_presses is not None:
                break
        if button_presses is not None:
            break
    if button_presses is not None:
        fewer_button_presses += 6
        continue
    
    # With 7 buttons
    for b1 in range(len(buttons)-6):
        for b2 in range(b1,len(buttons)-5):
            for b3 in range(b2,len(buttons)-4):
                for b4 in range(b3,len(buttons)-3):
                    for b5 in range(b4,len(buttons)-2):
                        for b6 in range(b5,len(buttons)-1):
                            for b7 in range(b6,len(buttons)):
                                if buttons[b1] ^ buttons[b2] ^ buttons[b3] ^ buttons[b4] ^ buttons[b5] ^ buttons[b6] ^ buttons[b7] == lights:
                                    #print(f"{lights}: {buttons[b1]} ^ {buttons[b2]} ^ {buttons[b3]} ^ {buttons[b4]} ^ {buttons[b5]} ^ {buttons[b6]} ^ {buttons[b7]}")
                                    button_presses = 7
                                    break
                            if button_presses is not None:
                                break
                        if button_presses is not None:
                            break
                    if button_presses is not None:
                        break
                if button_presses is not None:
                    break
            if button_presses is not None:
                break
        if button_presses is not None:
            break
    if button_presses is not None:
        fewer_button_presses += 7
        continue
    
    # With 8 buttons
    for b1 in range(len(buttons)-7):
        for b2 in range(b1,len(buttons)-6):
            for b3 in range(b2,len(buttons)-5):
                for b4 in range(b3,len(buttons)-4):
                    for b5 in range(b4,len(buttons)-3):
                        for b6 in range(b5,len(buttons)-2):
                            for b7 in range(b6,len(buttons)-1):
                                for b8 in range(b7,len(buttons)):
                                    if buttons[b1] ^ buttons[b2] ^ buttons[b3] ^ buttons[b4] ^ buttons[b5] ^ buttons[b6] ^ buttons[b7] ^ buttons[b8] == lights:
                                        button_presses = 8
                                        #print(f"{lights}: {buttons[b1]} ^ {buttons[b2]} ^ {buttons[b3]} ^ {buttons[b4]} ^ {buttons[b5]} ^ {buttons[b6]} ^ {buttons[b7]} ^ {buttons[b8]}")
                                        break
                                if button_presses is not None:
                                    break
                            if button_presses is not None:
                                break
                        if button_presses is not None:
                            break
                    if button_presses is not None:
                        break
                if button_presses is not None:
                    break
            if button_presses is not None:
                break
        if button_presses is not None:
            break
    if button_presses is not None:
        fewer_button_presses += 8
        continue
    print("More than 8")

print(f"Part 1: {fewer_button_presses}")
