## stat.py #####################################################################
## core shitty statistics module ###############################################
################################################################################

## calls for the 3 basic properties of datasets ################################
################################################################################

def Mean(dataSet):
	output = 0
	for cy in dataSet:
		output += cy
	output /= len(dataSet)
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
		
		
## random value generators for convenience #####################################
################################################################################		
		
def randomValue(floor, ceiling):
	value = floor + (random.random()*(ceiling - floor))
	return value		
		
def randomIntegerValue(floor, ceiling):
	return int(randomValue(floor, ceiling+1))




## module tests ################################################################
################################################################################


def testListFunctions():
	testArray = []
	for i in range(6):
		randam = randomIntegerValue(0,10)
		testArray.append(randam)
	print testArray, sorted(testArray)
	
	print "Array Mean = %f,\nArray Median = %f,\nArray Mode %d" % (Mean(testArray), Median(testArray), Mode(testArray))


if(__name__ == "__main__"):
	
	import random
	testListFunctions()







