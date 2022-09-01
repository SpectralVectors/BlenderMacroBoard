bl_info = {
    "name": "BlenderMacroBoard",
    "author": "Spectral Vectors",
    "version": (0, 0, 2),
    "blender": (2, 90, 0),
    "location": "Edit > Preferences > Addons > BlenderMacroBoard",
    "description": "A tool to configure your BlenderMacroBoard",
    "warning": "",
    "doc_url": "",
    "category": "Addons",
}

def install_serial():
    import subprocess
    import sys
    import os
    
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
    target = os.path.join(sys.prefix, 'lib', 'site-packages')
    
    subprocess.call([python_exe, '-m', 'ensurepip'])
    subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])
    
    subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pyserial', '-t', target])
    
    return{'FINISHED'}

import bpy
try:
    import serial
except:
    install_serial()

class SerialCommand(bpy.types.Operator):
    """Execute a command from serial"""
    
    bl_idname = "addon.serial_command"
    bl_label = "Serial Command"

    def execute(self, context):

        ser = serial.Serial("COM4")
        text = ser.readline().decode('utf-8')
        exec(text)
        ser.close()

        return {'FINISHED'}

class BlenderMacroBoardProperties(bpy.types.PropertyGroup):

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

    page : bpy.props.StringProperty(
        name='Macro Page',
        default='GENERAL (Page 1)',
        description='The current macro page',
    )

class PageNotification(bpy.types.Menu):
    bl_label = 'Current Page'

    def draw(self, context):
        layout = self.layout

    def menu_draw(self, context):

        bmp = bpy.context.scene.bmp
        page = bmp.page
        if page == 'GENERAL (Page 1)': 
            icon='FILE_3D'
        elif page == 'GREASE PENCIL (Page 2)':
            icon='GPBRUSH_PEN'
        elif page == 'SCULPT (Page 3)':
            icon='BRUSH_SMEAR'
        elif page == 'VSE (Page 4)':
            icon='VIEW_CAMERA'
        else:
            page = 'GENERAL (Page 1)'
            icon='FILE_3D'

        row = self.layout.row(align=True)
        row.label(icon=icon)
        row.label(text=page)
        

class BlenderMacroBoardPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):

        bmp = bpy.context.scene.bmp

        layout = self.layout
        box=layout.box()        
        column = box.column(align=True)
        row = column.row(align=True)
        box = row.box()
        box.label(text=bmp.Key1)
        box = row.box()
        box.label(text=bmp.Key2)
        box = row.box()
        box.label(text=bmp.Key3)
        row = column.row(align=True)
        box = row.box()
        box.label(text=bmp.Key4)
        box = row.box()
        box.label(text=bmp.Key5)
        box = row.box()
        box.label(text=bmp.Key6)
        row = column.row(align=True)
        box = row.box()
        box.label(text=bmp.Key7)
        box = row.box()
        box.label(text=bmp.Key8)
        box = row.box()
        box.label(text=bmp.Key9)
        column.label(text='Rotary 1:', icon='FILE_REFRESH')
        row = column.row(align=True)
        box = row.box()
        box.label(text=bmp.R1Left, icon='LOOP_BACK')
        box = row.box()
        box.label(text=bmp.R1Push, icon='SORT_ASC')
        box = row.box()
        box.label(text=bmp.R1Right, icon='LOOP_FORWARDS')
        column.label(text='Rotary 2:', icon='FILE_REFRESH')
        row = column.row(align=True)
        box = row.box()
        box.label(text=bmp.R2Left, icon='LOOP_BACK')
        box = row.box()
        box.label(text=bmp.R2Push, icon='SORT_ASC')
        box = row.box()
        box.label(text=bmp.R2Right, icon='LOOP_FORWARDS')
        column.label(text='Rotary 3:', icon='FILE_REFRESH')
        row = column.row(align=True)
        box = row.box()
        box.label(text=bmp.R3Left, icon='LOOP_BACK')
        box = row.box()
        box.label(text=bmp.R3Push, icon='SORT_ASC')
        box = row.box()
        box.label(text=bmp.R3Right, icon='LOOP_FORWARDS')



classes = [
    BlenderMacroBoardProperties,
    BlenderMacroBoardPreferences,
    PageNotification,
    SerialCommand,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.bmp = bpy.props.PointerProperty(type=BlenderMacroBoardProperties)
    bpy.types.STATUSBAR_HT_header.append(PageNotification.menu_draw)
    #bpy.types.TOPBAR_MT_editor_menus.prepend(PageNotification.menu_draw)

def unregister():
    bpy.types.STATUSBAR_HT_header.remove(PageNotification.menu_draw)
    #bpy.types.TOPBAR_MT_editor_menus.remove(PageNotification.menu_draw)

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
