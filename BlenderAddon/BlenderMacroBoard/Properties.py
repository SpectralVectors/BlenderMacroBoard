from bpy_types import PropertyGroup
from bpy.props import StringProperty, IntProperty, FloatProperty

class BlenderMacroBoardProperties(PropertyGroup):
    
    Key1: StringProperty(
        name='Key 1 Operator',
        default='[1]',
        description='The operator assigned to Key [1] on this page'
    )

    Key2: StringProperty(
        name='Key 2 Operator',
        default='[2]',
        description='The operator assigned to Key [2] on this page'
    )

    Key3: StringProperty(
        name='Key 3 Operator',
        default='[3]',
        description='The operator assigned to Key [3] on this page'
    )

    Key4: StringProperty(
        name='Key 4 Operator',
        default='[4]',
        description='The operator assigned to Key [4] on this page'
    )

    Key5: StringProperty(
        name='Key 5 Operator',
        default='[5]',
        description='The operator assigned to Key [5]on this page'
    )

    Key6: StringProperty(
        name='Key 6 Operator',
        default='[6]',
        description='The operator assigned to Key [6] on this page'
    )

    Key7: StringProperty(
        name='Key 7 Operator',
        default='[7]',
        description='The operator assigned to Key [7] on this page'
    )

    Key8: StringProperty(
        name='Key 8 Operator',
        default='[8]',
        description='The operator assigned to Key [8] on this page'
    )

    Key9: StringProperty(
        name='Key 9 Operator',
        default='[9]',
        description='The operator assigned to Key [9] on this page'
    )

    R1Left: StringProperty(
        name='Rotary 1 Left Turn Operator',
        default='(R1Left)',
        description='The operator assigned to Rotary 1 - [Left Turn] on this page'
    )

    R1Button: StringProperty(
        name='Rotary 1 Button Operator',
        default='[R1Button]',
        description='The operator assigned to Rotary 1 - [Button] on this page'
    )

    R1Right: StringProperty(
        name='Rotary 1 Right Turn Operator',
        default='(R1Right)',
        description='The operator assigned to Rotary 1 - [Right Turn] on this page'
    )

    R2Left: StringProperty(
        name='Rotary 2 Left Turn Operator',
        default='(R2Left)',
        description='The operator assigned to Rotary 2 - [Left Turn] on this page'
    )

    R2Button: StringProperty(
        name='Rotary 2 Button Operator',
        default='[R2Button]',
        description='The operator assigned to Rotary 2 - [Button] on this page'
    )

    R2Right: StringProperty(
        name='Rotary 2 Right Turn Operator',
        default='(R2Right)',
        description='The operator assigned to Rotary 2 - [Right Turn] on this page'
    )

    R3Left: StringProperty(
        name='Rotary 3 Left Turn Operator',
        default='(R3Left)',
        description='The operator assigned to Rotary 3 - [Left Turn] on this page'
    )

    R3Button: StringProperty(
        name='Rotary 3 Button Operator',
        default='[R3Button]',
        description='The operator assigned to Rotary 3 - [Button] on this page'
    )

    R3Right: StringProperty(
        name='Rotary 3 Right Turn Operator',
        default='(R3Right)',
        description='The operator assigned to Rotary 3 - [Right Turn] on this page'
    )

    Page : StringProperty(
        name='Macro Page',
        default='GENERAL (Page 1)',
        description='The current macro page',
    )

    Port : StringProperty(
        name='USB Port',
        default='COM3',
        description='The port used by the board for serial communication, often: Win: COM4, Linux: ttyACM0, Mac: /dev/tty.usbmodem...',
    )

    DriveLetter : StringProperty(
        name='Drive Letter',
        default='G:',
        description='The drive letter of the storage on the board, often: Win: D:, E:,...',
    )

    ActiveItem : StringProperty(
        name='Active Item',
        default='bpy.context.object',
        description='The currently active item: Object, Mesh, Vertex, Armature, Bone, Curve, Bezier Point etc.',
    )

    Direction : IntProperty(
        name='Direction',
        default=1,
        description='The direction of the current action: positive or negative, 1 or -1',
        min=-1,
        max=1,
    )

    Value : FloatProperty(
        name='Value',
        default=0.08726646,
        description='The amount of the current action: how far to rotate, how much to scale etc',
    )

    Axis : IntProperty(
        name='Axis',
        default=0,
        description='The axis to perform the current action on: X = 0, Y = 1, Z = 2',
        min=0,
        max=2,
    )