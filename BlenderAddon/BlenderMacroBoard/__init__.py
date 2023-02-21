bl_info = {
    "name": "BlenderMacroBoard",
    "author": "Spectral Vectors",
    "version": (0, 0, 7),
    "blender": (2, 90, 0),
    "location": "Edit > Preferences > Addons > BlenderMacroBoard",
    "description": "Syncs your Board with Blender",
    "warning": "This addon is under development",
    "doc_url": "https://github.com/SpectralVectors/BlenderMacroBoard",
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

from email import message
import bpy
from bpy_types import Operator
try:
    import serial
    import serial.tools.list_ports
    import wmi
except:
    install_dependencies()

from .Properties import BlenderMacroBoardProperties
from .UserInterface import KeyLayoutViewer, WM_MT_PageNotification, BlenderMacroBoardPreferences

class MacroMessageBox(Operator):
    """Display a popup text message"""
    bl_idname = "addon.messagebox"
    bl_label = "Macro Board Error!"

    Message : bpy.props.StringProperty(
        name='Message',
        default='Board Error',
        description='Popup for Board-related messages.',
    )

    def execute(self, context):
        self.report({'INFO'}, self.Message)
        print(self.Message)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)

    def draw(self, context):
        self.layout.label(text=self.Message, icon="SEQUENCE_COLOR_01")

class SerialCommand(Operator):
    """Execute a command from serial"""
    bl_idname = "addon.serial_command"
    bl_label = "Serial Command"

    def execute(self, context):

        bmp = context.scene.bmp
        ser = serial.Serial(bmp.Port)
        text = ser.readline().decode('utf-8')
        exec(text)
        ser.close()

        return {'FINISHED'}

class AutoDetectBoard(Operator):
    """Automatically detect the port and drive letter of the board."""
    bl_idname = "addon.autodetect_board"
    bl_label = "Autodetect"

    def execute(self, context):

        bmp = context.scene.bmp

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

        # Write Drive Letter data to file on Pico for local access
        file = open(f'{drive}/lib/BoardSetup/_drive.py', 'w')
        file.write(f"drive = '{drive}'")
        file.close()

        return {'FINISHED'}

classes = [
    BlenderMacroBoardProperties,
    BlenderMacroBoardPreferences,
    WM_MT_PageNotification,
    SerialCommand,
    KeyLayoutViewer,
    AutoDetectBoard,
    MacroMessageBox,
]

def add_keymap():
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

def clear_keymap():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps['Window']

    for kmi in wm.keyconfigs.addon.keymaps['Window'].keymap_items:
        if kmi.idname == 'addon.serial_command':
            km.keymap_items.remove(kmi)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.bmp = bpy.props.PointerProperty(type=BlenderMacroBoardProperties)
    bpy.types.STATUSBAR_HT_header.append(WM_MT_PageNotification.menu_draw)

    add_keymap()

def unregister():
    clear_keymap()

    bpy.types.STATUSBAR_HT_header.remove(WM_MT_PageNotification.menu_draw)

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__package__":
    register()
