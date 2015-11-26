## rungekutta.py ###############################################################
## solve a pde using RK4 and graph solution ####################################
################################################################################
import math
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




def xDerivative(x, y, z, sigma, b, r):
	output = sigma*(y - x)
	return output

def yDerivative(x, y, z, sigma, b, r):
	output = r*x - y - x*z
	return output

def zDerivative(x, y, z, sigma, b, r):
	output = x*y - b*z
	return output
	

	
	
def solve(sigma, b, r, tf, h):
	tRange = [0.0]
	## initially, we only have the start time, but we will attach the start time
	## for each frame. We need this so that we can graph the quantities with
	## respect to time later
	t = 0
	## current simulation time
	
	
	x = [0]
	y = [1]
	z = [0]
	## set our initial conditions
	
	## our x, y, z here are lists, so that we have the sequential values of x,
	## y and z, which are calculated at each frame.
	i = 0
	## set our index to 0, so that we start off referencing the first element fo
	
	while(t < tf):
		tRange.append(t)
		## attach whatever the current time is
		
		## we start by calculating our coefficients, hopefully in the correct
		## order
		
		k0 = h*xDerivative(x[i], y[i], z[i], sigma, b, r)
		l0 = h*yDerivative(x[i], y[i], z[i], sigma, b, r)
		m0 = h*zDerivative(x[i], y[i], z[i], sigma, b, r)
		
		k1 = h*xDerivative((x[i] + 0.5*k0), (y[i] + 0.5*l0), (z[i] + 0.5*m0), sigma, b, r)
		l1 = h*yDerivative((x[i] + 0.5*k0), (y[i] + 0.5*l0), (z[i] + 0.5*m0), sigma, b, r)
		m1 = h*zDerivative((x[i] + 0.5*k0), (y[i] + 0.5*l0), (z[i] + 0.5*m0), sigma, b, r)		
		
		k2 = h*xDerivative((x[i] + 0.5*k1), (y[i] + 0.5*l1), (z[i] + 0.5*m1), sigma, b, r)
		l2 = h*yDerivative((x[i] + 0.5*k1), (y[i] + 0.5*l1), (z[i] + 0.5*m1), sigma, b, r)
		m2 = h*zDerivative((x[i] + 0.5*k1), (y[i] + 0.5*l1), (z[i] + 0.5*m1), sigma, b, r)	

		k3 = h*xDerivative(x[i] + k2, y[i] + l2, z[i] + m2, sigma, b, r)
		l3 = h*yDerivative(x[i] + k2, y[i] + l2, z[i] + m2, sigma, b, r)
		m3 = h*zDerivative(x[i] + k2, y[i] + l2, z[i] + m2, sigma, b, r)
		
		x.append(x[i] + ((1/6.0)*(k0 + 2*k1 + 2*k2 + k3)))
		y.append(y[i] + ((1/6.0)*(l0 + 2*l1 + 2*l2 + l3)))
		z.append(z[i] + ((1/6.0)*(m0 + 2*m1 + 2*m2 + m3)))
		## we append the values for x_{i+1}, y_{i+1}, z_{i+1} to each list so
		## that we have a value showing us what each of x, y, and z were for
		## each step that we ran. At the end of this, i value will be the
		## number of steps that were run 		
		
		i += 1
		t += h
		## move the current time one step forward
	plt.plot(tRange, y, label='y vs t')
	plt.plot( x,z, label='z vs x')
	plt.legend()
	plt.xlabel("t or x")
	plt.ylabel("y or z")
	## plotting 4 axes on the same plot is impossible to label clearly,
	## but hopefully this helps it make more sense
	titleText = "Solution for sigma = %f, b = %f, r = %f" % (sigma, b, r)
	plt.title(titleText)
	plt.savefig('figure1.png')

if(__name__ == "__main__"):
	
	sigma = inputFloat("Please input sigma value: ")
	b = inputFloat("Please input b value: ")
	r = inputFloat("Please input r value: ")
	##tf = inputFloat("Please input time to run")
	tf = 50.0
	solve(sigma, b, r, tf, 0.1)
	## no step size was specified, so I went with 0.1 as a reasonable choice?
