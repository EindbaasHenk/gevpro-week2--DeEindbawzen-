#!/bin/env python3.4
# country.py

from PyQt4 import QtCore, QtGui

import sys

from random import randrange

class Country(QtGui.QWidget): 
	
	def __init__(self):
		super(Country, self).__init__()
		self.initUI()
	
	# function to get all the data/countries from file	
	def getCountries(self):
		self.countries = {}
		with open('countries_list.txt', 'r') as in_f:
			for line in in_f:
				regels = line.split()
				value = regels[-1]
				self.countries[regels[0]] = value
				
		return sorted(self.countries)
	
		
	def initUI(self):
		
		# set a interface
		self.setGeometry(300,300,600,275)
		self.setWindowTitle("Random Country Flag-Color Generator - De Eindbawzen")
		self.show()	
		
		# get the data/countries inside a list to use in the interface
		countries_list = self.getCountries()
		
		# create a combobox that with all the countries
		self.combobox1 = QtGui.QComboBox(self)
		self.combobox1.setGeometry(10,20,250,30)
		self.combobox1.setStyleSheet('QComboBox { font-size: 11pt; font-family: Calibri; }')
		self.combobox1.show()
		
		# loop all the items in the list and add them to the combobox
		for i in countries_list:
			self.combobox1.addItem(i)
		
		# create 3 seperate Qframes to represent the flag colors
		self.frame1 = QtGui.QFrame(self)
		self.frame1.setGeometry(150,75,300,60)
		self.frame1.show()
		
		self.frame2 = QtGui.QFrame(self)
		self.frame2.setGeometry(150,135,300,60)
		self.frame2.show()
		
		self.frame3 = QtGui.QFrame(self)
		self.frame3.setGeometry(150,195,300,60)
		self.frame3.show()
		
		# create 3 colorobjects to represent the color of each QFrame
		# and give each one of the colorobjects other backgroundcolors
		self.color1 = QtGui.QColor(0,0,0)
		self.color2 = QtGui.QColor(0,100,0)
		self.color3 = QtGui.QColor(0,0,100)
		
		self.frame1.setStyleSheet('QFrame {background-color: %s}'% self.color1.name())
		self.frame2.setStyleSheet('QFrame {background-color: %s}'% self.color2.name())
		self.frame3.setStyleSheet('QFrame {background-color: %s}'% self.color3.name())
		
		# if the selected country in the combobox changes connect 
		# to an update
		self.combobox1.currentIndexChanged.connect(self.updateUI)

	def updateUI(self):
		
		# update colors of each QFrame randomly to get a new 
		# Country Flag
		self.color1.setRed(randrange(0,255))
		self.color1.setGreen(randrange(0,255))
		self.color1.setBlue(randrange(0,255))
		
		self.color2.setRed(randrange(0,255))
		self.color2.setGreen(randrange(0,255))
		self.color2.setBlue(randrange(0,255))
		
		self.color3.setRed(randrange(0,255))
		self.color3.setGreen(randrange(0,255))
		self.color3.setBlue(randrange(0,255))
		
		flag_color1 = self.frame1.setStyleSheet('QFrame {background-color: %s}'% self.color1.name())
		flag_color2 = self.frame2.setStyleSheet('QFrame {background-color: %s}'% self.color2.name())
		flag_color3 = self.frame3.setStyleSheet('QFrame {background-color: %s}'% self.color3.name())
		
def main():
	
	app = QtGui.QApplication(sys.argv)
	ex = Country()
	sys.exit(app.exec_())
	
if __name__== "__main__":
	main()
