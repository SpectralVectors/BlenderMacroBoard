from .base import *
from .Pages.Page1 import *
from .Pages.Page2 import *
from .Pages.Page3 import *
from .Pages.Page4 import *

page = 1
totalpages = 4

pages = {
    '1':Page1Name,
    '2':Page2Name,
    '3':Page3Name,
    '4':Page4Name,
}

# This button is dedicated to changing pages/layers and should not be changed
def Button0(page):
    # Enters Python Code
    kb.send(shift,ctrl,alt,a)
    name = pages[str(page)]
    text.write(f"C.scene.bmp.p='{page} - {name}'")
    kb.send(enter)
    kb.send(shift,ctrl,alt,b)
    