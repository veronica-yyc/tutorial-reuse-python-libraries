import math
import numpy as np

def calculate_frictionfactor(Re : float, e_over_d : float) -> float:
	ff = -1.8*math.log10(6.9/Re + math.pow(e_over_d/3.7, 1.11))
	
	return 1/ff * 1/ff

def calculate_frictionfactorcurve(e_over_d: float) -> list[float]:
	x = []
	y = []
	for Re in np.logspace(4,8):
		x.append(Re)
		y.append(calculate_frictionfactor(Re, e_over_d))
	return [np.array(x),np.array(y)]
