from math import pow, exp, factorial
import matplotlib.pyplot as plt


def paskal(a, list):
	"""Paskal distribution, similiar to Geom"""
	ryad = []
	k = 0
	mat = 0
	for element in list:
		p = pow(a, element)/(pow(a+1, element+1))
		ryad.append(p)
	for i in range(len(list)):
		mat += ryad[i]*list[i]
	return ryad
	

def pois(a, list):
	"""Poisson distribution"""
	ryad = []
	k = 0
	mat = 0
	for element in list:
		p = exp(-a)*pow(a,element)/factorial(element)
		ryad.append(p)
	for i in range(len(list)):
		mat += ryad[i]*list[i]
	return ryad


def binom(mean, list):
	"""Binomial distribution"""
	a = mean/len(list)
	ryad = []
	n = len(list)
	mat = 0
	for element in list:
		p = (factorial(n)/(factorial(element)*factorial(n - element)))*pow(a,element)*pow(1-a, n - element)
		ryad.append(p)
	for i in range(len(list)):
		mat += ryad[i]*list[i]

	return ryad	


# def geom(mean, list):
# 	"""Geometric distribution for raw"""
# 	a = 0.458716
# 	ryad = []
# 	for element in list:
# 		p = a * pow(1-a,element)
# 		ryad.append(p)
# 	return ryad	


real = [0.34, 0.35, 0.17, 0.09, 0.04, 0.01]
test = [0,1,2,3,4,6]


print("binom", binom(1.18,test))
print("paskal", paskal(1.18,test))
print('pois', pois(1.18,test))
# print('geyom', geom(1.18,test))



graph1=  plt.plot(test,list(zip(real, pois(1.18, test))))
plt.xlabel("Bin")
plt.ylabel('Frequency')
plt.show()
