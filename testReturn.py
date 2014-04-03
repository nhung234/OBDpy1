import serial

dev_name = input("Enter device name: ")

ser = serial.Serial("/dev/tty"+dev_name, 38400, timeout=1)

test_command = input("Command: ")
ser.write(test_command+"\r")
line = ser.readline()
print line 
