## modelfit.py #################################################################
## fitting a line to a set of data points ######################################
################################################################################
import numpy
import math

import matplotlib.pyplot as plt

def getModelCoefficients(x, y, o):
	
	## we are going to sum up the data provided in the form shown in the notes
	## the variables t, u, v, q, r, and s will represent our coefficients
	
	## t -au - bv = 0
	## q - ar - bs = 0
	
	t, u, v, q, r, s = 0, 0, 0, 0, 0, 0
	
	for cy in range(1, len(o)):
		t += (x[cy]*y[cy])/(o[cy]**2)
		v += (x[cy]**2)/(o[cy]**2)
		u += 1/(o[cy]**2)

		q += (y[cy])/(o[cy]**2)
		s += (x[cy])/(o[cy]**2)
		r += 1/(o[cy]**2)
	
	## print out the system of equations that our summation produced
	print "%f - a*%f - b*%f = 0" % (t, u, v)
	print "%f - a*%f - b*%f = 0" % (q, r, s)
	## note that we move the a and b terms over to the right hand side before
	## solving to make things a bit easier
	
	
	linearSystem = numpy.array([
		[u, v],
		[r, s]])
	equals = numpy.array([t,q])
	solution = numpy.linalg.lstsq(linearSystem, equals)
	
	a = solution[0][0]
	b = solution[0][1]
	
	print "\n --Solutions--"
	print "a %f\nb %f" % (solution[0][0], solution[0][1])
	## the output  for the solution here also may contain additional possible
	## solutions that we need to address
	
	## but here we just print out our a and b coefficients for the first fit
	## that numpy produces
	xval = range(0,int(max(x)))
	m =[]
	for cy in range(0,int(max(x))):
		m.append(b*cy + a)
	plt.plot(x, y, 'r^', xval, m, 'b--')
	plt.savefig('figure.png')
	

if(__name__ == "__main__"):
	data = numpy.loadtxt("A3Q1data.txt")
	## load the file with our data
	x, y, o = data[:,0], data[:,1], data[:,2]
	## create three arrays for the x values, y values, and standard deviations
	## of our data from the file
	getModelCoefficients(x,y, o)

