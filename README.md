# BlenderMacroBoard
_Work in Progress - Alpha Build_

An open-source, customizable hardware control surface for Blender.

## What's in this Repo?
__BlenderAddon__ contains all the files for the Blender addon, currently just 'BlenderMacroBoard.py'

__KiCAD Gerber Files__ contains all the design files for KiCAD if you wish to modify the original design, as well as pregenerated Gerber files if you wish to have PCBs made from the existing design.

__Pico__ contains all the files needed for the Raspberry Pi Pico. Drag and drop __code.py__ and the __lib__ folder onto your Pico at any time and replace the existing __code.py__ and __lib__ folder in order to update the board, then press the Reset button to complete the update. (This assumes you have already flashed your Pico with a .uf2, if not, check the next folder...)

__UF2__ contains the Adafruit CircuitPython firmware that powers the board. If you have an assembled and tested unit you will not need to use this, if you are building from scratch then the 'nuke' uf2 can clear your existing memory before using the Adafruit uf2 to set up the system. See other guides online for how to properly flash a Pico.

__images__ contains the images on this web page, and are not necessary to build or operate the board.

## Setup the Board
Connect the board to your PC.

Ensure that you have the latest software: Download 'BlenderMacroBoard.py', and 'PicoFiles.zip' from the Releases section.

Unzip 'PicoFiles.zip', and drag and drop 'code.py', and the 'lib' folder onto your Pico. You may be asked if you want to replace the files, and you do, so click Yes to All.

Press the reset button on the Pico to finish the update.

Open Blender with Administrator privileges in Windows (right-click, select 'Run as Administrator'), then go to Edit > Preferences > Addons > Install.. and select 'BlenderMacroBoard.py'.

*IMPORTANT* Close Blender. In order to connect to the board, we need to reset the Python console that installed the libraries in the previous step, this means restarting Blender. If you don't restart Blender you will get errors when you try to 'Autodetect'.

This is the only time you will need Administrator privileges, from now on you can just open Blender normally.

Reopen Blender, on the bottom right of the screen you should see the BlenderMacroBoard Panel, it will say 'General (Page 1)'.

Click on the button and it will open a panel. Above the OK button is a button called 'Autodetect'.

Clicking 'Autodetect' will automatically identify and set the communication port, as well as the location of the 'Scripts' folder on the Pico.

Your board should now be ready to use!

(You may have to cycle through the pages for all the shortcuts to display properly, this will be addressed in a future update.)

### Layout
![](/images/BlenderMacroBoardPCBPreview.png)

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

The red arrows point to files that the user may wish to edit: the Preset pages, the Scripts, and the Layout (for adding extra pages and more advanced functions).

The rest can be regarded as 'system' files and will not need to be edited by 99% of users.

### Pico Prep (if you are building from scratch)
You may wish to first 'Nuke' your Pico to ensure a clean install. After connecting it as described above, you can drag and drop 'flash_nuke.uf2' from the 'UF2' folder onto your Pico.

Then, you can drag and drop 'adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.3.uf2' from the 'UF2' folder (or download it directly from Circuitpython.com) onto your Pico, and it is now ready for the files in the 'Pico' folder. Open the folder and drag the files inside to your Pico so that 'code.py' is in the root directory of the Pico, replace the existing 'code.py', and it is finally ready for use!

## Known Issues
The KiCAD files folder contains everything you should need to open up the design in KiCAD and change any elements.

The Gerber files are there for anyone not comfortable generating them on their own, however, I only created Gerber files for Rev 001 of the board, which turned out to have an issue that prevents the top rotary from properly functioning. This can be modified or omitted from the design and the device will otherwise function normally.

There is a Rev 002 KiCAD file that represents my attempt to address that, and a few other issues, however, I did not generate Gerber files or have a test board made from this iteration, so I cannot guarantee it is without fault.

Periodically, the board stops responding, and requires a restart of the PC to get it to function again. Most of the time this issue can be resolved by pressing the Reset button on the board.

## Roadmap
The design philosophy of the device is to change Blender as little as possible, make using the device as simple as pluggin in a keyboard, and not require remapping of keys/controls, or anything that could potentially create conflicts with Blender's keymap, future keymap additions, or any of the thousands of addons that come with their own custom keymaps.

With support from the community, this could become the basis of a 'family' of controllers, perhaps you'd prefer to have 9 rotary encoders, perhaps 144 buttons in a 12x12 matrix, perhaps linear and rotary potentiometers to represent all the values that can go from 0-1, perhaps a trackball or trackpad, perhaps a display on the device, perhaps some combination of the above, or some way to 'chain' devices so that you could have a bank of rotary encoders in addition to the current default layout.

The goal is to offer Blender users the same type of interface that video editors get from hardware made by Blackmagic, Loupedeck, Roland, AVID or audio editors get from hardware made by Focusrite, SSL, Ableton, AVID, Presonus, Behringer and M-Audio. To grant Blender users access to knobs, switches and sliders for operations where those inputs provide the best control.
