'''
Original Keycode list: 
https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode

Shortcode list (eg: instead of writing: Keycode.A, you can just write: a):

Letters: 
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

Numbers(At the top of the keyboard, NOT the Numpad): 
kb1, kb2, kb3, kb4, kb5, kb6, kb7, kb8, kb9, kb0

Actions: 
enter, esc, backspace, tab, space, caps_lock, insert, delete, home, end, page_up,
page_down, print_screen, scroll_lock, pause

Modifiers:
shift, ctrl, alt, os, right_shift, right_ctrl, right_alt, right_os

Arrows:
right, up, left, down

Symbols: 
minus, equals, left_bracket, right_bracket, backslash, pound, hash, semicolon, 
quote, grave_accent, comma, period, dot, slash 

Function Keys: 
f1, f2, f3, f4, f5,f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, 
f19, f20, f21, f22, f23, f24

Numpad:
np1, np2, np3, np4, np5, np6, np7, np8, np9, np0, np_numlock, np_slash, np_star,
np_minus, np_plus, np_enter, np_dot

The Keyboard Layout, for reference:

|1|2|3|
|4|5|6|
|7|8|9|0|
|R|R|R|

'''
# Importing the libraries we need
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from presets.shortcodes import *

# Convenience variable
keyboard = Keyboard(usb_hid.devices)
text = KeyboardLayoutUS(keyboard)

def key(Keycode):
    keyboard.send(Keycode)
    time.sleep(0.01)

def keys(Keycodes):
    for Keycode in Keycodes:
        keyboard.send(Keycode)
    time.sleep(0.01)


# Add your own custom macros below:

########################
######## Page 1 ########
########################

### Push Buttons

def Page1_Button1():
    # Rotate Y 45 degrees
    keys([r, y, kb4, kb5, enter])

def Page1_Button2():
    # Rotate X 45 degrees
    keys([f12])

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
    # Rotate X 3 degrees
    keys([r, x, kb3, enter])

def Page1_Rotary1_Push():
    print('p1r1p')
    time.sleep(0.1)

def Page1_Rotary1_Right():
    # Rotate X -3 degrees
    keys([r, x, minus, kb3, enter])

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