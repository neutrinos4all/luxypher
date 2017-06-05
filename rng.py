#!usr/bin/env python

import random
import sys

userInput = int(raw_input("Enter a desired seed value between 1 and 100: "))
if 1 <= userInput <= 100:
	random.seed(userInput)
	randomNumber = random.random()
	print "The random number generated with your selected seed value is:", randomNumber
else:
	print "The number you used as input is not within the acceptable range of values, please try again."

