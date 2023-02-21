import bpy

context = bpy.context
bmp = context.scene.bmp
mode = context.mode
object = context.object
type = object.type
data = object.data

axis = bmp.Axis

if type == 'MESH':
    if mode == 'EDIT_MESH':
        bpy.ops.addon.messagebox('INVOKE_DEFAULT', Message='You cannot keyframe mesh data!')
    else:
        object.keyframe_insert(data_path='rotation_euler', index=axis)

elif type == 'ARMATURE':
    if mode == 'POSE':
        bone = context.selected_pose_bones[0]
        bone.rotation_mode = 'XYZ'
        bone.keyframe_insert(data_path='rotation_euler', index=axis)
        
    elif mode == 'EDIT_ARMATURE':
        bpy.ops.addon.messagebox('INVOKE_DEFAULT', Message='You cannot keyframe edit bones!')
    
    else:
        object.keyframe_insert(data_path='rotation_euler', index=axis)

elif type == 'CURVE':
    if mode == 'EDIT_CURVE':
        bpy.ops.addon.messagebox('INVOKE_DEFAULT', Message='You cannot keyframe bezier points!')

    else:
        object.keyframe_insert(data_path='rotation_euler', index=axis)
        
else:
    object.keyframe_insert(data_path='rotation_euler', index=axis)

object.hide_render = object.hide_render
