import serial


ser = serial.Serial('/dev/ttyACM0', 9600)  # Establish the connection on a specific port
for i in range(1000):
    print(ser.readline())
