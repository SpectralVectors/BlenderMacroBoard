from .._base import *

########################
######## Page 1 ########
########################

# Enter a name for this page
Page1Name = 'General'

### Push Buttons

def Page1_Button1():
    kb.send(esc)
    print('Page 1 Button 1')
    wait(0.1)


def Page1_Button2():
    kb.send(ctrl,z)
    print('Page 1 Button 2')
    wait(0.1)
    # Run a script from the specified location
    #run_script('G:/lib/scripts/ObjectTest.py')

def Page1_Button3():
    kb.send(enter)
    print('Page 1 Button 3')
    wait(0.1)

def Page1_Button4():
    run_script('G:/lib/scripts/ObjectTest.py')
    print('Page 1 Button 4')
    wait(0.1)

def Page1_Button5():
    print('Page 1 Button 5')
    wait(0.1)

def Page1_Button6():
    print('Page 1 Button 6')
    wait(0.1)

def Page1_Button7():
    print('Page 1 Button 7')
    wait(0.1)

def Page1_Button8():
    print('Page 1 Button 8')
    wait(0.1)

def Page1_Button9():
    print('Page 1 Button 9')
    wait(0.1)

### Rotaries

def Page1_Rotary1_Left():
    print('Page 1 Rotary 1 Left')
    # Rotate X 5 degrees
    kb.send(r, x, kb5, enter)

def Page1_Rotary1_Push():
    kb.send(shift,ctrl,alt,x)
    print('Page 1 Rotary 1 Push')
    wait(0.1)

def Page1_Rotary1_Right():
    print('Page 1 Rotary 1 Right')
    # Rotate X -5 degrees
    kb.send(r, x, minus, kb5, enter)

def Page1_Rotary2_Left():
    kb.send(r,y,kb5,enter)
    print('Page 1 Rotary 2 Left')


def Page1_Rotary2_Push():
    kb.send(shift,ctrl,alt,y)
    print('Page 1 Rotary 2 Push')
    wait(0.1)

def Page1_Rotary2_Right():
    kb.send(r,y,minus,kb5,enter)
    print('Page 1 Rotary 2 Right')


def Page1_Rotary3_Left():
    kb.send(r,z,kb5,enter)
    print('Page 1 Rotary 3 Left')


def Page1_Rotary3_Push():
    kb.send(shift,ctrl,alt,z)
    print('Page 1 Rotary 3 Push')
    wait(0.1)

def Page1_Rotary3_Right():
    kb.send(r,z,minus,kb5,enter)
    print('Page 1 Rotary 3 Right')
