from .._base import *

########################
######## Page 1 ########
########################

# Enter a name for this page
Page1Name = 'GENERAL (Page 1)'

### Push Buttons

def Page1_Button1():
    name = 'Escape'
    kb.send(esc)
    print(f'Page 1 Button 1: {name}')
    wait(0.1)


def Page1_Button2():
    name = 'Undo'
    kb.send(ctrl,z)
    print(f'Page 1 Button 2: {name}')
    wait(0.1)

def Page1_Button3():
    name = 'Enter'
    kb.send(enter)
    print(f'Page 1 Button 3: {name}')
    wait(0.1)

def Page1_Button4():
    name = 'Transform Script'
    run_script('G:/lib/Scripts/ObjectTest.py')
    print(f'Page 1 Button 4: {name}')
    wait(0.1)

def Page1_Button5():
    name = ''
    kb.send(shift, r)
    kb.send(ctrl, r)
    kb.send(enter)
    print(f'Page 1 Button 5: {name}')
    wait(0.1)

def Page1_Button6():
    name = ''
    print(f'Page 1 Button 6: {name}')
    wait(0.1)

def Page1_Button7():
    name = ''
    print(f'Page 1 Button 7: {name}')
    wait(0.1)

def Page1_Button8():
    name = ''
    print(f'Page 1 Button 8: {name}')
    wait(0.1)

def Page1_Button9():
    name = ''
    print(f'Page 1 Button 9: {name}')
    wait(0.1)

### Rotaries

def Page1_Rotary1_Left():
    name = 'Rotate X +5'
    kb.send(r, x, kb5, enter)
    print(f'Page 1 Rotary 1 Left: {name}')

def Page1_Rotary1_Button():
    name = 'Keyframe Rotation X'
    command("bpy.context.object.keyframe_insert(data_path='rotation_euler', index=0, frame=bpy.data.scenes['Scene'].frame_current)")

def Page1_Rotary1_Right():
    name = 'Rotate X -5'
    kb.send(r, x, minus, kb5, enter)
    print(f'Page 1 Rotary 1 Right: {name}')

def Page1_Rotary2_Left():
    name = 'Rotate Y +5'
    kb.send(r, y, kb5, enter)
    print(f'Page 1 Rotary 2 Left: {name}')

def Page1_Rotary2_Button():
    name = 'Keyframe Rotation Y'
    command("bpy.context.object.keyframe_insert(data_path='rotation_euler', index=1, frame=bpy.data.scenes['Scene'].frame_current)")

def Page1_Rotary2_Right():
    name = 'Rotate Y -5'
    kb.send(r, y, minus, kb5, enter)
    print(f'Page 1 Rotary 2 Right: {name}')


def Page1_Rotary3_Left():
    name = 'Rotate Z +5'
    kb.send(r, z, kb5, enter)
    print(f'Page 1 Rotary 3 Left: {name}')


def Page1_Rotary3_Button():
    name = 'Keyframe Rotation Z'
    command("bpy.context.object.keyframe_insert(data_path='rotation_euler', index=2, frame=bpy.data.scenes['Scene'].frame_current)")

def Page1_Rotary3_Right():
    name = 'Rotate Z -5'
    kb.send(r, z, minus, kb5, enter)
    print(f'Page 1 Rotary 3 Right: {name}')
