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


def inputFloat(prompt):
	while(True):
		i = raw_input(prompt)
		try:
			i = float(i)
			return i
		except ValueError:
			print "\n non float value input, please input a float value"
			continue

		
