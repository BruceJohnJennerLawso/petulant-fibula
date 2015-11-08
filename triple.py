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
	
def integral(intervalSize, xMax):
	
	output = 0
	
	xRange = np.arange(0, xMax, intervalSize)
	
	for cy in xRange:
		print "%f, (y^2 + z^2) <= %f" % (cy, rxBound(cy))
		
	for xSlice in xRange:
		radius = rxBound(xSlice)
		yRange = np.arange(-radius, radius, intervalSize)
		for ySlice in yRange:
			if (abs(ySlice) != radius):
				## the conditional is needed here so that we dont try to
				## evaluate the edge of the circle, where our zrange will be
				## empty
				zSpan = math.sqrt(radius**2 - ySlice**2)
				zRange = np.arange(-zSpan, zSpan, intervalSize)
				for zSlice in zRange:
					output += (rx(zSlice, ySlice)*(1 + ySlice + zSlice**2))
	return output
			## how do we set up our z range...?
			

if(__name__ == "__main__"):
	xMax = inputFloat("Input upper bound for x: ")
	
	intervalSize = 0.01
	print "Moment integral around x axis: %f" % integral(intervalSize, xMax)
		
