import time
import board
import digitalio
from presets.default import *

btn0_pin = board.GP0
btn0 = digitalio.DigitalInOut(btn0_pin)
btn0.direction = digitalio.Direction.INPUT
btn0.pull = digitalio.Pull.DOWN

btn1_pin = board.GP1
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2_pin = board.GP2
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

page = 1

while True:

    if btn0.value:
        page += 1
        if page > 4:
            page = 1
        print(page)
        time.sleep(0.1)

    if btn1.value:
        if page == 1:
            Page1_Button1()
        if page == 2:
            Page2_Button1()
        if page == 3:
            Page3_Button1()
        if page == 4:
            Page4_Button1()
        
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
