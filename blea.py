## blea.py #####################################################################
## shitting some code for compphys 236 #########################################
################################################################################
import math
import numpy as np
import matplotlib.pyplot as plt


def factorial(value):
	output = 1
	while(value > 1):
		output *= value
		value -= 1
	return output	


def binomialCoefficient(n, k):
	output = factorial(n)
	output /= (factorial(k)*factorial(n-k))
	return output
	
def binomialDistribution(n, k, p):
	output = binomialCoefficient(n, k)
	output *= p**k
	output *= (1 -p)**(n - k)
	return output
	
def mean(dataset):
	output = 0
	for cy in dataset:
		output += cy
	print len(dataset)
	output /= len(dataset)
	return output	

def customSix(x):
	output = x**(3.0/2.0)
	output /= 2
	output = math.exp(output)
	return output


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


if(__name__=="__main__"):
	##dataset = np.loadtxt("midtestdat.txt")
	##print mean(dataset)
	
	##factValues = []
	##customValues = []
	
	##for i in range(0, 20):
	##	print i, factorial(i), customSix(i)
		
	##	factValues.append(factorial(i))
	##	customValues.append(customSix(i))
		
	##plt.plot(range(0, 20), factValues, "g", customValues, "b--")
	##plt.show()
	
	t1 = np.arange(0.0, 5.0, 0.02)
	t2 = np.arange(0.0, 5.0, 0.02)

	plt.figure(1)
	plt.subplot(211)
	plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("f(t)")

	plt.subplot(212)
	plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("cos(x)")
	plt.show()
	
	
	##import random
	
	##x = []
	##for i in range(0, 30):
	##	x.append(int(random.random()*100))
		
	##print x	
	##np.savetxt("midtestdat.txt", np.c_[x])
	
