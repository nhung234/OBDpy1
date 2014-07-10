import serial
import os.path
from time import strftime

dev = raw_input("Enter device directory: ")
print "entered device", dev

serialIO = serial.Serial("/dev/tty"+dev, 38400, timeout=1)

directory=strftime("%d-%m-%Y")

if not os.path.exists(directory):
    os.mkdir(directory)         #it will creatte folder named by date e.g. 31-05-2014
    #if directory is exist it will not create

#PART TO COUNT FILES IN DIRECTORY TO DELETE IF MEMEORY FULL (NOT FINISH)
#path = '.'
#num_files = len([f for f in os.listdir(path)
# if os.path.isfile(os.path.join(path, f))])


f = open(strftime("%d-%m-%Y")+"/"+strftime("%d-%m-%Y_%H:%M:%S")+".txt", "w",5) #it will create a record file in the folder that has created 
#so file will store like this "31-05-2014/31-05-2014_10:15:45.txt"

while True :
#print "------ "+strftime("%d-%m-%Y %H:%M:%S")+" ------"

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
    
    serialIO.write("01 11 \r")
    line_tp = serialIO.readline().split(" ")
    tp = int("0x"+line_tp[4], 16)*100/255

    #MPG = (14.7 * 6.17 * 454 * speed * 0.621371) / (3600 * maf / 100) MPG Calculation
    f.write(repr(strftime("%H:%M:%S"))+"---- Speed:"+repr(speed)+ ", MAF:" +repr(maf)+ ", RPM:" +repr(rpm)+ ", Load:"+repr(load)+ ", TP:"+repr(tp) )
    #In file "31-05-2014_10:15:45.txt" will store the drive data 
    #e.g. "10:15:45---- Speed:20, MAF:3, RPM:1500, Load:10"
    print speed, "km/h ; ",rpm, "rpm ; ",MPG, " MPG ; Load:",load,"%"
