from .._base import *

########################
######## Page 3 ########
########################

# Enter a name for this page
Page3Name = 'SCULPT (Page 3)'

### Push Buttons

def Page3_Button1():
    print('Page 3 Button 1')
    wait(0.1)

def Page3_Button2():
    print('Page 3 Button 2')
    wait(0.1)

def Page3_Button3():
    print('Page 3 Button 3')
    wait(0.1)

def Page3_Button4():
    print('Page 3 Button 4')
    wait(0.1)

def Page3_Button5():
    print('Page 3 Button 5')
    wait(0.1)

def Page3_Button6():
    print('Page 3 Button 6')
    wait(0.1)

def Page3_Button7():
    print('Page 3 Button 7')
    wait(0.1)

def Page3_Button8():
    print('Page 3 Button 8')
    wait(0.1)

def Page3_Button9():
    print('Page 3 Button 9')
    wait(0.1)

### Rotaries

def Page3_Rotary1_Left():
    print('Page 3 Rotary 1 Left')
    kb.send(s, x, kb2, enter)

def Page3_Rotary1_Button():
    print('Page 3 Rotary 1 Button')
    wait(0.1)

def Page3_Rotary1_Right():
    print('Page 3 Rotary 1 Right')
    kb.send(s, x, kb0, dot, kb5, enter)

def Page3_Rotary2_Left():
    print('Page 3 Rotary 2 Left')
    kb.send(s, y, kb2, enter)

def Page3_Rotary2_Button():
    print('Page 3 Rotary 2 Button')
    wait(0.1)

def Page3_Rotary2_Right():
    print('Page 3 Rotary 2 Right')
    kb.send(s, y, kb0, dot, kb5, enter)


def Page3_Rotary3_Left():
    print('Page 3 Rotary 3 Left')
    kb.send(s, z, kb2, enter)

def Page3_Rotary3_Button():
    print('Page 3 Rotary 3 Button')
    wait(0.1)

def Page3_Rotary3_Right():
    print('Page 3 Rotary 3 Right')
    kb.send(s, z, kb0, dot, kb5, enter)
