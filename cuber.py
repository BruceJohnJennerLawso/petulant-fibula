## cuber.py ####################################################################
## check for perfect cube roots ################################################
################################################################################
from input import *
from sys import argv


def raiseToPower(value, n):
	if(n == 0):
		return 1
	elif(n == 1):
		return value
	else:
		output = value
		if(n > 1):
			while(n > 1):
				output *= value
				n -= 1
		else:
			output = 1
			while(n < 0):
				output /= value
				n += 1
	return output

def getCubeRoot(value):
	root = 0
	
	increment = 1
	
	counter = 0
	
	while(True):
		counter += 1
		if(counter >= 80):
			increment = 0
		root += increment
		offset = abs(root*root*root) - abs(value)
		if(abs(increment) <= 0.0000001):
			return root
		else:
			if((offset > 0)and(increment > 0)):
				## our root value was too big, so we go back down, and we try to
				increment = -increment
				increment /= 10.0
			elif((offset < 0)and(increment < 0)):
				## our increment is negative, and we went too far down, so
				## we make our increment even smaller and start going back up
				## again
				increment = - increment
				increment /= 10.0
		#print "%d value %f, root %f, offset %f, increment %f, increment zero? %r" % (counter,value, root,offset, increment, (increment == 0))		

def getNthRoot(value, n):
	root = 0
	
	increment = 1
	
	counter = 0
	
	while(True):
		counter += 1
		if(counter >= 80):
			increment = 0
		root += increment
		offset = abs(raiseToPower(root, n)) - abs(value)
		if(abs(increment) <= 0.0000001):
			return root
		else:
			if((offset > 0)and(increment > 0)):
				## our root value was too big, so we go back down, and we try to
				increment = -increment
				increment /= 10.0
			elif((offset < 0)and(increment < 0)):
				## our increment is negative, and we went too far down, so
				## we make our increment even smaller and start going back up
				## again
				increment = - increment
				increment /= 10.0


def isPerfectCube(value):
	root = 0
	
	while((root**3) < abs(value)):
		root = root + 1
		## keep adding to ans until our value cubed ( ie the root)
		## is equal to or greater than our input
		
		## theres gotta be a better way of doing this than starting at 0
	if((root**3) != abs(value)):
		return False
	else:
		if(value < 0):
			root = -root
		return True

## module tests ################################################################

def testPerfectCubeChecker():
	for cy in range(0,100):
		if(isPerfectCube(float(cy))):
			print "\n%d is a perfect cube" % cy
		else:
			print "%d is not a perfect cube" % cy,

def testRootFinder():
	#print getCubeRoot(1.5)
	#for cy in range(10,21):
	#	print "(%f)^1/3 = %f" % (cy/10.0, getCubeRoot(cy/10.0)) 
	for cy in range(1, 10):
		for y in [2,3,4]:
			print "%dth root of %d is %f" % (y, cy, getNthRoot(float(cy), y))

def testPowerFunction():
	for cy in range(1, 10):
		for y in [-2,-1,0,1,2,3,4]:
			print "%d^%d=%f" % (cy, y,raiseToPower(float(cy), y))

if(__name__ == "__main__"):
	testRootFinder()
	##testPowerFunction()
