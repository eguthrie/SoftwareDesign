from math import sqrt
from math import factorial

def estimate_pi():
	""" Estimates pi until 10e-15 term
	returns float of pi"""
	coef=2*sqrt(2)/9801
	pi=0
	k=0
	sumwhole=0
	sumpart=factorial(4*k)*(1103+26390*k)/(factorial(k)**4*396**(4*k))
	while sumpart>=10**(-15):
		k=k+1
		sumwhole=sumwhole+sumpart
		pi=1/(coef*sumwhole)
		sumpart=factorial(4*k)*(1103+26390*k)/(factorial(k)**4*396**(4*k))
	return pi
print estimate_pi()
