import time
import board
import digitalio as io

from BoardSetup.Layout import *

input = io.Direction.INPUT
down = io.Pull.DOWN

# Setting up the Pins
for i in range(pins):
    exec(f"pin{i} = io.DigitalInOut(board.GP{i})")

# Setting up the Buttons
for i in range(buttons):
    exec(f"button{i} = pin{i}")
    exec(f"button{i}.direction = input")
    exec(f"button{i}.pull = down")

# Setting up the Rotaries
rotaries = 3
rotary_pins = {
    '1':(10,11),
    '2':(12,13),
    '3':(14,15),
    }

rotary1PinA = pin10
rotary1PinA.direction = input
rotary1PinA.pull = down

rotary1PinB = pin11
rotary1PinB.direction = input
rotary1PinB.pull = down

rotary1Value = rotary1PinB.value

rotary2PinA = pin12
rotary2PinA.direction = input
rotary2PinA.pull = down

rotary2PinB = pin13
rotary2PinB.direction = input
rotary2PinB.pull = down

rotary2Value = rotary2PinB.value

rotary3PinA = pin14
rotary3PinA.direction = input
rotary3PinA.pull = down

rotary3PinB = pin15
rotary3PinB.direction = input
rotary3PinB.pull = down

rotary3Value = rotary3PinB.value

r1Push = pin16
r1Push.direction = input
r1Push.pull = down

r2Push = pin17
r2Push.direction = input
r2Push.pull = down

r3Push = pin18
r3Push.direction = input
r3Push.pull = down

while True:
    # Page Button
    if button0.value:
        print('button 0')
        page += 1
        if page > totalpages:
            page = 1
        Button0(page)
        time.sleep(0.1)
        
    # Buttons 1 - 9
    if button1.value:
        exec(f"Page{page}_Button1()")
        time.sleep(0.1)
        
    if button2.value:
        exec(f"Page{page}_Button2()")
        time.sleep(0.1)
        
    if button3.value:
        exec(f"Page{page}_Button3()")
        time.sleep(0.1)
        
    if button4.value:
        exec(f"Page{page}_Button4()")
        time.sleep(0.1)
        
    if button5.value:
        exec(f"Page{page}_Button5()")
        time.sleep(0.1)
        
    if button6.value:
        exec(f"Page{page}_Button6()")
        time.sleep(0.1)

    if button7.value:
        exec(f"Page{page}_Button7()")
        time.sleep(0.1)

    if button8.value:
        exec(f"Page{page}_Button8()")
        time.sleep(0.1)
        
    if button9.value:
        exec(f"Page{page}_Button9()")
        time.sleep(0.1)
        
    if r1Push.value:
        exec(f"Page{page}_Rotary1_Push()")
        time.sleep(0.1)

    if r2Push.value:
        exec(f"Page{page}_Rotary2_Push()")
        time.sleep(0.1)

    if r3Push.value:
        exec(f"Page{page}_Rotary3_Push()")
        time.sleep(0.1)

    # Rotaries
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
