#!usr/bin/env python

import time	

for x in range(0,249):
	execfile("hardware.py")
	time.sleep(2)
	print "Iteration %s complete." % x

print "Readings complete!"
