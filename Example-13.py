# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:57:39 2020

@author: Tanweer
"""

def g(x):
    def h():
        x= 'abc'
        print(x)
    x = x + 1
    
    print('g: x=',x)
    h()
    #return x

x = 3
z = g(x) 


#def h():
#    x= 'abc'
#    return x
#
#h()