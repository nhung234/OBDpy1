import serial
from time import strftime
dev = raw_input("Enter device directory: ")
print "entered device", dev

serialIO = serial.Serial("/dev/tty"+dev, 38400, timeout=1)

f = open(record.txt", "w")
while True :
	print "------ "+strftime("%d-%m-%Y %H:%M:%S")+" ------"

	serialIO.write("01 0C \r")
	line_rpm = serialIO.readline().split(" ")
	rpm = int("0x"+line_rpm[4]+line_rpm[5], 16)/4

	serialIO.write("01 0D \r")
	line_speed = serialIO.readline().split(" ")
	speed = int("0x"+line_speed[4], 16)

	serialIO.write("01 04 \r")
	line_load = serialIO.readline().split(" ")
	load = int("0x"+line_load[4], 16)*100/255
	
	serialIO.write("01 10 \r")
	line_maf = serialIO.readline().split(" ")
	maf = int("0x"+line_maf[4]+line_maf[5], 16)/100

	f.write(repr(strftime("%H:%M:%S"))+"----"+repr(speed)+ "km/h,  " +repr(rpm)+ "rpm,  " +repr(maf)+ " grams/sec ")
	print speed, "km/h ; ",rpm, "rpm ; ",maf, " grams/sec ; "
	print "-------------------------------"

