import time
import board
import digitalio as io

from presets.layout import *

input = io.Direction.INPUT
down = io.Pull.DOWN

pin0 = io.DigitalInOut(board.GP0)
pin1 = io.DigitalInOut(board.GP1)
pin2 = io.DigitalInOut(board.GP2)
pin3 = io.DigitalInOut(board.GP3)
pin4 = io.DigitalInOut(board.GP4)
pin5 = io.DigitalInOut(board.GP5)
pin6 = io.DigitalInOut(board.GP6)
pin7 = io.DigitalInOut(board.GP7)
pin8 = io.DigitalInOut(board.GP8)
pin9 = io.DigitalInOut(board.GP9)
pin10 = io.DigitalInOut(board.GP10)
pin11 = io.DigitalInOut(board.GP11)
pin12 = io.DigitalInOut(board.GP12)
pin13 = io.DigitalInOut(board.GP13)
pin14 = io.DigitalInOut(board.GP14)
pin15 = io.DigitalInOut(board.GP15)

# Setting up the Buttons

button0 = pin0
button0.direction = input
button0.pull = down

button1 = pin1
button1.direction = input
button1.pull = down
 
button2 = pin2
button2.direction = input
button2.pull = down

button3 = pin3
button3.direction = input
button3.pull = down

button4 = pin4
button4.direction = input
button4.pull = down

button5 = pin5
button5.direction = input
button5.pull = down

button6 = pin6
button6.direction = input
button6.pull = down

# Setting up the Rotaries

rotary1PinA = pin10
rotary1PinA.direction = input
rotary1PinA.pull = down

rotary1PinB = pin11
rotary1PinB.direction = input
rotary1PinB.pull = down

rotary1Value = False

rotary2PinA = pin12
rotary2PinA.direction = input
rotary2PinA.pull = down

rotary2PinB = pin13
rotary2PinB.direction = input
rotary2PinB.pull = down

rotary2Value = False

while True:
    # Page Button
    if button0.value:
        print('button 0')
        page += 1
        time.sleep(0.2)
        if page > totalpages:
            page = 1
        Button0(page)
        time.sleep(0.1)
        
    # Buttons 1 - 9
    if button1.value:
        print('button 1')
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
        print('button 2')
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
        print('button 3')
        time.sleep(0.1)
        
    if button4.value:
        print('button 4')
        time.sleep(0.1)
        
    if button5.value:
        print('button 5')
        time.sleep(0.1)
        
    if button6.value:
        print('button 6')
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
        time.sleep(0.1)
        
    if rotary2Value != rotary2PinB.value:
        if rotary2PinB.value == False:
            if rotary2PinA.value == False:
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
        time.sleep(0.1)