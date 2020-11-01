# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:11:55 2019

@author: Tanweer
"""

car = input("Enter the availability of car.")
bike = input("Enter the availability of bike.")




if car == "True" or car == "Yes":
	print("You can drive")

else:
    if bike == "True" or bike == "Yes":
        print("You can drive")
    else:
        print("You cannot drive")