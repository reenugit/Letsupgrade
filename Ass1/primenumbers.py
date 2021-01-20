# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:25:03 2021

@author: U35220
"""

first,last = [int(x) for x in input("Enter the range").split()]
print("Prime numbers between ",first," and ",last," is: ")
for each in range(first,last+1):
    count = 0
    if each == 1:
        print(each)
    else:
        for i in range(1,each+1):
            if each%i==0:
                count = count + 1
    if count in range(1,3):
        print(each)
    

        