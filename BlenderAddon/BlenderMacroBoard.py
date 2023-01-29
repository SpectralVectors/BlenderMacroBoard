bl_info = {
    "name": "BlenderMacroBoard",
    "author": "Spectral Vectors",
    "version": (0, 0, 6),
    "blender": (2, 90, 0),
    "location": "Edit > Preferences > Addons > BlenderMacroBoard",
    "description": "Syncs your Board with Blender",
    "warning": "",
    "doc_url": "",
    "category": "Addons",
}

def install_dependencies():
    import subprocess
    import sys
    import os
    
    libraries = ['pyserial', 'wmi']

    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
    target = os.path.join(sys.prefix, 'lib', 'site-packages')
    
    subprocess.call([python_exe, '-m', 'ensurepip'])
    subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])
    
    for library in libraries:
        subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', library, '-t', target])
    
    return{'FINISHED'}

import bpy
try:
    import serial
    import serial.tools.list_ports
    import wmi
except:
    install_dependencies()

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

    R1Button: bpy.props.StringProperty(
        name='Rotary 1 Button Operator',
        default='[R1Button]',
        description='The operator assigned to Rotary 1 - [Button] on this page'
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

    R2Button: bpy.props.StringProperty(
        name='Rotary 2 Button Operator',
        default='[R2Button]',
        description='The operator assigned to Rotary 2 - [Button] on this page'
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

    R3Button: bpy.props.StringProperty(
        name='Rotary 3 Button Operator',
        default='[R3Button]',
        description='The operator assigned to Rotary 3 - [Button] on this page'
    )

    R3Right: bpy.props.StringProperty(
        name='Rotary 3 Right Turn Operator',
        default='(R3Right)',
        description='The operator assigned to Rotary 3 - [Right Turn] on this page'
    )

    Page : bpy.props.StringProperty(
        name='Macro Page',
        default='GENERAL (Page 1)',
        description='The current macro page',
    )

    Port : bpy.props.StringProperty(
        name='USB Port',
        default='COM3',
        description='The port used by the board for serial communication, often: Win: COM4, Linux: ttyACM0, Mac: /dev/tty.usbmodem...',
    )

    DriveLetter : bpy.props.StringProperty(
        name='Drive Letter',
        default='G:',
        description='The drive letter of the storage on the board, often: Win: D:, E:,...',
    )

class SerialCommand(bpy.types.Operator):
    """Execute a command from serial"""
    
    bl_idname = "addon.serial_command"
    bl_label = "Serial Command"

    def execute(self, context):

        bmp = bpy.context.scene.bmp
        ser = serial.Serial(bmp.Port)
        text = ser.readline().decode('utf-8')
        exec(text)
        ser.close()

        return {'FINISHED'}
    
class AutoDetectBoard(bpy.types.Operator):
    """Automatically detect the port and drive letter of the board."""
    
    bl_idname = "addon.autodetect_board"
    bl_label = "Autodetect"

    def execute(self, context):

        bmp = bpy.context.scene.bmp

        # Get the port number
        list = serial.tools.list_ports.comports(include_links=False)

        for item in list:
            if item.description.startswith('USB') and item.vid == 9114 and item.pid == 33012:
                bmp.Port = item.name

        # Get the drive letter
        model = 'Raspberr Pico USB Device'

        disks                      = wmi.WMI().Win32_DiskDrive()
        drives_to_partitions       = wmi.WMI().Win32_DiskDriveToDiskPartition()
        paritions_to_logical_disks = wmi.WMI().Win32_LogicalDiskToPartition()

        drive_letter_name       = None
        cf_drive_partition_name = None
        drive_device_id         = None

        for disk in disks:
            if disk.Model == model:
                drive_device_id = disk.DeviceID

        if drive_device_id != None:
            for d_2_p in drives_to_partitions:
                if d_2_p.Antecedent.DeviceID == drive_device_id:
                    cf_drive_partition_name = d_2_p.Dependent.DeviceID 

        if cf_drive_partition_name != None:
            for p_2_ld in paritions_to_logical_disks:
                if p_2_ld.Antecedent.DeviceID == cf_drive_partition_name:
                    drive_letter_name = p_2_ld.Dependent.DeviceID

        bmp.DriveLetter = drive_letter_name

        drive = bmp.DriveLetter

        file = open(f'{drive}/lib/BoardSetup/_drive.py', 'w')
        file.write(f"drive = '{drive}'")
        file.close()

        return {'FINISHED'}

class KeyLayoutViewer(bpy.types.Operator):
    bl_idname = "addon.key_layout_viewer"
    bl_label = "Current Page:"

    def execute(self, context):
        print('Viewing Key Layout')
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=480)

    def draw(self, context):
        
        bmp = bpy.context.scene.bmp

        layout = self.layout

        box = layout.box()
        box.label(text=bmp.Page)
        box=layout.box()
        box.label(text='Globals:', icon='WORLD')
        column = box.column(align=True)
        row = column.row(align=True)
        box = row.box()
        box.label(text='Scrub Timeline', icon='FILE_REFRESH')
        box = row.box()
        box.label(text='Reset Board', icon='QUIT')
        box = row.box()
        box.label(text='Page Change', icon='DUPLICATE')

        box=layout.box()
        box.label(text='Buttons:', icon='FILE_VOLUME')
        column = box.column(align=True)
        row = column.row(align=True)
        box = row.box()
        box.label(text=f'[1]  {bmp.Key1}')
        box = row.box()
        box.label(text=f'[2]  {bmp.Key2}')
        box = row.box()
        box.label(text=f'[3]  {bmp.Key3}')
        row = column.row(align=True)
        box = row.box()
        box.label(text=f'[4]  {bmp.Key4}')
        box = row.box()
        box.label(text=f'[5]  {bmp.Key5}')
        box = row.box()
        box.label(text=f'[6]  {bmp.Key6}')
        row = column.row(align=True)
        box = row.box()
        box.label(text=f'[7]  {bmp.Key7}')
        box = row.box()
        box.label(text=f'[8]  {bmp.Key8}')
        box = row.box()
        box.label(text=f'[9]  {bmp.Key9}')

        column.label(text='Rotary Encoders:', icon='FILE_REFRESH')
        row = column.row()
        column = row.column(align=True)
        column.label(text='Rotary 1:')
        box = column.box()
        box.label(text=bmp.R1Left, icon='LOOP_BACK')
        box = column.box()
        box.label(text=bmp.R1Right, icon='LOOP_FORWARDS')
        box = column.box()
        box.label(text=bmp.R1Button, icon='SORT_ASC')

        column = row.column(align=True)
        column.label(text='Rotary 2:')
        box = column.box()
        box.label(text=bmp.R2Left, icon='LOOP_BACK')
        box = column.box()
        box.label(text=bmp.R2Right, icon='LOOP_FORWARDS')
        box = column.box()
        box.label(text=bmp.R2Button, icon='SORT_ASC')

        column = row.column(align=True)
        column.label(text='Rotary 3:')
        box = column.box()
        box.label(text=bmp.R3Left, icon='LOOP_BACK')
        box = column.box()
        box.label(text=bmp.R3Right, icon='LOOP_FORWARDS')
        box = column.box()
        box.label(text=bmp.R3Button, icon='SORT_ASC')

        layout.operator('addon.autodetect_board', icon='EXTERNAL_DRIVE')


class WM_MT_PageNotification(bpy.types.Menu):
    bl_label = 'Current Page'

    def draw(self, context):
        layout = self.layout

    def menu_draw(self, context):

        bmp = bpy.context.scene.bmp
        page = bmp.Page
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
        row.operator('addon.key_layout_viewer', text=page, icon=icon)
        

class BlenderMacroBoardPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):

        bmp = bpy.context.scene.bmp

        layout = self.layout
        box = layout.box()
        row = box.row()
        row.prop(bmp, 'Port')
        row = box.row()
        row.prop(bmp, 'DriveLetter')
        row = box.row()
        row.operator('addon.autodetect_board', icon='EXTERNAL_DRIVE')


classes = [
    BlenderMacroBoardProperties,
    BlenderMacroBoardPreferences,
    WM_MT_PageNotification,
    SerialCommand,
    KeyLayoutViewer,
    AutoDetectBoard,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.bmp = bpy.props.PointerProperty(type=BlenderMacroBoardProperties)
    bpy.types.STATUSBAR_HT_header.append(WM_MT_PageNotification.menu_draw)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    km = kc.keymaps.new(
        name="Window",
        space_type='EMPTY',
        region_type='WINDOW'
        )
        
    kmi = km.keymap_items.new(
        "addon.serial_command",
        'INSERT',
        'PRESS',
        shift = 1,
        ctrl = 1,
        alt = 1,
        )

    kmi.active = True

def unregister():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps['Window']

    for kmi in wm.keyconfigs.addon.keymaps['Window'].keymap_items:
        if kmi.idname == 'addon.serial_command':
            km.keymap_items.remove(kmi)

    bpy.types.STATUSBAR_HT_header.remove(WM_MT_PageNotification.menu_draw)

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
