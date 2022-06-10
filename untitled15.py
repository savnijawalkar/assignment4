# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:17:23 2022

@author: Dell
"""

l=int(input("Enter the year: "))
if l%400 == 0:
    print(l, "is a leap year.")
elif l%4 == 0:
    print(l, "is a leap year.")
else:
    print(l, "is not a leap year.")