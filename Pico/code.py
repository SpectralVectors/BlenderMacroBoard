import board
import digitalio as io
from analogio import AnalogIn
from time import sleep as wait

from BoardSetup.Layout import *

input = io.Direction.INPUT
down = io.Pull.DOWN

# Setting up the Pins
if pins:
    for i in range(pins):
        exec(f'''

pin{i} = io.DigitalInOut(board.GP{i})

''')

# Setting up the Buttons
if buttons:
    for i in range(buttons):
        exec(f'''

button{i} = pin{button_pins[i]}
button{i}.direction = input
button{i}.pull = down

''')

# Setting up the Rotaries
if rotaries:
    for i in range(rotaries):
        exec(f'''

rotary{i}PinA = pin{rotary_pins[i][0]}
rotary{i}PinA.direction = input
rotary{i}PinA.pull = down

rotary{i}PinB = pin{rotary_pins[i][1]}
rotary{i}PinB.direction = input
rotary{i}PinB.pull = down

rotary{i}Value = rotary{i}PinB.value

rotary{i}Button = pin{rotary_pins[i][2]}
rotary{i}Button.direction = input
rotary{i}Button.pull = down

''')

# Setting up the Pots
if pots:
    for i in range(pots):
        exec(f'''

pot{i+1} = AnalogIn(board.A{i})

''')

# Check for input in an infinite loop
while True:
    
    # Button 0 - Page Change
    if button0.value:
        page += 1
        if page > totalpages:
            page = 1
        Button0(page)
        wait(0.1)

    # Buttons 1 - 9
    if button1.value:
        exec(f"Page{page}_Button1()")
        wait(0.1)

    if button2.value:
        exec(f"Page{page}_Button2()")
        wait(0.1)

    if button3.value:
        exec(f"Page{page}_Button3()")
        wait(0.1)

    if button4.value:
        exec(f"Page{page}_Button4()")
        wait(0.1)

    if button5.value:
        exec(f"Page{page}_Button5()")
        wait(0.1)

    if button6.value:
        exec(f"Page{page}_Button6()")
        wait(0.1)

    if button7.value:
        exec(f"Page{page}_Button7()")
        wait(0.1)

    if button8.value:
        exec(f"Page{page}_Button8()")
        wait(0.1)

    if button9.value:
        exec(f"Page{page}_Button9()")
        wait(0.1)

    if rotary0Button.value:
        kb.send(space)
        print('space')
        wait(0.2)

    if rotary1Button.value:
        exec(f"Page{page}_Rotary1_Button()")
        wait(0.1)

    if rotary2Button.value:
        exec(f"Page{page}_Rotary2_Button()")
        wait(0.1)

    if rotary3Button.value:
        exec(f"Page{page}_Rotary3_Button()")
        wait(0.1)

    # Rotaries
    # Rotary 0 is set to scrub the timeline on all pages
    # with the button set to Play/Stop
    if rotary0Value != rotary0PinB.value:
        if not rotary0PinB.value:
            if not rotary0PinA.value:
                kb.send(right)
                print('right')
                wait(0.1)
            else:
                kb.send(left)
                print('left')
                wait(0.1)
        rotary0Value = rotary0PinB.value

    if rotary1Value != rotary1PinB.value:
        if not rotary1PinB.value:
            if not rotary1PinA.value:
                exec(f"Page{page}_Rotary1_Left()")
            else:
                exec(f"Page{page}_Rotary1_Right()")                 
        rotary1Value = rotary1PinB.value

    if rotary2Value != rotary2PinB.value:
        if not rotary2PinB.value:
            if not rotary2PinA.value:
                exec(f"Page{page}_Rotary2_Left()")
            else:
                exec(f"Page{page}_Rotary2_Right()")                   
        rotary2Value = rotary2PinB.value
        
    if rotary3Value != rotary3PinB.value:
        if not rotary3PinB.value:
            if not rotary3PinA.value:
                exec(f"Page{page}_Rotary3_Left()")
            else:
                exec(f"Page{page}_Rotary3_Right()")                  
        rotary3Value = rotary3PinB.value

    # Pots
    if pots:
        # Get the Pot value as a percentage
        print(f"{int((pot1.value / 65520) * 100)}%")
