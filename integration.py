## integration.py ##############################################################
## generic integration on functions ############################################
################################################################################
import math
import numpy as np

def integral(x_min, x_max, intervals, func):
	intervalLen = abs(x_max - x_min)
	intervals = np.arange(x_min, x_max, (intervalLen/intervals))
	output = 0
	print 1, len(intervals)
	for i in range(1, len(intervals)):
		area = func(intervals[i])
		area *= (intervals[i] - intervals[i-1])
		output += area
	return output


if(__name__=="__main__"):
	for cy in range(0, 10):
		print "integral of sin(x) from %f to %f, %d intervals is %f" % (0, math.pi, (10**cy),integral(0, ((math.pi)), (10**cy), math.sin))
