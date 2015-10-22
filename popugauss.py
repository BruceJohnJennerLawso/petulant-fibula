## popugauss.py ################################################################
################################################################################
import numpy as np
import math

def Mean(dataSet):
	output = 0
	for cy in dataSet:
		output += cy
	output /= float(len(dataSet))
	## gotta make sure its a float, otherwise our mean gets rounded like
	## an integer, which we dont want
	return output

def gaussian(sigma, x, xbar):
	output = 1/(sigma*(math.sqrt(2*math.pi)))
	output *= math.exp(-((x - xbar)**2)/(2*(sigma**2)))
	return output

if(__name__=="__main__"):
	data = np.loadtxt("A4Q1data.txt")
	##x = []
	x = data[:]
	print x
	y = []
	##xbar = Mean(x)
	for cy in x:
		y.append(gaussian(0.3, cy, 1))
		
	##data[:] = y	
	np.savetxt("A4Q1data.txt", np.c_[x, y])
