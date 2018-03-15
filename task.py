###Flight simulator. 
# Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth).
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
# Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations").
# With every simulation step the orentation should be corrected, applied and printed out.
# The level of realism in simulation is of your choice, but more sophisticated solutions are better.
# If you can thing of any other features, you can add them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
#
# When you are done upload this code to your github repository.
# The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
# Good Luck

from random import gauss
from time import sleep
import multiprocessing


class Plane:
    def __init__(self):
        self.optimal = 0.0
        self.prev_orientation = 0.0
        self.orientation = 0.0
        self.max_angle = 270

    def new_orientation(self, orientation):
        self.prev_orientation = self.orientation
        self.orientation = orientation
        self.did_crash()

    def correct_orientation(self):
        diff = self.prev_orientation - self.orientation
        self.orientation = 0.01 * diff

    def current_orientation(self):
        return "Current orientation is: {} degrees.".format(self.orientation)

    def did_crash(self):
        if abs(self.orientation) > 270:
            print("Plane crashed.")
            exit()

    def fly(self):
        while True:
            self.new_orientation(gauss(0, 30))
            self.correct_orientation()
            yield plane.current_orientation()


class Simulation:
    @staticmethod
    def run():
        print("Plane is taking off.")
        for orientation in plane.fly():
            print(orientation)
            sleep(0.5)


class Manager:
    def __init__(self):
        self.simulation = multiprocessing.Process(name='simulation', target=Simulation.run)

    def start(self):
        while True:
            user_input = input("**** FLIGHT SIMULATOR ****\nPress r to run\n"
                               "Press q to quit(anytime)\n**************************\n")
            if user_input is 'r':
                self.simulation.start()
                break
            elif user_input is 'q':
                exit()

    def wait_for_user_input(self):
        while True:
            user_input = input()
            if user_input is 'q':
                print("**** Simulation terminated by user. ****")
                self.simulation.terminate()
                exit()


if __name__ == "__main__":
    plane = Plane()
    manager = Manager()
    manager.start()
    manager.wait_for_user_input()
