# Importing the libraries we need
from time import sleep as wait
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
# Importing the shortened keycodes
from presets.shortcodes import *

# Convenience variable
kb = Keyboard(usb_hid.devices)
text = KeyboardLayoutUS(kb)
mouse = Mouse(usb_hid.devices)

# This is a helper function to make running scripts only a single line
def run_script(filepath):
    kb.send(shift,ctrl,alt,a)
    text.write(str(f"exec(open('{filepath}').read())"))
    kb.send(enter)
    kb.send(shift,ctrl,alt,b)
