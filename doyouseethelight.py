## doyouseethelight.py #########################################################
## the band elwood, the band ###################################################
################################################################################
import numpy as np
import matplotlib.pyplot as plt


class rayState:
	def __init__(self, yi, alphai):
		self.y = yi
		## height above the x axis of our light ray
		self.alpha = alphai
		## angle above the vertical, looking rightwards
		## must be in radians
		
	def translateForward(*translations):
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
		 

def lensMatrix(f):
	output = np.matrix([[1, 0],[float(-1.0/f), 1]])
	return output
	
def distanceMatrix(d):
	output = np.matrix([[1.0, d],[0.0, 1.0]])
	return output

def yForward(initial, d1, f, d2):
	initial.translateForward(distanceMatrix(d1), lensMatrix(f), distanceMatrix(d2))
	return initial
	## this function might not actually be needed cause it should stop after
	## each transformation so we can plot it?

if(__name__ == "__main__"):
	



