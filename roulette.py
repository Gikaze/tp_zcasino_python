# -*-coding:Latin-1 -*
import os
from random import randint

def getRouletteNumber():
	min = 0
	max = 49
	return randint(min, max)
	 
def getRouletteColor(number):

	if number % 2 == 0:
		colorR = True
	else:
		colorR = False
		
	return colorR
