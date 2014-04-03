import serial
from time import strftime
dev = raw_input("Enter device directory: ")
print "entered device", dev

serialIO = serial.Serial("/dev/tty"+dev, 38400, timeout=1)


while True :
	print "------ "+strftime("%d-%m-%Y %H:%M:%S")+" ------"

	serialIO.write("01 0C \r")
	line_rpm = serialIO.readline().split(" ")
	rpm = int("0x"+line_rpm[2]+line_rpm[3], 16)/4

	serialIO.write("01 0D \r")
	line_speed = serialIO.readline().split(" ")
	speed = int("0x"+line_speed[4], 16)

	serialIO.write("01 04 \r")
	line_load = serialIO.readline().split(" ")
	load = int("0x"+line_load[4], 16)*100/255
	
	serialIO.write("01 0B \r")
	line_map = serialIO.readline().split(" ")
	amap = int("0x"+line_map[4], 16)

	print speed+" km/h"
	print rpm+" rpm"
	print amap+" kPa"
	print "Current Load "+load+" %"
	print "-------------------------------"

