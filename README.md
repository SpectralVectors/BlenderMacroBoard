# BlenderMacroBoard
_Work in Progress - Alpha Build_

An open-source, customizable hardware control surface for Blender.

## How to Setup & Use
The project runs on a Raspberry Pi Pico, a detailed build guide will come as the project continues. For now, this guide represents how to build and use the alpha prototype, and is recommended only for users familiar with microcontroller wiring and programming. This will change as the design details and features solidify.

### Layout
![](/images/BlenderMacroBoardPCBPreview.png)

### Software
You may wish to first 'Nuke' your Pico to ensure a clean install. After connecting it as described above, you can drag and drop 'flash_nuke.uf2' from the 'UF2' folder onto your Pico.

Then, you can drag and drop 'adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.3.uf2' from the 'UF2' folder (or download it directly from Circuitpython.com) onto your Pico, and it is now ready for the files in the 'Pico' folder. Open the folder and drag the files inside to your Pico so that 'code.py' is in the root directory of the Pico, replace the existing 'code.py', and it is finally ready for use!

### Functionality
Open Blender and install the 'BlenderMacroBoard.py' found in the 'BlenderAddon' folder, then you can start experimenting with the rotary encoders, each is set to rotate and keyframe one axis of the active object.

If you wish to change/edit the functions of the board, you can do so anytime by opening the board like a USB stick, navigating to the 'lib/BoardSetup/' folder and editing the 'Layout.py' file, or by going directly into the 'Pages' folder and customizing each button on each page to send: single keypresses, key combos, text, scripts, mouse moves, clicks etc.

These files will allow you to see how the default presets are created, and how to customize them to your own liking.

### Folder Structure
![](/images/BlenderBoardFolderStructure.png)
The red arrows point to files that the user may wish to edit, the Preset pages, the Scripts, and the Layout (for adding extra pages and more advanced functions).
The rest can be regarded as 'system' files and will not need to be edited by 99% of users.

## Roadmap
The design philosophy of the device is to change Blender as little as possible, make using the device as simple as pluggin in a keyboard, and not require remapping of keys/controls, or anything that could potentially create conflicts with Blender's keymap, future keymap additions, or any of the thousands of addons that come with their own custom keymaps.

With support from the community, this could become the basis of a 'family' of controllers, perhaps you'd prefer to have 9 rotary encoders, perhaps 144 buttons in a 12x12 matrix, perhaps linear and rotary potentiometers to represent all the values that can go from 0-1, perhaps a trackball or trackpad, perhaps a display on the device, perhaps some combination of the above, or some way to 'chain' devices so that you could have a bank of rotary encoders in addition to the current default layout.

The goal is to offer Blender users the same type of interface that video editors get from hardware made by Blackmagic, Loupedeck, Roland, AVID or audio editors get from hardware made by Focusrite, SSL, Ableton, AVID, Presonus, Behringer and M-Audio. To grant Blender users access to knobs, switches and sliders for operations where those inputs provide the best control.
