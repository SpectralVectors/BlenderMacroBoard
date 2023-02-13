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
Page1_Button3_Name = 'Redo'
def Page1_Button3():
    kb.send(shift, ctrl, z)
    print('Page 1 Button 3')
    wait(0.1)

# Button 4
Page1_Button4_Name = 'Cycle Edit Mode'
def Page1_Button4():
    run_script('CycleEditModes.py')
    print('Page 1 Button 4')
    wait(0.1)

# Button 5
Page1_Button5_Name = 'Merge at Center'
def Page1_Button5():
    command("bpy.ops.mesh.merge(type='CENTER') if bpy.context.object.mode == 'EDIT' else print('Cannot perform the operation in this context')")
    print('Page 1 Button 5')
    wait(0.1)

# Button 6
Page1_Button6_Name = 'Mark as Seam'
def Page1_Button6():
    command("bpy.ops.mesh.mark_seam(clear=False) if bpy.context.object.mode == 'EDIT' else print('Cannot perform the operation in this context')")
    print('Page 1 Button 6')
    wait(0.1)

# Button 7
Page1_Button7_Name = 'Jump to Previous Keyframe'
def Page1_Button7():
    kb.send(down)
    print('Page 1 Button 7')
    wait(0.1)

# Button 8
Page1_Button8_Name = 'Delete Active'
def Page1_Button8():
    kb.send(x, d)
    print('Page 1 Button 8')
    wait(0.1)

# Button 9
Page1_Button9_Name = 'Jump to Next Keyframe'
def Page1_Button9():
    kb.send(up)
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

