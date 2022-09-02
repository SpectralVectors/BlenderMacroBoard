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
pins = 22

# This is the total number of buttons, including the Page Button, which is Button 0
buttons = 10

# Button Pins are setup as:
# Button : GPIO Pin
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
rotaries = 4

# The pins used by the rotary encoders, the first two must be consecutive GPIO pins
# The pins are setup as:
# (Rotary Pin A, Rotary Pin B, Rotary Button Pin)
rotary_pins = {
    0:(20,21,19),
    1:(10,11,16),
    2:(12,13,17),
    3:(14,15,18),
    }

# The total number of potentiometers
pots = 0

# This button is dedicated to changing pages/layers and should not be changed
def Button0(page):

    name = pages[str(page)]

    B1 = eval(f"Page{page}_Button1_Name")
    B2 = eval(f"Page{page}_Button2_Name")
    B3 = eval(f"Page{page}_Button3_Name")
    B4 = eval(f"Page{page}_Button4_Name")
    B5 = eval(f"Page{page}_Button5_Name")
    B6 = eval(f"Page{page}_Button6_Name")
    B7 = eval(f"Page{page}_Button7_Name")
    B8 = eval(f"Page{page}_Button8_Name")
    B9 = eval(f"Page{page}_Button9_Name")

    R1Left = eval(f"Page{page}_Rotary1_Left_Name")
    R1Right = eval(f"Page{page}_Rotary1_Right_Name")
    R1Button = eval(f"Page{page}_Rotary1_Button_Name")

    R2Left = eval(f"Page{page}_Rotary2_Left_Name")
    R2Right = eval(f"Page{page}_Rotary2_Right_Name")
    R2Button = eval(f"Page{page}_Rotary2_Button_Name")

    R3Left = eval(f"Page{page}_Rotary3_Left_Name")
    R3Right = eval(f"Page{page}_Rotary3_Right_Name")
    R3Button = eval(f"Page{page}_Rotary3_Button_Name")

    command(f'''p=bpy.context.scene.bmp;p.Page = '{name}';p.Key1='{B1}';p.Key2='{B2}';p.Key3='{B3}';p.Key4='{B4}';p.Key5='{B5}';p.Key6='{B6}';p.Key7='{B7}';p.Key8='{B8}';p.Key9='{B9}';p.R1Left='{R1Left}';p.R1Right='{R1Right}';p.R1Button='{R1Button}';p.R2Left='{R2Left}';p.R2Right='{R2Right}';p.R2Button='{R2Button}';p.R3Left='{R3Left}';p.R3Right='{R3Right}';p.R3Button='{R3Button}' ''')