import board
import digitalio as io
import storage

input = io.Direction.INPUT
down = io.Pull.DOWN

modeswitch = io.DigitalInOut(board.GP28)
modeswitch.direction = input
modeswitch.pull = down

storage.remount('/', modeswitch.value)
