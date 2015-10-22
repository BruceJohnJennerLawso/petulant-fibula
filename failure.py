
def getDelta(x, y, sigma):
	delta11 = 0
	delta12 = 0
	delta13 = 0
	delta23 = 0
	delta33 = 0
	for i in range(0, len(sigma)):
		delta11 += (1/(sigma[i]**2))
		delta12 += (x[i]/(sigma[i]**2))
		delta13 += ((x[i]**2)/(sigma[i]**2))	
		delta23 += ((x[i]**3)/(sigma[i]**2))
		delta33 += ((x[i]**4)/(sigma[i]**2))		
		
	delta22 = delta13
	delta31 = delta13	
	delta21 = delta12
	delta32 = delta23
	
	detArray = np.array([[delta11, delta12, delta13],
						 [delta21, delta22, delta23],
						 [delta31, delta32, delta33]])
	print detArray
	return np.linalg.det(detArray)


def getAValue(x, y, sigma):
	delta = getDelta(x, y, sigma)
	
	a11 = 0
	a12 = 0
	a13 = 0
	a21 = 0
	a22 = 0
	a23 = 0
	a31 = 0
	a32 = 0
	a33 = 0
	for i in range(0, len(sigma)):
		a11 += (y[i]/(sigma[i]**2))
		a12 += (x[i]/(sigma[i]**2))		
		a13 += ((x[i]**2)/(sigma[i]**2))	

		a21 += ((y[i]*x[i])/(sigma[i]**2))
		a22 += ((x[i]**2)/(sigma[i]**2))		
		a23 += ((x[i]**3)/(sigma[i]**2))	
		
		a31 += ((y[i]*(x[i]**2))/(sigma[i]**2))
		a32 += ((x[i]**3)/(sigma[i]**2))		
		a33 += ((x[i]**4)/(sigma[i]**2))			

	detArray = np.array([[a11, a12, a13],
						 [a21, a22, a23],
						 [a31, a32, a33]])
	print detArray
	output = np.linalg.det(detArray)
	output /= delta
	return output
	
	
def getBValue(x, y, sigma):
	delta = getDelta(x, y, sigma)
	
	b11 = 0
	b12 = 0
	b13 = 0
	b21 = 0
	b22 = 0
	b23 = 0
	b31 = 0
	b32 = 0
	b33 = 0
	for i in range(0, len(sigma)):
		b11 += (1/(sigma[i]**2))
		b12 += (y[i]/(sigma[i]**2))		
		b13 += ((x[i]**2)/(sigma[i]**2))	

		b21 += ((x[i])/(sigma[i]**2))
		b22 += ((y[i])/(sigma[i]**2))		
		b23 += ((x[i]**3)/(sigma[i]**2))	
		
		b31 += (((x[i]**2))/(sigma[i]**2))
		b32 += ((y[i])/(sigma[i]**2))		
		b33 += ((x[i]**4)/(sigma[i]**2))			

	detArray = np.array([[b11, b12, b13],
						 [b21, b22, b23],
						 [b31, b32, b33]])
	print detArray
	output = np.linalg.det(detArray)
	output /= delta
	return output	
	
def getCValue(x, y, sigma):
	delta = getDelta(x, y, sigma)
	
	c11 = 0
	c12 = 0
	c13 = 0
	c21 = 0
	c22 = 0
	c23 = 0
	c31 = 0
	c32 = 0
	c33 = 0
	for i in range(0, len(sigma)):
		c11 += (1/(sigma[i]**2))
		c12 += ((x[i])/(sigma[i]**2))		
		c13 += ((y[i])/(sigma[i]**2))	

		c21 += ((x[i])/(sigma[i]**2))
		c22 += ((y[i])/(sigma[i]**2))		
		c23 += ((y[i]*x[i])/(sigma[i]**2))	
		
		c31 += (((x[i]**2))/(sigma[i]**2))
		c32 += ((y[i])/(sigma[i]**2))		
		c33 += (((y[i])*(x[i]**2))/(sigma[i]**2))			

	detArray = np.array([[c11, c12, c13],
						 [c21, c22, c23],
						 [c31, c32, c33]])
	print detArray
	return np.linalg.det(detArray)		
