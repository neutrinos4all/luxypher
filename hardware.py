#!usr/bin/env python

import time
#import sys
import os
import random
import numpy

#status update text
print "Sending operation request to the Beagleboard light-dependent resistor..."
execfile ("ldr.py")
time.sleep(2)

#perform operations on the returned data
print "Computing averages of the returned dataset..."
data = numpy.loadtxt("ldr_readings.out")
average = numpy.average(data)
print "The average value of the returned light sensor data is:",average
time.sleep(2)

#insert the number back into a random number generator
random.seed(average)
trueRandomNumber = random.random()
print "The unique random number generated with input from the Beagleboard is:",trueRandomNumber

#this deletes ldr_readings.py (security measure)
print "Cleaning up directory, please wait...",
os.remove("ldr_readings.out")
print "done."

#this gets uncommented if you want to run the validation.py test (there are other key variables to change, see ldr.py for details
#filename = "validation.out"
#f = open(filename, "a")
#with open("validation.out", "a") as f:
#    f.write("%s \n" % trueRandomNumber)
#f.close()
