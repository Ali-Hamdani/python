# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:56:20 2019

@author: Tanweer
"""

def Factorial(n):
    if n==1 :
        return 1
    else:
        return (n * Factorial(n-1))


num = int(input("Enter any number "))
Factorial(num)