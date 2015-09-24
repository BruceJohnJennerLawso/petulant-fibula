## altitude.py #################################################################
## input a value of T and print the correct altitude in meters #################
################################################################################
import math

def inputInteger(prompt):
	while(True):
		i = raw_input(prompt)
		try:
			i = int(i)
			return i
		except ValueError:
			print "\n non integer value input, please input an integer value"
			continue
			

def getAltitudeForPeriod(period, G, planetMass, planetRadius):
	output = (G*planetMass)*(period**2)
	output /= (4*(math.pi**2))
	output = output**(1/3.0)
	output -= planetRadius
	
	return output

if(__name__ == "__main__"):
	period = inputInteger("Please input a period in seconds: ")
	print getAltitudeForPeriod(period, 6.67e-11, 5.97e24, 6371000)
