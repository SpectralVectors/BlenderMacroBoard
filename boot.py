import board
import digitalio as io
import storage

input = io.Direction.INPUT
down = io.Pull.DOWN

modeswitch = io.DigitalInOut(board.GP28)
modeswitch.direction = input
modeswitch.pull = down

storage.remount('/', modeswitch.value)

if modeswitch.value:
    storage.enable_usb_drive()
else:
    storage.disable_usb_drive()
