from ..base import *

########################
######## Page 1 ########
########################

# Enter a name for this page
Page1Name = 'General'

### Push Buttons

def Page1_Button1():
    # Escape
    kb.send(esc)

def Page1_Button2():
    # Run a script from the specified location
    run_script('G:/lib/scripts/ObjectTest.py')

def Page1_Button3():
    print('Page 1 Button 3')
    wait(0.1)

def Page1_Button4():
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
    print('Page 1 Rotary 1 Push')

def Page1_Rotary1_Right():
    print('Page 1 Rotary 1 Right')
    # Rotate X -5 degrees
    kb.send(r, x, minus, kb5, enter)

def Page1_Rotary2_Left():
    print('Page 1 Rotary 2 Left')
    wait(0.1)

def Page1_Rotary2_Push():
    print('Page 1 Rotary 2 Push')
    wait(0.1)

def Page1_Rotary2_Right():
    print('Page 1 Rotary 2 Right')
    wait(0.1)

def Page1_Rotary3_Left():
    print('Page 1 Rotary 3 Left')
    wait(0.1)

def Page1_Rotary3_Push():
    print('Page 1 Rotary 3 Push')
    wait(0.1)

def Page1_Rotary3_Right():
    print('Page 1 Rotary 3 Right')
    wait(0.1)