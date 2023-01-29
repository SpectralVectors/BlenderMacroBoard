import bpy

bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 2
bpy.ops.object.shade_smooth(use_auto_smooth=True)
