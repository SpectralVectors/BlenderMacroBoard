import bpy

bpy.ops.transform.translate(value=(1,0,0))
bpy.ops.transform.rotate(value=30,orient_axis='X')
bpy.ops.transform.resize(value=(2,1,3))
bpy.context.object.location[0] += 5