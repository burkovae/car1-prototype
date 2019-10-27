import sys
import time

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

board = PyMata3()

PMW_PIN = 11

board.set_pin_mode(8, Constants.OUTPUT)
board.set_pin_mode(6, Constants.PWM)
board.set_pin_mode(PMW_PIN, Constants.OUTPUT)
board.servo_config(PMW_PIN)

board.digital_write(8, 1)
for i in range(128, 512):
    board.analog_write(PMW_PIN, i)
    print((i, board.get_pin_state(PMW_PIN)))
    time.sleep(0.1)


board.analog_write(PMW_PIN, 2400)
board.analog_write(6, 0)

board.digital_write(8, 0)


for i in range(128, 256):
    board.analog_write(6, i)
    print((i, board.get_pin_state(6)))
    time.sleep(0.1)
