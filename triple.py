## triple.py ###################################################################
## triple integral to get the moment of inertia for an object with #############
## a defined mass distribution #################################################
################################################################################
import math
import numpy as np

def inputFloat(prompt):
	while(True):
		i = raw_input(prompt)
		try:
			i = float(i)
			return i
		except ValueError:
			print "\n non float value input, please input a float value"
			continue

def rx(y, z):
	output = y**2 + z**2
	return output
	
def rxBound(x):
	output = x
	output *= math.exp(-(x**3))
	return output


if(__name__ == "__main__"):
	xMax = inputFloat("Input upper bound for x: ")
	
	stepSize = 0.01
	
	xRange = np.arange(0, xMax, stepSize)
	
	for cy in xRange:
		print "%f, (y^2 + z^2) <= %f" % (cy, rxBound(cy))
		
