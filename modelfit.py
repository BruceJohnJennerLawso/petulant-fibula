## modelfit.py #################################################################
## fitting a line to a set of data points ######################################
################################################################################
import numpy
import math

import matplotlib.pyplot as plt

def Mean(dataSet):
	output = 0
	for cy in dataSet:
		output += cy
	output /= float(len(dataSet))
	## gotta make sure its a float, otherwise our mean gets rounded like
	## an integer, which we dont want
	return output
	
def isOdd(value):
	if(value%2 != 0):
		return True	
	else:
		return False
	
def Median(dataSet):
	sortedData = sorted(dataSet)
	arrayLen = len(sortedData)
	if(isOdd(arrayLen)):
		## we take the middle value
		return sortedData[ (arrayLen+1)/2 -1 ]
		## not very confident with that, lets see if it works
	else:
		return float(sortedData[ (arrayLen/2) -1 ] + sortedData[ (arrayLen/2) ])/2
		
def Mode(dataSet):
	##sortedData = sorted(dataSet)
	mode = dataSet[0]
	maxHits = 0
	
	for cy in dataSet:
		##print "checking cy=%f, current maxHits is %f" % (cy, maxHits)
		hit = -1
		## negative 1, because we have to find the value itself at least once
		for cycy in dataSet:
			if(cycy == cy):
				hit += 1
		##print "Finished checking the list for hits, %f were found, previous maximum was %f" % (hit, maxHits)
		if(hit >= maxHits):
			mode = cy
			maxHits = hit
	return mode
		

def Variance(dataSet):
	mean = Mean(dataSet)
	
	N = float(len(dataSet))
	output = 0

	for cy in dataSet:
		output += ((cy - mean)**2)
	output /= (N - 1)
	return output
	
def standardDeviation(dataSet):
	variance = Variance(dataSet)
	output = math.sqrt(variance)
	return output

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
	
	a2 = solution[3][0]
	b2 = solution[3][1]
	
	print "\n --Solutions--"
	print "a %f\nb %f" % (solution[3][0], solution[3][1])
	for sol in solution:
		print sol
	## the output  for the solution here also may contain additional possible
	## solutions that we need to address
	
	## but here we just print out our a and b coefficients for the first fit
	## that numpy produces
	xval = range(0,int(max(x)))
	m =[]
	m2 = []
	for cy in range(0,int(max(x))):
		m.append(b*cy + a)
		m2.append(b2*cy + a2)
	plt.plot(x, y, 'r^', xval, m, 'b')
	##ax1.set_xlim(xMin, xMax)
	##plt.set_ylim(0, int(max(y) ) )
	plt.savefig('figure.png')
	

if(__name__ == "__main__"):
	data = numpy.loadtxt("hockeyDataExport.csv", usecols = range(2,17), delimiter = ",", skiprows = 1)
	## load the file with our data
	x, y = data[:,4], data[:,14]
	## 4 is GAA, 2 is AGF, 10 is AWQI, 11 is AGCI
	o = data[:,2]
	for cy in o:
		cy = standardDeviation(o)
	print "x ",x
	print "y ",y
	## create three arrays for the x values, y values, and standard deviations
	## of our data from the file
	getModelCoefficients(x,y, o)

