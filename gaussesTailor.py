## gaussesTailor.py ############################################################
## input a 1d data stream and fit a single gaussian ############################
## to the data #################################################################
################################################################################
import numpy as np
import matplotlib.pyplot as plt
import math

def inputFloat(prompt):
	while(True):
		i = raw_input(prompt)
		try:
			i = float(i)
			return i
		except ValueError:
			print "\n non float value input, please input a float value"
			continue

def chiSquare(x, xg, sigma):
	output = 0
	for i in range(0, len(x)):
		outputi = ((x[i] - xg)**2)
		outputi /= (2*(sigma**2))
		output += outputi
	return output
	## the part of the gaussian inside the exponential that we want to minimize

def gaussian(sigma, x, xbar, A):
	output = 1/(sigma*(math.sqrt(2*math.pi)))
	output *= math.exp(-((x - xbar)**2)/(2*(sigma**2)))
	output *= A
	return output
	## the gaussian function itself, scaled up by some factor A

def findGaussian(xValues, yValues, sigmaValues, xMin, xMax, width, heightPeak, xPeak):
	
	
	
	print "\n\n\nxMin %f, xMax %f, width %f, heightPeak %f, xPeak %f" % (xMin, xMax, width, heightPeak, xPeak)
	## just lets me know what the values that gnh gave us are
	
	x_min = xMin
	x_max = xMax
	x_mid = -1
	## we set our boundaries before we start applying bisection to find a minimum
	## value of chi-squared for a given value of xPeak (the center of the gaussian)
	counter = 0
	## ticker that we will use to keep track of how many times the loop has run
	print "Finding optimal xPeak values between %f and %f" % (x_min, x_max)
	while(True):
		counter += 1
		x_mid = (x_min + (x_max-x_min)/2.0)
		
		atMin = chiSquare(xValues, x_min, width)
		atMax = chiSquare(xValues, x_max, width)
		atMid = chiSquare(xValues, x_mid, width)
		print "Loop %d\nxMin %f atMin %f\nxMid %f atMid %f\nxMax %f atMax %f" % (counter, x_min, atMin, x_mid, atMid, x_max, atMax)
		if(atMax < atMin):
			x_min = x_mid
		else:
			if((abs(atMid-atMax) < 0.001)or(abs(atMid - atMin) < 0.001)):
				break
			x_max = x_mid
		if(counter > 4):
			break
	## we found a best value for xPeak at x_mid
	xPeak = x_mid
	

	
	sigma_min = 0.00001
	sigma_max = width + ((xMin + xMax))
	## now we apply bisection again, but this time on a range of possible values
	## for sigma (width)
	
	## our range is from tiny and close to 0, up to some large value of sigma
	## which in this case we set as being roughly bigger than our x range
	## (sigma probably smaller than our x range?)
	
	print "Finding optimal width (sigma) values between %f and %f" % (sigma_min, sigma_max)
	counter = 0
	while(True):
		counter += 1
		sigma_mid = (sigma_min + sigma_max)/2.0
		
		atMin = chiSquare(xValues, xPeak, sigma_min)
		atMax = chiSquare(xValues, xPeak, sigma_max)
		atMid = chiSquare(xValues, xPeak, sigma_mid)			
		print "Loop %d\nsigmaMin %f atMin %f\nsigmaMid %f atMid %f\nsigmaMax %f atMax %f" % (counter, sigma_min, atMin, sigma_mid, atMid, sigma_max, atMax)
		if(atMax < atMin):
			sigma_min = sigma_mid
		else:
			if((abs(atMid-atMax) < 0.001)or(abs(atMid - atMin) < 0.001)):
				break
			sigma_max = sigma_mid		
		
	width = sigma_mid		
	## we found a best value for width
	
	
	closestX = xMax
	for i in range(0, len(yValues)):
		if(abs(xPeak - xValues[i]) < abs(xPeak -closestX)):
			closestX = xValues[i]
			heightPeak = yValues[i]
	print "heightPeak %f" %heightPeak	
	## runs through the x range, finds the x value closest to our peak value
	## found earlier, then set the y value associated with that x value as our
	## height peak
	
	## it really should be something more like averaging values closest to xPeak
	## but this is simplest	
	
	xPeakError = xPeak
	while(True):
		xPeakError += (0.1*xPeak)
		if(abs(chiSquare(xValues, xPeakError, width)) < (chiSquare(xValues, xPeak, width) + 1)):	
			break
	xPeakError = xPeakError - xPeak
	## set our xPeakError (error on xPeak) by incrementing a value of Xpeak up
	## until it is a full 1 away from our minimum chi square. Once we get there,
	## we find the difference in xPeak from our best fit xPeak, and use that as
	## the error
	
	widthError = width
	while(True):
		widthError += (0.1*width)
		if(abs(chiSquare(xValues, xPeak, widthError)) < (chiSquare(xValues, xPeak, width) + 1)):	
			break	
	widthError = widthError - width
	## same idea as with the xPeakError, just applied to the sigma/width value
	
	gaussianMax = gaussian(width, xPeak, xPeak, 1)
	scaleFactor = heightPeak/gaussianMax
	## our gaussians biggest value is too small to match the actual data, so we
	## create a scaling factor to multiply all values by so the peak of our
	## calculated gaussian matches the one we found in the data
	## (ie y at x peak)
	
	
	fig, (ax1) = plt.subplots(1)

	ax1.set_xlabel("x")
	ax1.set_ylabel("y")
	
	ax1.errorbar(xValues, yValues, yerr=sigmaValues,fmt='g^')
	x = np.arange(xMin, xMax, 1)
	y = []
	for cy in x:
		y.append(gaussian(width, cy, xPeak, scaleFactor))
	## generates a list of y values to represent the gaussian function with our
	## parameters, so we can graph the gaussian that we found in pyplot along
	## with the original data
	print "Width %f +/- %f, xPeak %f +/- %f" % (width, widthError, xPeak, xPeakError)
	ax1.plot(x, y, "c")
	plt.savefig('figure.png')
	
if(__name__ == "__main__"):
	data = np.loadtxt("A4Q1data.txt")
	x, y, = data[:,0], data[:,1]
	## load our x and y values from file
	sigma = []
	for cy in x:
		sigma.append(0.3)
		## create our sigma values for the error with a set value of 0.3
	xPeak = inputFloat("Please input x peak: ")
	heightPeak = inputFloat("Please input height peak: ")
	width = inputFloat("Please input width: ")
	xMin = inputFloat("Please input x Min: ")
	xMax = inputFloat("Please input x Max: ")
	## user input of our search interval, width of the gaussian, x value for the
	## peak, and the height peak (peak in y)
	
	findGaussian(x, y, sigma, xMin, xMax, width, heightPeak, xPeak)
		
