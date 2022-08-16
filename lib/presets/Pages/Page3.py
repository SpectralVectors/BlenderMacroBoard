from ..base import *

########################
######## Page 3 ########
########################

Page3Name = 'Sculpt'

### Push Buttons

def Page3_Button1():
    kb.send(enter)

def Page3_Button2():
    kb.send(shift,ctrl,alt,z)

def Page3_Button3():
    print('p3b3')
    wait(0.1)

def Page3_Button4():
    print('p3b4')
    wait(0.1)

def Page3_Button5():
    print('p3b5')
    wait(0.1)

def Page3_Button6():
    print('p3b6')
    wait(0.1)

def Page3_Button7():
    print('p3b7')
    wait(0.1)

def Page3_Button8():
    print('p3b8')
    wait(0.1)

def Page3_Button9():
    print('p3b9')
    wait(0.1)

### Rotaries

def Page3_Rotary1_Left():
    kb.send(r, z, kb5, enter)

def Page3_Rotary1_Push():
    print('p3r1p')
    wait(0.1)

def Page3_Rotary1_Right():
    kb.send(r, z, minus, kb5, enter)

def Page3_Rotary2_Left():
    print('p3r2l')
    wait(0.1)

def Page3_Rotary2_Push():
    print('p3r2p')
    wait(0.1)

def Page3_Rotary2_Right():
    print('p3r2r')
    wait(0.1)

def Page3_Rotary3_Left():
    print('p3r3l')
    wait(0.1)

def Page3_Rotary3_Push():
    print('p3r3p')
    wait(0.1)

def Page3_Rotary3_Right():
    print('p3r3r')
    wait(0.1)