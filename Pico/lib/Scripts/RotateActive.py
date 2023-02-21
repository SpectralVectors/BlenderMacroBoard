import bpy

context = bpy.context
bmp = context.scene.bmp
mode = context.mode
object = context.object
type = object.type
data = object.data

direction = bmp.Direction
value = bmp.Value
axis = bmp.Axis

_axis = {
    '0':(True,False,False),
    '1':(False,True,False),
    '2':(False,False,True),
}

if type == 'MESH':
    if mode == 'EDIT_MESH':
        bpy.ops.transform.rotate(value=value*direction, constraint_axis=_axis[str(axis)])
    else:
        object.rotation_euler[axis] += value*direction

elif type == 'ARMATURE':
    if mode == 'POSE':
        bone = context.selected_pose_bones[0]
        bone.rotation_mode = 'XYZ'
        bone.rotation_euler[axis] += value*direction
        
    elif mode == 'EDIT_ARMATURE':
        bpy.ops.transform.rotate(value=value*direction, constraint_axis=_axis[str(axis)])
    
    else:
        object.rotation_euler[axis] += value*direction

elif type == 'CURVE':
    if mode == 'EDIT_CURVE':
        bpy.ops.transform.rotate(value=value*direction, constraint_axis=_axis[str(axis)])

    else:
        object.rotation_euler[axis] += value*direction
        
else:
    object.rotation_euler[axis] += value*direction
