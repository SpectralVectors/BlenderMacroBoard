from ._base import *
from .Pages.Page1 import *
from .Pages.Page2 import *
from .Pages.Page3 import *
from .Pages.Page4 import *
from time import sleep as wait

# Update this section to reflect the number of Pages, GPIO pins, Buttons, Rotaries etc on your board

# This determines the starting Page
page = 1
# This defines how many Pages the pad loops through before returning to the starting Page
totalpages = 4

pages = {
    '1':Page1Name,
    '2':Page2Name,
    '3':Page3Name,
    '4':Page4Name,
}

# This is the total number of pins used by the buttons and rotaries
pins = 19

# This is the total number of buttons, including the Page Button, which is Button 0
buttons = 10

# Button Pins are setup as:
# Button Number : GPIO Pin Number
button_pins = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    }

# The total number of rotary encoders on your board
rotaries = 3

# The pins used by the rotary encoders, the first two must be consecutive GPIO pins
# The pins are setup as:
# (Rotary Pin A, Rotary Pin B, Rotary Button Pin)
rotary_pins = {
    1:(10,11,16),
    2:(12,13,17),
    3:(14,15,18),
    }

# This button is dedicated to changing pages/layers and should not be changed
def Button0(page):
    print("Button 0")
    # Enters Python Code
    kb.send(shift,ctrl,alt,a)
    name = pages[str(page)]
    wait(0.2)
    text.write(f"bpy.context.scene.bmp.p = '{name}'")
    kb.send(enter)
    kb.send(enter)
    kb.send(right,left)

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

    |0|
|1|2|3|
|4|5|6|
|7|8|9|
|R|R|R|

'''
    