# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:54:49 2021

@author: U35220
"""

num = int(input("Enter the number"))
fact = 1
if num == 1:
    fact = 1
else:
    for i in range(2,num+1):
        fact = fact * i
print(" Factorial of",num,"is :",fact)