#!usr/bin/env python

#This is taken from the file for homework 2. I split the reader and writer functions up into their respective files for demonstrative purposes, and included LDR.out as my sample data file.

#The following are the sensor program guts given to us by Johannes

import Adafruit_BBIO.ADC as ADC
import time

delay = 1.0
lightPin = "P9_40"

ADC.setup()

filename = "ldr_readings.out"
f = open(filename,"w")

#print "So far so good! File is created, beginning sensor detection now..."
#print "lightValue" "\t", "lightVoltage" "\n"

selection = raw_input("For how many seconds would you like to run the sensor suite? ")
iterations = int(selection)
print "Running for %d seconds, please stand by while the operation completes..." % iterations
for i in range(iterations):
	lightValue = ADC.read(lightPin)
	lightVoltage = lightValue * 1.8

#	print lightValue, "\t", lightVoltage
	f.write("%s \n" % lightValue)
	time.sleep(delay)

f.close()

print "Light data has been successfully gathered, process is advancing..."
