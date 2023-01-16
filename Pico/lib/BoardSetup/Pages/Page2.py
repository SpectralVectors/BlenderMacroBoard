from .._base import *

########################
######## Page 2 ########
########################

# Enter a name for this page
Page2Name = 'GREASE PENCIL (Page 2)'

###############
### Buttons ###
###############

# Button 1
Page2_Button1_Name = ''
def Page2_Button1():
    print('Page 2 Button 1')
    wait(0.1)

# Button 2
Page2_Button2_Name = ''
def Page2_Button2():
    print('Page 2 Button 2')
    wait(0.1)

# Button 3
Page2_Button3_Name = ''
def Page2_Button3():
    print('Page 2 Button 3')
    wait(0.1)

# Button 4
Page2_Button4_Name = ''
def Page2_Button4():
    print('Page 2 Button 4')
    wait(0.1)

# Button 5
Page2_Button5_Name = ''
def Page2_Button5():
    print('Page 2 Button 5')
    wait(0.1)

# Button 6
Page2_Button6_Name = ''
def Page2_Button6():
    print('Page 2 Button 6')
    wait(0.1)

# Button 7
Page2_Button7_Name = ''
def Page2_Button7():
    print('Page 2 Button 7')
    wait(0.1)

# Button 8
Page2_Button8_Name = ''
def Page2_Button8():
    print('Page 2 Button 8')
    wait(0.1)

# Button 9
Page2_Button9_Name = ''
def Page2_Button9():
    print('Page 2 Button 9')
    wait(0.1)

################
### Rotaries ###
################

# Rotary 1
Page2_Rotary1_Left_Name = 'Brush Size Up'
def Page2_Rotary1_Left():
    kb.send(left_bracket)

Page2_Rotary1_Right_Name = 'Brush Size Down'
def Page2_Rotary1_Right():
    kb.send(right_bracket)

Page2_Rotary1_Button_Name = 'Sculpt/Draw Mode Toggle'
def Page2_Rotary1_Button():
    command("bpy.ops.object.mode_set(mode='PAINT_GPENCIL') if bpy.context.mode == 'SCULPT_GPENCIL' else bpy.ops.object.mode_set(mode='SCULPT_GPENCIL')")

# Rotary 2
Page2_Rotary2_Left_Name = ''
def Page2_Rotary2_Left():
    print('Page 2 Rotary 2 Left')

Page2_Rotary2_Right_Name = ''
def Page2_Rotary2_Right():
    print('Page 2 Rotary 2 Right')

Page2_Rotary2_Button_Name = 'Insert Blank Keyframe'
def Page2_Rotary2_Button():
    command('bpy.ops.gpencil.blank_frame_add(all_layers=True)')

# Rotary 3
Page2_Rotary3_Left_Name = 'Previous Frame'
def Page2_Rotary3_Left():
    kb.send(left)

Page2_Rotary3_Right_Name = 'Next Frame'
def Page2_Rotary3_Right():
    kb.send(right)

Page2_Rotary3_Button_Name = 'Duplicate Active Keyframe'
def Page2_Rotary3_Button():
    command('bpy.ops.gpencil.frame_duplicate()')
