## doyouseethelight.py #########################################################
## the band elwood, the band ###################################################
################################################################################
import numpy as np
import matplotlib.pyplot as plt

def inputFloat(prompt):
	while(True):
		i = raw_input(prompt)
		try:
			i = float(i)
			return i
		except ValueError:
			print "\n non float value input, please input a float value"
			continue

class lens:
	def __init__(self, xPos, yPos, radius, fValue):
		self.x = xPos
		self.position = yPos
		self.radius = radius
		self.f = fValue



class rayState:
	def __init__(self, yi, xi, alphai):
		self.y = yi
		## height above the x axis of our light ray
		self.alpha = alphai
		## angle above the vertical, looking rightwards
		## must be in radians
		self.x = xi
		
	def translateForward(dx, *translations):
		## translations here is an arbitrary number of numpy 2x2 matrices that
		## we apply to the rayState to model its state moving forward through
		## either open space or a lens
		thisState = np.matrix([[self.y], [self.alpha]])
		for transl in translations:
			## the order seemed to be kind of important here with T1, L, T2, yi
			## hopefully I dont get burned on that
			thisState = np.dot(transl, thisState)
		self.y = float(thisState[0])
		self.alpha = float(thisState[1])
		self.x += dx
		 
class rayPath:
	def __init__(self, yi, xi, alphai, blocked):
		self.Points = []
		self.Points.append(rayState(yi, xi, alphai))
		self.Blocked = blocked
		## whether or not we missed one of the lenses
		## I really wish I could do this differently so that it only becomes
		## dashed after it hits a wall, but time is short
		
	def addNewPoint(self, y, x, alpha):
		self.Points.append(rayState(yi, xi, alpha))
		
	def getXRange(self):
		output = []
		for pt in self.Points:
			output.append(pt.x)
		return output

	def getYRange(self):
		output = []
		for pt in self.Points:
			output.append(pt.y)
		return output


def lensMatrix(f):
	output = np.matrix([[1, 0],[float(-1.0/f), 1]])
	return output
	
def distanceMatrix(d):
	output = np.matrix([[1.0, d],[0.0, 1.0]])
	return output

def yForward(initial, d1, f, d2):
	initial.translateForward(float(d1 + d2), distanceMatrix(d1), lensMatrix(f), distanceMatrix(d2))
	return initial
	## this function might not actually be needed cause it should stop after
	## each transformation so we can plot it?

def plotRaypaths(xMax, xPlotMax, lens1, lens2, lens3):
	
	rayPaths = []
	
	alphaSpread = np.arange(-0.05, 0.10, 0.05)
	for alpha in alphaSpread:
		ySpread = np.arange(-1.0, 1.0, 0.2)
		for y in ySpread:
			rayPaths.append(getRayPath(xMax, lens1, lens2, lens3, y, alpha)
	for path in rayPaths:
		if(path.Blocked == True):
			style = "b--"
		else:
			style = "b"
		plt.plot(path.getXRange(), path.getYRange(), style)
	plt.savefig("image.png")	
	
				
	

def getRayPath(xMax, lens1, lens2, lens3, yi, alphai):
	## we can just assume that x = 0 here, no need to pass another variable
	ray = rayState(yi, 0.0, alphai)
	path = rayPath(yi, 0.0, alphai, False)
	
	d = lens1.x
	ray.translateForward((d), distanceMatrix(d))
	path.addNewPoint(ray.y, ray.x, ray.alpha)
	if(abs(ray- lens1.position) > lens1.radius):
		##missed the first lens
		path.Blocked = True
		return path
	ray.translateForward(0.0, lensMatrix(lens1.f), lensMatrix(lens2.f))
	d = lens3.x - lens1.x
	ray.translateForward((d), distanceMatrix(d))
	path.addNewPoint(ray.y, ray.x, ray.alpha)
	if(abs(ray- lens1.position) > lens1.radius):
		##missed the first lens
		path.Blocked = True
		return path
	ray.translateForward(0.0, lensMatrix(lens3.f))		
	d = xMax - lens3.x
	ray.translateForward((d), distanceMatrix(d))
	path.addNewPoint(ray.y, ray.x, ray.alpha)
	return path

if(__name__ == "__main__"):
	
	xMax = inputFloat("Input maximum x value to simulate to: ")
	xPlotMax = inputFloat("Input maximum x value for plot: ")
	
	lensx12 = inputFloat("Input x position of lenses 1 and 2: ")
	lensy12 = inputFloat("Input y position of center of lenses 1 and 2")
	lensr12 = inputFloat("Input radius of lenses 1 and 2")
	lensf1 = inputFloat("Input focal length for lens 1")
	lensf2 = inputFloat("Input focal length for lens 2")
	
	lensx3 = inputFloat("Input x position of lens 3: ")
	lensy3 = inputFloat("Input y position of center of lens 3: ")
	lensr3 = inputFloat("Input radius of lens 3")
	lensf3 = inputFloat("Input focal length for lens 3")
	
	lens1 = lens(lensx12, lensy12, lensr12, lensf1)
	lens2 = lens(lensx12, lensy12, lensr12, lensf1)
	lens3 = lens(lensx3, lensy3, lensr3, lensf3)
	
	plotRaypaths(xMax, xPlotMax, lens1, lens2, lens3)
	


