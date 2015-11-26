## triple.py ###################################################################
## triple integral to get the moment of inertia for an object with #############
## a defined mass distribution #################################################
################################################################################
import math
import numpy as np


def inputFloat(prompt):
	## requests input from the user and continually loops if its getting garbage
	## input (ie something that isnt a float)
	while(True):
		i = raw_input(prompt)
		try:
			i = float(i)
			return i
		except ValueError:
			print "\n non float value input, please input a float value"
			continue

def rx(y, z):
	## the radius squared of the object around the x axis
	output = y**2 + z**2
	return output
	
def rxBound(x):
	## the maximum value of rx for some value of x. Basically the radius squared
	## of the object around the x axis for some value of x
	output = x
	output *= math.exp(-(x**3))
	return output
	
def f(x, y, z):
	## the function we are integrating, composed of the r^2 part
	## (as we are integrating m*(r^2) over the volume, and the mass distribution
	## function (1 + y + z**2), which describes where the mass is concentrated
	output = rx(y, z)*(1 + y + z**2)
	return output	
	
	
	
def integralTrapezoid(intervalSize, xMax):
	xRange = np.arange(0, xMax, intervalSize)
	## create our xRange, extending from 0 to whatever our maximum input of x
	## was			
	output = 0				
	for i in range(0, len(xRange)-1):
		print i, len(xRange)
		## our order of integration is dxdydz
		radius = rxBound(xRange[i])
		## the region we are integrating is a function rx <= x*exp(-(x^3))
		## rotated around the x axis, so we can subdivide it into circles
		## evenly spaced between x=0 and our maximum x input
		
		## the rxBound function defined above is the boundary on rx, which is
		## the radius squared, so we take the square root to get the actual
		## square root
		yRange = np.arange(-radius, radius, intervalSize)
		for j in range(0, len(yRange)-1):
			if (abs(yRange[j]) != radius):
				## the conditional is needed here so that we dont try to
				## evaluate the edge of the circle, where our zrange will be
				## empty
				zSpan = math.sqrt(radius**2 - yRange[j]**2)
				## we rearrange the rx = y^2 + z^2 equation to get the +/- z
				## value for a given value of y
				zRange = np.arange(-zSpan, zSpan, intervalSize)
				for k in range(0, len(zRange)-1):
					print "i=%d/%d,\nj=%d/%d,\nk=%d/%d\n\n" % (i, len(xRange), j, len(yRange), k, len(zRange))
					## now we have a point inside the object with position
					## (x, y, z) = (xRange[i], yRange[j], zRange[k])
					## we use this to define a cube with one corner at
					## (xRange[i], yRange[j], zRange[k]), and the others
					## one intervalSize away (ie [j+1], [k+1], etc
					
					## now we average the values at each corner of the cube,
					## applying the trapezoid rule in 3 dimensions to make the
					## cubes contribution to the overall integral better reflect
					## its distribution over the whole object, not just one of
					## its corners
					partA = (f(xRange[i], yRange[j], zRange[k]) + f(xRange[i], yRange[j], zRange[k+1]))/2.0
					## bottom edge on the yRange[j] side
					partB = (f(xRange[i], yRange[j+1], zRange[k]) + f(xRange[i], yRange[j+1], zRange[k+1]))/2.0
					## bottom edge on the yRange[j+1] side
					
					partC = (f(xRange[i+1], yRange[j], zRange[k]) + f(xRange[i+1], yRange[j], zRange[k+1]))/2.0
					## top edge on the yRange[j] side
					partD = (f(xRange[i+1], yRange[j+1], zRange[k]) + f(xRange[i+1], yRange[j+1], zRange[k+1]))/2.0
					
					## top edge on the yRange[j+1] side
					output += ((((partA+partB)/2.0)+((partC+partD)/2.0))/2.0)*(intervalSize**3)	
					## and finally we average the values on the bottom, then
					## top faces, then average both of those, and multiply
					## that little bit of m*r^2 that this cube contains by the
					## volume of the cube, (intervalSize**3)
	return output			

if(__name__ == "__main__"):
	xMax = inputFloat("Input upper bound for x: ")
	
	intervalSize = 0.05
	print "Moment trapezoid integral around x axis: %f" % integralTrapezoid(intervalSize, xMax)	
