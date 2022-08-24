from .._base import *

########################
######## Page 2 ########
########################

# Enter a name for this page
Page2Name = 'GREASE PENCIL (Page 2)'

### Push Buttons

def Page2_Button1():
    print('Page 2 Button 1')
    # Undo
    kb.send(ctrl,z)

def Page2_Button2():
    print('Page 2 Button 2')
    # Keyframe Y Rotation
    kb.send(shift,ctrl,alt,y)

def Page2_Button3():
    print('Page 2 Button 3')
    wait(0.1)

def Page2_Button4():
    print('Page 2 Button 4')
    wait(0.1)

def Page2_Button5():
    print('Page 2 Button 5')
    wait(0.1)

def Page2_Button6():
    print('Page 2 Button 6')
    wait(0.1)

def Page2_Button7():
    print('Page 2 Button 7')
    wait(0.1)

def Page2_Button8():
    print('Page 2 Button 8')
    wait(0.1)

def Page2_Button9():
    print('Page 2 Button 9')
    wait(0.1)

### Rotaries

def Page2_Rotary1_Left():
    print('Page 2 Rotary 1 Left')
    # Rotate Y 5 degrees
    #kb.send(r, y, kb5, enter)

def Page2_Rotary1_Push():
    print('Page 2 Rotary 1 Push')
    wait(0.1)

def Page2_Rotary1_Right():
    print('Page 2 Rotary 1 Right')
    # Rotate Y -5 degrees
    #kb.send(r, y, minus, kb5, enter)

def Page2_Rotary2_Left():
    print('Page 2 Rotary 2 Left')


def Page2_Rotary2_Push():
    print('Page 2 Rotary 2 Push')
    wait(0.1)

def Page2_Rotary2_Right():
    print('Page 2 Rotary 2 Right')


def Page2_Rotary3_Left():
    print('Page 2 Rotary 3 Left')


def Page2_Rotary3_Push():
    print('Page 2 Rotary 3 Push')
    wait(0.1)

def Page2_Rotary3_Right():
    print('Page 2 Rotary 3 Right')
