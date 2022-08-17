from ._base import *
from .Pages.Page1 import *
from .Pages.Page2 import *
from .Pages.Page3 import *
from .Pages.Page4 import *

pins = 16
buttons = 10

page = 1
totalpages = 4

pages = {
    '1':Page1Name,
    '2':Page2Name,
    '3':Page3Name,
    '4':Page4Name,
}

# This function updates the page number, and returns to the first page after the last
def turn_page(page, totalpages):
        page += 1
        if page > totalpages:
            page = 1

# This button is dedicated to changing pages/layers and should not be changed
def Button0(page):
    # Enters Python Code
    kb.send(shift,ctrl,alt,a)
    name = pages[str(page)]
    text.write(f"C.scene.bmp.p='{page} - {name}'")
    kb.send(enter)
    kb.send(shift,ctrl,alt,b)

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
    