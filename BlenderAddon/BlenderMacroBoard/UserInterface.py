from bpy_types import Operator, Menu, AddonPreferences

class KeyLayoutViewer(Operator):
    """View the button assignments for each macro page"""
    bl_idname = "addon.key_layout_viewer"
    bl_label = "Current Page:"

    def execute(self, context):
        print('Viewing Key Layout')
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=480)

    def draw(self, context):
        
        bmp = context.scene.bmp

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


class WM_MT_PageNotification(Menu):
    """Display the current page name and icon in the Status Bar"""
    bl_label = 'Current Page'

    def draw(self, context):
        layout = self.layout

    def menu_draw(self, context):

        bmp = context.scene.bmp
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
        

class BlenderMacroBoardPreferences(AddonPreferences):
    bl_idname = __name__

    def draw(self, context):

        bmp = context.scene.bmp

        layout = self.layout
        box = layout.box()
        row = box.row()
        row.prop(bmp, 'Port')
        row = box.row()
        row.prop(bmp, 'DriveLetter')
        row = box.row()
        row.operator('addon.autodetect_board', icon='EXTERNAL_DRIVE')