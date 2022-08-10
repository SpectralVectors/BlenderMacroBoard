bl_info = {
    "name": "BlenderMacroBoard",
    "author": "Spectral Vectors",
    "version": (0, 0, 1),
    "blender": (2, 90, 0),
    "location": "Edit > Preferences > Addons > BlenderMacroBoard",
    "description": "A tool to configure your BlenderMacroBoard",
    "warning": "",
    "doc_url": "",
    "category": "Addons",
}

import bpy

class AssignKey1(bpy.types.Operator):
    """Assign an Operator to Key 1"""
    
    bl_idname = "addon.assign_key1"
    bl_label = "Assign Key 1"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key1Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key1 = f'{CategoryName} - {Key1Name}'
        
        return {'FINISHED'}

class AssignKey2(bpy.types.Operator):
    """Assign an Operator to Key 2"""
    
    bl_idname = "addon.assign_key2"
    bl_label = "Assign an operator to key 2"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key2Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key2 = f'{CategoryName} - {Key2Name}'
        
        return {'FINISHED'}

class AssignKey3(bpy.types.Operator):
    """Assign an Operator to Key 3"""
    
    bl_idname = "addon.assign_key3"
    bl_label = "Assign an operator to key 3"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key3Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key3 = f'{CategoryName} - {Key3Name}'
        
        return {'FINISHED'}

class AssignKey4(bpy.types.Operator):
    """Assign an Operator to Key 4"""
    
    bl_idname = "addon.assign_key4"
    bl_label = "Assign an operator to key 4"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key4Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key4 = f'{CategoryName} - {Key4Name}'
        
        return {'FINISHED'}

class AssignKey5(bpy.types.Operator):
    """Assign an Operator to Key 5"""
    
    bl_idname = "addon.assign_key5"
    bl_label = "Assign an operator to key 5"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key5Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key5 = f'{CategoryName} - {Key5Name}'
        
        return {'FINISHED'}

class AssignKey6(bpy.types.Operator):
    """Assign an Operator to Key 6"""
    
    bl_idname = "addon.assign_key6"
    bl_label = "Assign an operator to key 6"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key6Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key6 = f'{CategoryName} - {Key6Name}'
        
        return {'FINISHED'}

class AssignKey7(bpy.types.Operator):
    """Assign an Operator to Key 7"""
    
    bl_idname = "addon.assign_key7"
    bl_label = "Assign an operator to key 7"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key7Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key7 = f'{CategoryName} - {Key7Name}'
        
        return {'FINISHED'}

class AssignKey8(bpy.types.Operator):
    """Assign an Operator to Key 8"""
    
    bl_idname = "addon.assign_key8"
    bl_label = "Assign an operator to key 8"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key8Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key8 = f'{CategoryName} - {Key8Name}'
        
        return {'FINISHED'}

class AssignKey9(bpy.types.Operator):
    """Assign an Operator to Key 9"""
    
    bl_idname = "addon.assign_key9"
    bl_label = "Assign an operator to key 9"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        Key9Name = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.Key9 = f'{CategoryName} - {Key9Name}'
        
        return {'FINISHED'}

class AssignR1Left(bpy.types.Operator):
    """Assign an Operator to Rotary 1 Left Turn"""
    
    bl_idname = "addon.assign_r1left"
    bl_label = "Rotary 1 Left"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R1LeftName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R1Left = f'{CategoryName} - {R1LeftName}'
        
        return {'FINISHED'}

class AssignR1Push(bpy.types.Operator):
    """Assign an Operator to Rotary 1 Push"""
    
    bl_idname = "addon.assign_r1push"
    bl_label = "Rotary 1 Push"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R1PushName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R1Push = f'{CategoryName} - {R1PushName}'
        
        return {'FINISHED'}

class AssignR1Right(bpy.types.Operator):
    """Assign an Operator to Rotary 1 Right Turn"""
    
    bl_idname = "addon.assign_r1right"
    bl_label = "Rotary 1 Right"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R1RightName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R1Right = f'{CategoryName} - {R1RightName}'
        
        return {'FINISHED'}

class AssignR2Left(bpy.types.Operator):
    """Assign an Operator to Rotary 2 Left Turn"""
    
    bl_idname = "addon.assign_r2left"
    bl_label = "Rotary 2 Left"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R2LeftName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R2Left = f'{CategoryName} - {R2LeftName}'
        
        return {'FINISHED'}

class AssignR2Push(bpy.types.Operator):
    """Assign an Operator to Rotary 2 Push"""
    
    bl_idname = "addon.assign_r2push"
    bl_label = "Rotary 2 Push"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R2PushName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R2Push = f'{CategoryName} - {R2PushName}'
        
        return {'FINISHED'}

class AssignR2Right(bpy.types.Operator):
    """Assign an Operator to Rotary 2 Right Turn"""
    
    bl_idname = "addon.assign_r2right"
    bl_label = "Rotary 2 Right"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R2RightName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R2Right = f'{CategoryName} - {R2RightName}'
        
        return {'FINISHED'}

class AssignR3Left(bpy.types.Operator):
    """Assign an Operator to Rotary 3 Left Turn"""
    
    bl_idname = "addon.assign_r3left"
    bl_label = "Rotary 3 Left"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R3LeftName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R3Left = f'{CategoryName} - {R3LeftName}'
        
        return {'FINISHED'}

class AssignR3Push(bpy.types.Operator):
    """Assign an Operator to Rotary 3 Push"""
    
    bl_idname = "addon.assign_r3push"
    bl_label = "Rotary 3 Push"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R3PushName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R3Push = f'{CategoryName} - {R3PushName}'
        
        return {'FINISHED'}

class AssignR3Right(bpy.types.Operator):
    """Assign an Operator to Rotary 3 Right Turn"""
    
    bl_idname = "addon.assign_r3right"
    bl_label = "Rotary 3 Right"

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        col = layout.column()
        col.prop(bmb_props, 'category', expand=False)
        col.prop(bmb_props, 'operator', expand=False)

    def execute(self, context):

        bmb_props = context.scene.bmb_props

        CategoryName = str(bmb_props.category).capitalize()
        R3RightName = str(bmb_props.operator).replace('_',' ').capitalize()

        bmb_props.R3Right = f'{CategoryName} - {R3RightName}'
        
        return {'FINISHED'}

class BlenderMacroBoardProperties(bpy.types.PropertyGroup):

    Page: bpy.props.EnumProperty(
        name='Page',
        description='The page you are currently editing',
        items=[('ONE', '1', 'Page 1'),
        ('TWO', '2', 'Page 2'),
        ('THREE', '3', 'Page 3'),
        ('FOUR', '4', 'Page 4'),]
    )

    Preset: bpy.props.EnumProperty(
        name='Preset',
        description='Preset board layouts',
        items=[('CUSTOM', 'Custom', 'Custom Shortcuts'),
        ('SCULPT', 'Sculpt (Activemotionpictures)', 'Shortcuts for Sculpting'),
        ('VSE', 'Video', 'Shortcuts for the Video Sequence Editor'),
        ('MESH', 'Edit (SpectralVectors)', 'Shortcuts for Mesh Editing'),]
    )

    Key1: bpy.props.StringProperty(
        name='Key 1 Operator',
        default='[1]',
        description='The operator assigned to Key [1] on this page'
    )

    Key2: bpy.props.StringProperty(
        name='Key 2 Operator',
        default='[2]',
        description='The operator assigned to Key [2] on this page'
    )

    Key3: bpy.props.StringProperty(
        name='Key 3 Operator',
        default='[3]',
        description='The operator assigned to Key [3] on this page'
    )

    Key4: bpy.props.StringProperty(
        name='Key 4 Operator',
        default='[4]',
        description='The operator assigned to Key [4] on this page'
    )

    Key5: bpy.props.StringProperty(
        name='Key 5 Operator',
        default='[5]',
        description='The operator assigned to Key [5]on this page'
    )

    Key6: bpy.props.StringProperty(
        name='Key 6 Operator',
        default='[6]',
        description='The operator assigned to Key [6] on this page'
    )

    Key7: bpy.props.StringProperty(
        name='Key 7 Operator',
        default='[7]',
        description='The operator assigned to Key [7] on this page'
    )

    Key8: bpy.props.StringProperty(
        name='Key 8 Operator',
        default='[8]',
        description='The operator assigned to Key [8] on this page'
    )

    Key9: bpy.props.StringProperty(
        name='Key 9 Operator',
        default='[9]',
        description='The operator assigned to Key [9] on this page'
    )

    R1Left: bpy.props.StringProperty(
        name='Rotary 1 Left Turn Operator',
        default='(R1Left)',
        description='The operator assigned to Rotary 1 - [Left Turn] on this page'
    )

    R1Push: bpy.props.StringProperty(
        name='Rotary 1 Push Operator',
        default='[R1Push]',
        description='The operator assigned to Rotary 1 - [Push] on this page'
    )

    R1Right: bpy.props.StringProperty(
        name='Rotary 1 Right Turn Operator',
        default='(R1Right)',
        description='The operator assigned to Rotary 1 - [Right Turn] on this page'
    )

    R2Left: bpy.props.StringProperty(
        name='Rotary 2 Left Turn Operator',
        default='(R2Left)',
        description='The operator assigned to Rotary 2 - [Left Turn] on this page'
    )

    R2Push: bpy.props.StringProperty(
        name='Rotary 2 Push Operator',
        default='[R2Push]',
        description='The operator assigned to Rotary 2 - [Push] on this page'
    )

    R2Right: bpy.props.StringProperty(
        name='Rotary 2 Right Turn Operator',
        default='(R2Right)',
        description='The operator assigned to Rotary 2 - [Right Turn] on this page'
    )

    R3Left: bpy.props.StringProperty(
        name='Rotary 3 Left Turn Operator',
        default='(R3Left)',
        description='The operator assigned to Rotary 3 - [Left Turn] on this page'
    )

    R3Push: bpy.props.StringProperty(
        name='Rotary 3 Push Operator',
        default='[R3Push]',
        description='The operator assigned to Rotary 3 - [Push] on this page'
    )

    R3Right: bpy.props.StringProperty(
        name='Rotary 3 Right Turn Operator',
        default='(R3Right)',
        description='The operator assigned to Rotary 3 - [Right Turn] on this page'
    )

    operator_categories = []
    cat_list = dir(bpy.ops)

    for i in cat_list:
        operator_categories.append((i, i.capitalize(), ''))

    current_category = ''

    def update_cat(self, context):
        self.current_category = self.category

    def get_operators(self, context):
        operator_list = []
        op_cat = eval(f'bpy.ops.{context.scene.bmb_props.category}')
        op_list = dir(op_cat)
        
        for i in op_list:
            operator_list.append((i, i.capitalize(), ''))

        return operator_list

    category : bpy.props.EnumProperty(
        name='Category',
        description='List of Categories',
        items=operator_categories,
        update=update_cat,
        )

    operator : bpy.props.EnumProperty(
        name='Operator',
        description='List of Operators',
        items=get_operators,
        options={'ANIMATABLE'},
        )

class BlenderMacroBoardPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):

        bmb_props = bpy.context.scene.bmb_props

        layout = self.layout
        row = layout.row()
        row.label(icon='BLENDER', text='BlenderMacroBoard:')
        box=layout.box()
        box.label(text='Presets:', icon='DOCUMENTS')
        row=box.row()
        row.prop(bmb_props, 'Page', icon='TEXT')
        row.prop(bmb_props, 'Preset', icon='PRESET')
        row=box.row(align=True)
        row.operator(AssignKey1.bl_idname, text='Save Current Page as Preset', icon='PRESET_NEW')
        row.operator(AssignKey1.bl_idname, text='Load Preset from File', icon='FILEBROWSER')
        box=layout.box()        
        column = box.column(align=True)
        column.label(text='Customize Individual Keys:', icon='TOOL_SETTINGS')
        column.label(text='Keypad:', icon='VIEW_ORTHO')
        row = column.row(align=True)
        row.operator(AssignKey1.bl_idname, text=bmb_props.Key1)
        row.operator(AssignKey2.bl_idname, text=bmb_props.Key2)
        row.operator(AssignKey3.bl_idname, text=bmb_props.Key3)
        row = column.row(align=True)
        row.operator(AssignKey4.bl_idname, text=bmb_props.Key4)
        row.operator(AssignKey5.bl_idname, text=bmb_props.Key5)
        row.operator(AssignKey6.bl_idname, text=bmb_props.Key6)
        row = column.row(align=True)
        row.operator(AssignKey7.bl_idname, text=bmb_props.Key7)
        row.operator(AssignKey8.bl_idname, text=bmb_props.Key8)
        row.operator(AssignKey9.bl_idname, text=bmb_props.Key9)
        column.label(text='Rotary 1:', icon='FILE_REFRESH')
        row = column.row(align=True)
        row.operator(AssignR1Left.bl_idname, text=bmb_props.R1Left, icon='LOOP_BACK')
        row.operator(AssignR1Push.bl_idname, text=bmb_props.R1Push, icon='SORT_ASC')
        row.operator(AssignR1Right.bl_idname, text=bmb_props.R1Right, icon='LOOP_FORWARDS')
        column.label(text='Rotary 2:', icon='FILE_REFRESH')
        row = column.row(align=True)
        row.operator(AssignR2Left.bl_idname, text=bmb_props.R2Left, icon='LOOP_BACK')
        row.operator(AssignR2Push.bl_idname, text=bmb_props.R2Push, icon='SORT_ASC')
        row.operator(AssignR2Right.bl_idname, text=bmb_props.R2Right, icon='LOOP_FORWARDS')
        column.label(text='Rotary 3:', icon='FILE_REFRESH')
        row = column.row(align=True)
        row.operator(AssignR3Left.bl_idname, text=bmb_props.R3Left, icon='LOOP_BACK')
        row.operator(AssignR3Push.bl_idname, text=bmb_props.R3Push, icon='SORT_ASC')
        row.operator(AssignR3Right.bl_idname, text=bmb_props.R3Right, icon='LOOP_FORWARDS')



classes = [
    BlenderMacroBoardProperties,
    BlenderMacroBoardPreferences,
    AssignKey1,
    AssignKey2,
    AssignKey3,
    AssignKey4,
    AssignKey5,
    AssignKey6,
    AssignKey7,
    AssignKey8,
    AssignKey9,
    AssignR1Left,
    AssignR1Push,
    AssignR1Right,
    AssignR2Left,
    AssignR2Push,
    AssignR2Right,
    AssignR3Left,
    AssignR3Push,
    AssignR3Right,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.bmb_props = bpy.props.PointerProperty(type=BlenderMacroBoardProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()