import time
import board
import digitalio
from presets.default import *

btn0 = digitalio.DigitalInOut(board.GP0)
btn0.direction = digitalio.Direction.INPUT
btn0.pull = digitalio.Pull.DOWN

btn1 = digitalio.DigitalInOut(board.GP1)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
 
btn2 = digitalio.DigitalInOut(board.GP2)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

r1dirPin = digitalio.DigitalInOut(board.GP3)
r1dirPin.direction = digitalio.Direction.INPUT
r1dirPin.pull = digitalio.Pull.DOWN

r1stepPin = digitalio.DigitalInOut(board.GP4)
r1stepPin.direction = digitalio.Direction.INPUT
r1stepPin.pull = digitalio.Pull.DOWN

page = 1

previousValue = False

while True:
    if btn0.value:
        page += 1
        time.sleep(0.2)
        if page > 4:
            page = 1
        print(page)

    if btn1.value:
        if page == 1:
            Page1_Button1()
        if page == 2:
            Page2_Button1()
        if page == 3:
            Page3_Button1()
        if page == 4:
            Page4_Button1()
        time.sleep(0.1)
        
    if btn2.value:
        if page == 1:
            Page1_Button2()
        if page == 2:
            Page2_Button2()
        if page == 3:
            Page3_Button2()
        if page == 4:
            Page4_Button2()
        time.sleep(0.1)

    if previousValue != r1stepPin.value:
        if r1stepPin.value == False:
            if r1dirPin.value == False:
                print('Left')
                Page1_Rotary1_Left()
            else:
                print('Right')
                Page1_Rotary1_Right()
        previousValue = r1stepPin.value
