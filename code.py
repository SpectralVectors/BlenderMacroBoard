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
        if page == 1:
            Page1_Button1()
        if page == 2:
            Page2_Button1()
        if page == 3:
            Page3_Button1()
        if page == 4:
            Page4_Button1()
        time.sleep(0.1)
        
    if button2.value:
        if page == 1:
            Page1_Button2()
        if page == 2:
            Page2_Button2()
        if page == 3:
            Page3_Button2()
        if page == 4:
            Page4_Button2()
        time.sleep(0.1)
        
    if button3.value:
        if page == 1:
            Page1_Button3()
        if page == 2:
            Page2_Button3()
        if page == 3:
            Page3_Button3()
        if page == 4:
            Page4_Button3()
        time.sleep(0.1)
        
    if button4.value:
        if page == 1:
            Page1_Button4()
        if page == 2:
            Page2_Button4()
        if page == 3:
            Page3_Button4()
        if page == 4:
            Page4_Button4()
        time.sleep(0.1)
        
    if button5.value:
        if page == 1:
            Page1_Button5()
        if page == 2:
            Page2_Button5()
        if page == 3:
            Page3_Button5()
        if page == 4:
            Page4_Button5()
        time.sleep(0.1)
        
    if button6.value:
        if page == 1:
            Page1_Button6()
        if page == 2:
            Page2_Button6()
        if page == 3:
            Page3_Button6()
        if page == 4:
            Page4_Button6()
        time.sleep(0.1)

    if button7.value:
        if page == 1:
            Page1_Button7()
        if page == 2:
            Page2_Button7()
        if page == 3:
            Page3_Button7()
        if page == 4:
            Page4_Button7()
        time.sleep(0.1)

    if button8.value:
        if page == 1:
            Page1_Button8()
        if page == 2:
            Page2_Button8()
        if page == 3:
            Page3_Button8()
        if page == 4:
            Page4_Button8()
        time.sleep(0.1)
        
    if button9.value:
        if page == 1:
            Page1_Button9()
        if page == 2:
            Page2_Button9()
        if page == 3:
            Page3_Button9()
        if page == 4:
            Page4_Button9()
        time.sleep(0.1)
        
    if r1Push.value:
        if page == 1:
            Page1_Rotary1_Push()
        if page == 2:
            Page2_Rotary1_Push()
        if page == 3:
            Page3_Rotary1_Push()
        if page == 4:
            Page4_Rotary1_Push()
        time.sleep(0.1)

    if r2Push.value:
        if page == 1:
            Page1_Rotary2_Push()
        if page == 2:
            Page2_Rotary2_Push()
        if page == 3:
            Page3_Rotary2_Push()
        if page == 4:
            Page4_Rotary2_Push()
        time.sleep(0.1)

    if r3Push.value:
        if page == 1:
            Page1_Rotary3_Push()
        if page == 2:
            Page2_Rotary3_Push()
        if page == 3:
            Page3_Rotary3_Push()
        if page == 4:
            Page4_Rotary3_Push()
        time.sleep(0.1)

    # Rotaries
    if rotary1Value != rotary1PinB.value:
        if not rotary1PinB.value:
            if not rotary1PinA.value:
                if page == 1:
                    Page1_Rotary1_Left()
                if page == 2:
                    Page2_Rotary1_Left()
                if page == 3:
                    Page3_Rotary1_Left()
                if page == 4:
                    Page4_Rotary1_Left()
            else:
                if page == 1:
                    Page1_Rotary1_Right()
                if page == 2:
                    Page2_Rotary1_Right()
                if page == 3:
                    Page3_Rotary1_Right()
                if page == 4:
                    Page4_Rotary1_Right()                  
        rotary1Value = rotary1PinB.value
        
        
    if rotary2Value != rotary2PinB.value:
        if not rotary2PinB.value:
            if not rotary2PinA.value:
                if page == 1:
                    Page1_Rotary2_Left()
                if page == 2:
                    Page2_Rotary2_Left()
                if page == 3:
                    Page3_Rotary2_Left()
                if page == 4:
                    Page4_Rotary2_Left()
            else:
                if page == 1:
                    Page1_Rotary2_Right()
                if page == 2:
                    Page2_Rotary2_Right()
                if page == 3:
                    Page3_Rotary2_Right()
                if page == 4:
                    Page4_Rotary2_Right()                   
        rotary2Value = rotary2PinB.value
        
    if rotary3Value != rotary3PinB.value:
        if not rotary3PinB.value:
            if not rotary3PinA.value:
                if page == 1:
                    Page1_Rotary3_Left()
                if page == 2:
                    Page2_Rotary3_Left()
                if page == 3:
                    Page3_Rotary3_Left()
                if page == 4:
                    Page4_Rotary3_Left()
            else:
                if page == 1:
                    Page1_Rotary3_Right()
                if page == 2:
                    Page2_Rotary3_Right()
                if page == 3:
                    Page3_Rotary3_Right()
                if page == 4:
                    Page4_Rotary3_Right()                  
        rotary3Value = rotary3PinB.value
