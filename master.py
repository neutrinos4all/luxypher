#!usr/bin/env python

import time
import sys  

#print initialization line
print "Initializing luxypher 0.8, please stand by...",
sys.stdout.flush()
time.sleep(2)
print "done."
time.sleep(1)

#print frontmatter for the user to read and choose an option
print "Welcome! You have two options:\n\t[1] initializes the pseudo-random number generator function;\n\t[2] initializes the hardware random number generator."
print "WARNING: You should note that every pseudo-random number generator is cryptologically insecure. If this program is being used to generate encryption keys, use the hardware random number generator." 

#user makes the program selection here
selection = raw_input("Which one would you like to use? ")
rng = int(selection)
if rng == 1:
	print "You selected to use the pseudo-random hardware generator. Initializing program..."
	execfile("rng.py")
elif rng == 2:
	print "You selected to use the hardware random hardware generator. Initializing program..."
	execfile("hardware.py")
else:
	print "Invalid selection. Please select one of the options above."
