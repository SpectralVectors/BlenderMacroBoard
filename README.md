# BlenderMacroBoard
_Work in Progress - Alpha Build_

An open-source, customizable hardware control surface for Blender.

## Using the Board
There are two important settings that you must adjust manually, based on your setup:

1 - The Pico will show up as a USB stick on your system, allowing you to open and edit the files while you use the device. The location of the Scripts folder is currently hard-coded into the script. For me, it is the __G:/__ drive, for most Windows users it will likely be __D:/__ or __E:/__.

2 - The same is true for COM port that allows Blender to communicate with the board. After installing the Blender Addon, open up the Addon preferences, and set __USB Port__, default is __COM4__, for most Windows users it will be __COM3__, __COM4__, or __COM5__

If you do not have these set correctly you will see errors in Blender when you try to use the board.

### Layout
![](/images/BlenderMacroBoardPCBPreview.png)

### Setup
Once you have assembled the board, connect it via USB. Open the board in your file explorer, and navigate to the __Scripts__ folder, ensure that the drive letter in the script matches the drive that your board is connected to, if it is not correct, update it and save the file.

Open Blender and install the 'BlenderMacroBoard.py' found in the 'BlenderAddon' folder, then, in the addon preferences, set your COM port. Try __COM3__, __COM4__, or __COM5__, you will know it is working when the Page Change button starts to work.

Then you can start experimenting with the keys and rotary encoders. Any key or encoder can be assigned to a single keypress, a key combination, a single line bpy command, a pre-written script stored on the device, a delay or some combination of all of the above.

### Editing
You can edit the files on the device and save them, reset the board if it does not respond, or use Thonny to run the __code.py__ file again. _(Open __code.py__ in Thonny, and press Run)_

Be aware that having code open in Thonny will prevent communication between Blender and the board, so make sure to close Thonny after running the updated code, otherwise Blender will give errors.

If you wish to change/edit the functions of the board, you can do so anytime by opening the board like a USB stick, navigating to the 'Pages' folder and customizing each button on each page.

These files will allow you to see how the default presets are created, and how to customize them to your own liking.

You can add more pages, but you will have to update __Layout.py__ to reflect those changes.

### Folder Structure
![](/images/BlenderBoardFolderStructure.png)

__Raspberry Pi Pico__ is the root folder of the Pico.

__Code__ is the _code.py_ file that defines the behavior of the Pico. It is set up so that it will load variables from the __Layout__ and preset __Page__ files. Located in the root folder of the Pico.

__Lib__ is a folder that contains all of the user editable files, and some system files.

__adafruit_hid__ is a folder that contains precompiled mpy binaries that cannot be edited by the user.

__Scripts__ is a folder that contains individual script files that can be run from a button press. 

__ObjectTest__ can be used as an example for how to write your own scripts.

__BoardSetup__ is the folder that contains most of the user-editable files:

__Layout__ can be updated if you want to add more preset Pages, or if you have created a custom build _(eg. different number of keys, rotaries, potentiometers etc.)_

__base__ is a system file that imports libraries and defines the _'run_script'_ and _'command'_ functions.

__shortcodes__ is a system file that shortens the Adafruit keycodes for convenience.

__Pages__ is a folder containing all the user preset Pages.

__Page1__ is a preset file. Here you can define what function each key, rotary turn and press perform, and what name will be displayed in the Addon in Blender. You can have as many pages as you want, but you will have to update your __Layout__ file to reflect any additional pages.

The red arrows point to files that the user may wish to edit, the Preset pages, the Scripts, and the Layout (for adding extra pages and more advanced functions).
The rest can be regarded as 'system' files and will not need to be edited by 99% of users.

### Pico Prep (if you are building from scratch)
You may wish to first 'Nuke' your Pico to ensure a clean install. After connecting it as described above, you can drag and drop 'flash_nuke.uf2' from the 'UF2' folder onto your Pico.

Then, you can drag and drop 'adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.3.uf2' from the 'UF2' folder (or download it directly from Circuitpython.com) onto your Pico, and it is now ready for the files in the 'Pico' folder. Open the folder and drag the files inside to your Pico so that 'code.py' is in the root directory of the Pico, replace the existing 'code.py', and it is finally ready for use!

## Known Issues
The KiCAD files folder contains everything you should need to open up the design in KiCAD and change any elements.

The Gerber files are there for anyone not comfortable generating them on their own, however, I only created Gerber files for Rev 001 of the board, which turned out to have an issue that prevents the top rotary from properly functioning. This can be modified or omitted from the design and the device will otherwise function normally.

There is a Rev 002 KiCAD file that represents my attempt to address that, and a few other issues, however, I did not generate Gerber files or have a test board made from this iteration, so I cannot guarantee it is without fault.

Periodically, the board stops responding, and requires a restart of the PC to get it to function again. Most of the time this issue can be resolved by pressing the Reset button on the board.

Since the USB port and drive letter are set manually, it is easy for one of them to be set incorrectly and cause errors in Blender.

## Roadmap
The design philosophy of the device is to change Blender as little as possible, make using the device as simple as pluggin in a keyboard, and not require remapping of keys/controls, or anything that could potentially create conflicts with Blender's keymap, future keymap additions, or any of the thousands of addons that come with their own custom keymaps.

With support from the community, this could become the basis of a 'family' of controllers, perhaps you'd prefer to have 9 rotary encoders, perhaps 144 buttons in a 12x12 matrix, perhaps linear and rotary potentiometers to represent all the values that can go from 0-1, perhaps a trackball or trackpad, perhaps a display on the device, perhaps some combination of the above, or some way to 'chain' devices so that you could have a bank of rotary encoders in addition to the current default layout.

The goal is to offer Blender users the same type of interface that video editors get from hardware made by Blackmagic, Loupedeck, Roland, AVID or audio editors get from hardware made by Focusrite, SSL, Ableton, AVID, Presonus, Behringer and M-Audio. To grant Blender users access to knobs, switches and sliders for operations where those inputs provide the best control.
