###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
#Good Luck

import random

class Plane():
	def __init__(self):
		self.optimal = 0.0
		self.prev_orientation = 0.0
		self.orientation = 0.0

	def new_orientation(self, orientation):
		self.prev_oreintation = self.orientation
		self.orientation = orientation


	def correct_orientation(self):
		diff = self.prev_oreintation - self.orientation
		self.orientation = 0.01*diff

	def print_orientation(self):
		print("Current orientation is: {} degrees.".format(self.orientation))


if __name__ == "__main__":
	plane = Plane()
	plane.print_orientation()

	while True:
		#every step orientation changes because of the turbulences
		plane.new_orientation(random.gauss(0, 30))
		plane.correct_orientation()
		plane.print_orientation()
	

