from .._base import *

########################
######## Page 4 ########
########################

# Enter a name for this page
Page4Name = 'VSE (Page 4)'

###############
### Buttons ###
###############

# Button 1
Page4_Button1_Name = ''
def Page4_Button1():
    print('Page 4 Button 1')
    wait(0.1)

# Button 2
Page4_Button2_Name = ''
def Page4_Button2():
    print('Page 4 Button 2')
    wait(0.1)

# Button 3
Page4_Button3_Name = ''
def Page4_Button3():
    print('Page 4 Button 3')
    wait(0.1)

# Button 4
Page4_Button4_Name = ''
def Page4_Button4():
    print('Page 4 Button 4')
    wait(0.1)

# Button 5
Page4_Button5_Name = ''
def Page4_Button5():
    print('Page 4 Button 5')
    wait(0.1)

# Button 6
Page4_Button6_Name = ''
def Page4_Button6():
    print('Page 4 Button 6')
    wait(0.1)

# Button 7
Page4_Button7_Name = ''
def Page4_Button7():
    print('Page 4 Button 7')
    wait(0.1)

# Button 8
Page4_Button8_Name = ''
def Page4_Button8():
    print('Page 4 Button 8')
    wait(0.1)

# Button 9
Page4_Button9_Name = ''
def Page4_Button9():
    print('Page 4 Button 9')
    wait(0.1)


################
### Rotaries ###
################

# Rotary 1
Page4_Rotary1_Left_Name = 'Blink (Down)'
def Page4_Rotary1_Left():
    command('bpy.context.object.data.shape_keys.key_blocks['Blink'].value -= 0.05')
    print('Page 4 Rotary 1 Left')

Page4_Rotary1_Right_Name = 'Blink (Up)'
def Page4_Rotary1_Right():
    command('bpy.context.object.data.shape_keys.key_blocks['Blink'].value += 0.05')
    print('Page 4 Rotary 1 Right')

Page4_Rotary1_Button_Name = ''
def Page4_Rotary1_Button():
    command('bpy.data.shape_keys["Key"].key_blocks["Blink"].keyframe_insert(data_path='value', frame=bpy.data.scenes['Scene'].frame_current)')
    print('Page 4 Rotary 1 Button')
    wait(0.1)

# Rotary 2
Page4_Rotary2_Left_Name = 'JawOpen (Down)'
def Page4_Rotary2_Left():
    command('bpy.context.object.data.shape_keys.key_blocks['JawOpen'].value -= 0.05')
    print('Page 4 Rotary 2 Left')

Page4_Rotary2_Right_Name = 'JawOpen (Up)'
def Page4_Rotary2_Right():
    command('bpy.context.object.data.shape_keys.key_blocks['JawOpen'].value += 0.05')
    print('Page 4 Rotary 2 Right')

Page4_Rotary2_Button_Name = ''
def Page4_Rotary2_Button():
    command('bpy.data.shape_keys["Key"].key_blocks["JawOpen"].keyframe_insert(data_path='value', frame=bpy.data.scenes['Scene'].frame_current)')
    print('Page 4 Rotary 2 Button')
    wait(0.1)

# Rotary 3
Page4_Rotary3_Left_Name = 'Joy (Down)'
def Page4_Rotary3_Left():
    command('bpy.context.object.data.shape_keys.key_blocks['Joy'].value -= 0.05')
    print('Page 4 Rotary 3 Left')

Page4_Rotary3_Right_Name = 'Joy (Up)'
def Page4_Rotary3_Right():
    command('bpy.context.object.data.shape_keys.key_blocks['Joy'].value += 0.05')
    print('Page 4 Rotary 3 Right')

Page4_Rotary3_Button_Name = ''
def Page4_Rotary3_Button():
    command('bpy.data.shape_keys["Key"].key_blocks["Joy"].keyframe_insert(data_path='value', frame=bpy.data.scenes['Scene'].frame_current)')
    print('Page 4 Rotary 3 Button')
    wait(0.1)
