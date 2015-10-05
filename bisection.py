## bisection.py ################################################################
## use the bisection method to find a root of a quadratic equation #############
## with form y = cx^2 + bx + c, given inputs x_min and x_max ###################
################################################################################

## utility functions ###########################################################

def printHeading(text):
	print "=="+text+"==\n"
	## just a habit of printing something off at the start to explain
	## what the program is for
	
	## it looks nicer

def inputFloat(prompt):
	while(True):
		i = raw_input(prompt)
		try:
			i = float(i)
			return i
		except ValueError:
			print "\n non float value input, please input a float value"
			continue

def maxOf(value1, value2):
	if(value1 >= value2):
		return value1
	else:
		return value2
		
def minOf(value1, value2):
	if(value1 <= value2):
		return value1
	else:
		return value2	

def isZero(value, tolerance):
	if(abs(value) <= tolerance):
		## made a bit easier, since abs of any value is also how far it is
		## from 0
		return True
	return False

def oppositeSigns(value1, value2):
	if((value1 == 0)or(value2 == 0)):
		return False
	else:
		if(value1 < 0):
			if(value2 > 0):
				return True
			else:
				return False
		else:
			## value1 was positive
			if(value2 < 0):
				return True
			else:
				return False

################################################################################

def quadratic(c, b, a, x):
	y = ( (c*x**2) + (b*x) + a )
	return y

def getQuadraticRoot(c, b, a, x_min, x_max):
	count = 0
	## never a bad idea for testing to keep track of times through the
	## loop
	xLow = x_min
	xHigh = x_max
	## the lowest and highest bounds of the x interval that we are
	## searching
	while(True):
		xMid = xLow + (xHigh-xLow)/2.0
		## the halfway point through our x interval
		mid = quadratic(c, b, a, xMid)
		if(isZero(mid, 0.0001)):
			return xMid
		low = quadratic(c, b, a, xLow)
		high = quadratic(c, b, a, xHigh)
		if(isZero(low, 0.0001)):
			return xLow
		elif(isZero(high, 0.0001)):
			return xHigh
		## we went through the values at the start, midpoint, and end of our
		## ranges and found no values that were close enough to zero, so we need
		## to keep tightening our range until we get close enough
		if(oppositeSigns(mid, low)):
			## low happens to have the luck of the draw here, so y = x^2 -1 is
			## going to consistently gravitate towards the x = -1 root first
			xHigh = xMid
		elif(oppositeSigns(mid, high)):
			xLow = xMid
		else:
			if(isZero((xHigh-xLow), 0.00001)):
				raise ValueError('hasRoot check failed, x range has no roots')
			higher = high - mid
			lower = low - mid
			if(lower >= higher):
				xLow = xMid
			else:
				xHigh = xMid				
			
			
			
			##raise ValueError('hasRoot check failed, x range has no roots')
			## this shouldnt happen, but sometimes shit happens anyways
		
		
if(__name__ == "__main__"):
	printHeading("Bisection Method Root Finder")
	
	print "cx^2 + bx + c = 0 for x between x_min and x_max\n"
	c = inputFloat("Input value for c: ")
	b = inputFloat("Input value for b: ")
	a = inputFloat("Input value for a: ")
	x_min = inputFloat("Input value for x_min: ")
	x_max = inputFloat("Input value for x_max: ")
	
	x_min = minOf(x_min, x_max)
	x_max = maxOf(x_min, x_max)
	## just so there isnt any funny business happening with the order of our
	## x bounds
	try:
		root = getQuadraticRoot(c, b, a, x_min, x_max)
		print "\n\ny = %fx^2 + %fx + %f has a root at x = %f\non the range x=%f to x=%f" % \
			(c, b, a, root, x_min, x_max)
	except ValueError:
		print "\n\ny = %fx^2 + %fx + %f has no roots on the range x=%f to x=%f" % \
			(c, b, a, x_min, x_max)

