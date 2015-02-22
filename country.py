#!/bin/env python3.4
# country.py
from PyQt4 import QtCore, QtGui
import sys


class Country():
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "{} {}".format("Hello from", self.name)


def main(argv):
	
	hoi = Country(argv[1])
	print(hoi)
	
if __name__== "__main__":
	main(sys.argv)
