# Importing the libraries we need
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

# Convenience variable
keyboard = Keyboard(usb_hid.devices)

# Keycode list: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode

# The Keyboard Layout, for reference:

'''
|1|2|3|
|4|5|6|
|7|8|9|0|
|R|R|R|
'''

# Add your own custom macros below:

########################
######## Page 1 ########
########################

### Push Buttons

def Page1_Button1():
    print('p1b1')
    time.sleep(0.1)

def Page1_Button2():
    print('p1b2')
    time.sleep(0.1)

def Page1_Button3():
    print('p1b3')
    time.sleep(0.1)

def Page1_Button4():
    print('p1b4')
    time.sleep(0.1)

def Page1_Button5():
    print('p1b5')
    time.sleep(0.1)

def Page1_Button6():
    print('p1b6')
    time.sleep(0.1)

def Page1_Button7():
    print('p1b7')
    time.sleep(0.1)

def Page1_Button8():
    print('p1b8')
    time.sleep(0.1)

def Page1_Button9():
    print('p1b9')
    time.sleep(0.1)

### Rotaries

def Page1_Rotary1_Left():
    print('p1r1l')
    time.sleep(0.1)

def Page1_Rotary1_Push():
    print('p1r1p')
    time.sleep(0.1)

def Page1_Rotary1_Right():
    print('p1r1r')
    time.sleep(0.1)

def Page1_Rotary2_Left():
    print('p1r2l')
    time.sleep(0.1)

def Page1_Rotary2_Push():
    print('p1r2p')
    time.sleep(0.1)

def Page1_Rotary2_Right():
    print('p1r2r')
    time.sleep(0.1)

def Page1_Rotary3_Left():
    print('p1r3l')
    time.sleep(0.1)

def Page1_Rotary3_Push():
    print('p1r3p')
    time.sleep(0.1)

def Page1_Rotary3_Right():
    print('p1r3r')
    time.sleep(0.1)

########################
######## Page 2 ########
########################

### Push Buttons

def Page2_Button1():
    print('p2b1')
    time.sleep(0.1)

def Page2_Button2():
    print('p2b2')
    time.sleep(0.1)

def Page2_Button3():
    print('p2b3')
    time.sleep(0.1)

def Page2_Button4():
    print('p2b4')
    time.sleep(0.1)

def Page2_Button5():
    print('p2b5')
    time.sleep(0.1)

def Page2_Button6():
    print('p2b6')
    time.sleep(0.1)

def Page2_Button7():
    print('p2b7')
    time.sleep(0.1)

def Page2_Button8():
    print('p2b8')
    time.sleep(0.1)

def Page2_Button9():
    print('p2b9')
    time.sleep(0.1)

### Rotaries

def Page2_Rotary1_Left():
    print('p2r1l')
    time.sleep(0.1)

def Page2_Rotary1_Push():
    print('p2r1p')
    time.sleep(0.1)

def Page2_Rotary1_Right():
    print('p2r1r')
    time.sleep(0.1)

def Page2_Rotary2_Left():
    print('p2r2l')
    time.sleep(0.1)

def Page2_Rotary2_Push():
    print('p2r2p')
    time.sleep(0.1)

def Page2_Rotary2_Right():
    print('p2r2r')
    time.sleep(0.1)

def Page2_Rotary3_Left():
    print('p2r3l')
    time.sleep(0.1)

def Page2_Rotary3_Push():
    print('p2r3p')
    time.sleep(0.1)

def Page2_Rotary3_Right():
    print('p2r3r')
    time.sleep(0.1)

########################
######## Page 3 ########
########################

### Push Buttons

def Page3_Button1():
    print('p3b1')
    time.sleep(0.1)

def Page3_Button2():
    print('p3b2')
    time.sleep(0.1)

def Page3_Button3():
    print('p3b3')
    time.sleep(0.1)

def Page3_Button4():
    print('p3b4')
    time.sleep(0.1)

def Page3_Button5():
    print('p3b5')
    time.sleep(0.1)

def Page3_Button6():
    print('p3b6')
    time.sleep(0.1)

def Page3_Button7():
    print('p3b7')
    time.sleep(0.1)

def Page3_Button8():
    print('p3b8')
    time.sleep(0.1)

def Page3_Button9():
    print('p3b9')
    time.sleep(0.1)

### Rotaries

def Page3_Rotary1_Left():
    print('p3r1l')
    time.sleep(0.1)

def Page3_Rotary1_Push():
    print('p3r1p')
    time.sleep(0.1)

def Page3_Rotary1_Right():
    print('p3r1r')
    time.sleep(0.1)

def Page3_Rotary2_Left():
    print('p3r2l')
    time.sleep(0.1)

def Page3_Rotary2_Push():
    print('p3r2p')
    time.sleep(0.1)

def Page3_Rotary2_Right():
    print('p3r2r')
    time.sleep(0.1)

def Page3_Rotary3_Left():
    print('p3r3l')
    time.sleep(0.1)

def Page3_Rotary3_Push():
    print('p3r3p')
    time.sleep(0.1)

def Page3_Rotary3_Right():
    print('p3r3r')
    time.sleep(0.1)

########################
######## Page 4 ########
########################

### Push Buttons

def Page4_Button1():
    print('p4b1')
    time.sleep(0.1)

def Page4_Button2():
    print('p4b2')
    time.sleep(0.1)

def Page4_Button3():
    print('p4b3')
    time.sleep(0.1)

def Page4_Button4():
    print('p4b4')
    time.sleep(0.1)

def Page4_Button5():
    print('p4b5')
    time.sleep(0.1)

def Page4_Button6():
    print('p4b6')
    time.sleep(0.1)

def Page4_Button7():
    print('p4b7')
    time.sleep(0.1)

def Page4_Button8():
    print('p4b8')
    time.sleep(0.1)

def Page4_Button9():
    print('p4b9')
    time.sleep(0.1)

### Rotaries

def Page4_Rotary1_Left():
    print('p4r1l')
    time.sleep(0.1)

def Page4_Rotary1_Push():
    print('p4r1p')
    time.sleep(0.1)

def Page4_Rotary1_Right():
    print('p4r1r')
    time.sleep(0.1)

def Page4_Rotary2_Left():
    print('p4r2l')
    time.sleep(0.1)

def Page4_Rotary2_Push():
    print('p4r2p')
    time.sleep(0.1)

def Page4_Rotary2_Right():
    print('p4r2r')
    time.sleep(0.1)

def Page4_Rotary3_Left():
    print('p4r3l')
    time.sleep(0.1)

def Page4_Rotary3_Push():
    print('p4r3p')
    time.sleep(0.1)

def Page4_Rotary3_Right():
    print('p4r3r')
    time.sleep(0.1)