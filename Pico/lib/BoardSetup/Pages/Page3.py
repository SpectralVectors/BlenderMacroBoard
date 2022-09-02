from .._base import *

########################
######## Page 3 ########
########################

# Enter a name for this page
Page3Name = 'SCULPT (Page 3)'

###############
### Buttons ###
###############

# Button 1
Page3_Button1_Name = ''
def Page3_Button1():
    print('Page 3 Button 1')
    wait(0.1)

# Button 2
Page3_Button2_Name = ''
def Page3_Button2():
    print('Page 3 Button 2')
    wait(0.1)

# Button 3
Page3_Button3_Name = ''
def Page3_Button3():
    print('Page 3 Button 3')
    wait(0.1)

# Button 4
Page3_Button4_Name = ''
def Page3_Button4():
    print('Page 3 Button 4')
    wait(0.1)

# Button 5
Page3_Button5_Name = ''
def Page3_Button5():
    print('Page 3 Button 5')
    wait(0.1)

# Button 6
Page3_Button6_Name = ''
def Page3_Button6():
    print('Page 3 Button 6')
    wait(0.1)

# Button 7
Page3_Button7_Name = ''
def Page3_Button7():
    print('Page 3 Button 7')
    wait(0.1)

# Button 8
Page3_Button8_Name = ''
def Page3_Button8():
    print('Page 3 Button 8')
    wait(0.1)

# Button 9
Page3_Button9_Name = ''
def Page3_Button9():
    print('Page 3 Button 9')
    wait(0.1)


################
### Rotaries ###
################

# Rotary 1
Page3_Rotary1_Left_Name = ''
def Page3_Rotary1_Left():
    print('Page 3 Rotary 1 Left')

Page3_Rotary1_Right_Name = ''
def Page3_Rotary1_Right():
    print('Page 3 Rotary 1 Right')

Page3_Rotary1_Button_Name = ''
def Page3_Rotary1_Button():
    print('Page 3 Rotary 1 Button')
    wait(0.1)

# Rotary 2
Page3_Rotary2_Left_Name = ''
def Page3_Rotary2_Left():
    print('Page 3 Rotary 2 Left')

Page3_Rotary2_Right_Name = ''
def Page3_Rotary2_Right():
    print('Page 3 Rotary 2 Right')

Page3_Rotary2_Button_Name = ''
def Page3_Rotary2_Button():
    print('Page 3 Rotary 2 Button')
    wait(0.1)

# Rotary 3
Page3_Rotary3_Left_Name = 'Remesh Voxel Size Down'
def Page3_Rotary3_Left():
    command('bpy.context.object.data.remesh_voxel_size -= 0.01')

Page3_Rotary3_Right_Name = 'Remesh Voxel Size Up'
def Page3_Rotary3_Right():
    command('bpy.context.object.data.remesh_voxel_size += 0.01')

Page3_Rotary3_Button_Name = 'Voxel Remesh'
def Page3_Rotary3_Button():
    command('bpy.ops.object.voxel_remesh()')
