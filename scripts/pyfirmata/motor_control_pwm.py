
from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyACM0')

# board.bytes_available()
# board.sp.readline()
# for i in range(10):
#     print(board.sp.read())
# board.sp.readline()
# board.iterate()
# board.iterate()

pin11 = board.get_pin('d:11:p')
pin6 = board.get_pin('d:6:p')
pin8 = board.get_pin('d:8:o')


pin8.write(0)
pin11.write(1)
pin6.write(0.5)
time.sleep(1)
pin6.write(0)


for i in range(300, 1000, 5):
    print(i/1000)
    pin6.write(i/1000)
    time.sleep(0.5)

#pin6.write(1)
pin6.write(0)


# Request data and read data from serial port

for i in range(10000):
    board.send_sysex(0x01, '')
    board.bytes_available()
    distance_data = list(board.sp.read(2))
    print(distance_data, distance_data[1] * (1 << 8) + distance_data[0])

