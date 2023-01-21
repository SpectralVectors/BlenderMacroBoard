# Importing the libraries we need
from time import sleep as wait
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from ._drive import drive

# Importing the shortened keycodes
from BoardSetup._shortcodes import *

# Convenience variables
kb = Keyboard(usb_hid.devices)
text = KeyboardLayoutUS(kb)
mouse = Mouse(usb_hid.devices)

# The location of the Scripts folder
path = '/lib/Scripts/'

# Helper function to allow running commands in the background
def command(command):
    kb.send(shift,ctrl,alt,insert)
    wait(0.1)
    print(f"import bpy;{command}")
    kb.send(left,right)

# Helper function to make running scripts only a single line
def run_script(script):
    kb.send(shift,ctrl,alt,insert)
    wait(0.1)
    print(f"exec(open('{drive}{path}{script}').read())")
