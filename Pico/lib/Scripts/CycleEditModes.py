import bpy

context = bpy.context

if context.object.mode != 'EDIT':
    # if we aren't in edit mode goto edit and set face select
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='DESELECT')
else:
    try:
        # if we are editing cycle through selection modes
        sel_mode = context.tool_settings.mesh_select_mode
        if sel_mode[0]: # vertex
            bpy.ops.mesh.select_mode(type='EDGE')
        elif sel_mode[1]: # edge
            bpy.ops.mesh.select_mode(type='FACE')
        elif sel_mode[2]: # face
            bpy.ops.mesh.select_mode(type='VERT')
    except:
        print('Not Available in this Mode')