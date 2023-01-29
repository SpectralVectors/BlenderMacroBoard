from .._base import *

########################
######## Page 1 ########
########################

# Enter a name for this page
Page1Name = 'GENERAL (Page 1)'

###############
### Buttons ###
###############

# Button 1
Page1_Button1_Name = 'Escape'
def Page1_Button1():
    kb.send(esc)
    print('Page 1 Button 1')
    wait(0.1)

# Button 2
Page1_Button2_Name = 'Undo'
def Page1_Button2():
    kb.send(ctrl,z)
    print('Page 1 Button 2')
    wait(0.1)

# Button 3
Page1_Button3_Name = 'Enter'
def Page1_Button3():
    kb.send(enter)
    print('Page 1 Button 3')
    wait(0.1)

# Button 4
Page1_Button4_Name = 'Transform Script'
def Page1_Button4():
    run_script('ObjectTest.py')
    print('Page 1 Button 4')
    wait(0.1)

# Button 5
Page1_Button5_Name = 'SubSmooth'
def Page1_Button5():
    run_script('SubSmooth.py')
    print('Page 1 Button 5')
    wait(0.1)

# Button 6
Page1_Button6_Name = ''
def Page1_Button6():
    print('Page 1 Button 6')
    wait(0.1)

# Button 7
Page1_Button7_Name = ''
def Page1_Button7():
    print('Page 1 Button 7')
    wait(0.1)

# Button 8
Page1_Button8_Name = ''
def Page1_Button8():
    print('Page 1 Button 8')
    wait(0.1)

# Button 9
Page1_Button9_Name = ''
def Page1_Button9():
    print('Page 1 Button 9')
    wait(0.1)

################
### Rotaries ###
################

# Rotary 1
Page1_Rotary1_Left_Name = 'Rotate X +5'
def Page1_Rotary1_Left():
    command('bpy.context.object.rotation_euler[0] += 0.08726646')
    print('Page 1 Rotary 1 Left')

Page1_Rotary1_Right_Name = 'Rotate X -5'
def Page1_Rotary1_Right():
    command('bpy.context.object.rotation_euler[0] -= 0.08726646')
    print('Page 1 Rotary 1 Right')

Page1_Rotary1_Button_Name = 'Keyframe Rotation X'
def Page1_Rotary1_Button():
    command("bpy.context.object.keyframe_insert(data_path='rotation_euler', index=0, frame=bpy.data.scenes['Scene'].frame_current)")

# Rotary 2
Page1_Rotary2_Left_Name = 'Rotate Y +5'
def Page1_Rotary2_Left():
    command('bpy.context.object.rotation_euler[1] += 0.08726646')
    print('Page 1 Rotary 2 Left')

Page1_Rotary2_Right_Name = 'Rotate Y -5'
def Page1_Rotary2_Right():
    command('bpy.context.object.rotation_euler[1] -= 0.08726646')
    print('Page 1 Rotary 2 Right')

Page1_Rotary2_Button_Name = 'Keyframe Rotation Y'
def Page1_Rotary2_Button():
    command("bpy.context.object.keyframe_insert(data_path='rotation_euler', index=1, frame=bpy.data.scenes['Scene'].frame_current)")

# Rotary 3
Page1_Rotary3_Left_Name = 'Rotate Z +5'
def Page1_Rotary3_Left():
    command('bpy.context.object.rotation_euler[2] += 0.08726646')
    print('Page 1 Rotary 3 Left')

Page1_Rotary3_Right_Name = 'Rotate Z -5'
def Page1_Rotary3_Right():
    command('bpy.context.object.rotation_euler[2] -= 0.08726646')
    print('Page 1 Rotary 3 Right')

Page1_Rotary3_Button_Name = 'Keyframe Rotation Z'
def Page1_Rotary3_Button():
    command("bpy.context.object.keyframe_insert(data_path='rotation_euler', index=2, frame=bpy.data.scenes['Scene'].frame_current)")

