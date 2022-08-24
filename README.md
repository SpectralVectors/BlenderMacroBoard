# BlenderMacroBoard
(Work in Progress - Alpha Build)

An open-source, customizable control surface for Blender.

## How to Set Use
The project runs on a Raspberry Pi Pico, a detailed build guide will come as the project continues. For now, this guide represents how to build and use the alpha prototype, and is recommended only for users familiar with microcontroller wiring and programming. This will change as the design details and features solidify.

### Wiring
(All of the wiring directions assume the use of the default 'code.py' file above, you can, of course, change any of this in the 'code.py' file and assign any buttons to any pins. The toggle switch control is found in 'boot.py')

Buttons 0-9 are wired with pins 0-9 on the Pico on one contact, the other contact goes to ground.

The rotaries must be wired with their direction pins on consecutive Pico pins, so they are wired:
Rotary 1A - Pin 10, Rotary 1B - Pin 11, Rotary2A - Pin 12, Rotary 2B - Pin 13, Rotary 3A - Pin 14, Rotary 3B - Pin 15

If your rotaries have push button functionality, they can be wired the same way as Buttons 0-9

A toggle switch must be wired with one contact going to Pin 22 on the Pico, and the other contact going to ground. This will control the 'write' mode that the Pico will boot into, one way will allow your PC to write to the Pico's memory, but prevent the Pico from writing to its own internal memory, and the other way will prevent your PC from writing to the Pico's memory, but will allow the Pico to write to itself.

Finally, a Reset button is added, with one contact going to the 'Run' pin on the Pico, and the other contact going to ground. This is necessary to 'Refresh' the Pico, as well as to allow the user to instantly reboot to change 'write' modes.

### Software
After wiring your Pico, before you connect it to your PC, hold down the 'BOOTSEL' button, then connect it to your PC. This allows you to load the Adafruit firmware that lets it act as a keyboard/mouse etc.

You may wish to first 'Nuke' your Pico to ensure a clean install. After connecting it as described above, you can drag and drop 'flash_nuke.uf2' from the 'UF2' folder onto your Pico.

Then, eject your Pico, disconnect it, hold down 'BOOTSEL' again and reconnect it to your PC. This time you can drag and drop 'adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.3.uf2' from the 'UF2' folder (or download it directly from Circuitpython.com) onto your Pico, and it is now ready for the files in the 'Pico' folder. Open the folder and drag the files inside to your Pico so that 'code.py' is in the root directory of the Pico, replace the existing 'code.py', and it is finally ready for use!

### Functionality
Open Blender and install the 'BlenderMacroBoard.py' found in the 'BlenderAddon' folder, then you can start experimenting with the rotary encoders, each is set to rotate and keyframe one axis of the active object.

If you wish to change/edit the functions of the board, you can do so anytime by opening the board like a USB stick, navigating to the 'lib/BoardSetup/' folder and editing the 'Layout.py' file, or by going directly into the 'Pages' folder and customizing each button on each page to send: single keypresses, key combos, text, scripts, mouse moves, clicks etc.

These files will allow you to see how the default presets are created, and how to customize them to your own liking.

### Roadmap
At the moment the barrier to entry is quite high, I don't want to invest time in creating beginner-friendly build and usage guides until all the features solidify, and I can already see a number of changes that I would make to the code, and the wiring of the device itself.

This would make a slimmer build with a custom PCB to mount keyswitches and a Pico on, and it would tidy up the mess of wires currently needed to use the device. (So would using a key-matrix, see above point about changes!) And creating a custom PCB to mount an RP2040 to could open up the range of IO possibilities even further.

These could be included as Gerber files in this repo for anyone who wanted to make their own PCB (or alter the design), and possibly as kits or finished boards (if there is demand).

The design philosophy of the device is to change Blender as little as possible, make using the device as simple as pluggin in a keyboard, and not require remapping of keys/controls, or anything that could potentially create conflicts with Blender's keymap, future keymap additions, or any of the thousands of addons that come with their own custom keymaps.

It currently implements a handful of custom operators in the addon to achieve things like - macro page change notifications, running scripts in any area, keyframing individual axis rotations, but I hope to be able to create a 'behind the scenes' link between the board and Blender that would make operation totally seamless.

With support from the community, this could become the basis of a 'family' of controllers, perhaps you'd prefer to have 9 rotary encoders, perhaps 144 buttons in a 12x12 matrix, perhaps linear and rotary potentiometers to represent all the values that can go from 0-1, perhaps a trackball or trackpad, perhaps a display on the device, perhaps some combination of the above, or some way to 'chain' devices so that you could have a bank of rotary encoders in addition to the current default layout.

The goal is to offer Blender users the same type of interface that video editors get from hardware made by Blackmagic, Loupedeck, Roland, AVID or audio editors get from hardware made by Focusrite, SSL, Ableton, AVID, Presonus, Behringer and M-Audio. To grant Blender users access to knobs, switches and sliders for operations where those inputs provide the best control.
