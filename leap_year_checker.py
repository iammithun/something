# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:15:12 2024

@author: iamrs
"""

year=int(input("type the year"))

if year % 4==0:
  if year % 100==0:
    if year % 400==0:
       print("Leap year.")
    else:
       print("Not leap year.")
  else:
       print("Leap year.")
else:
    print("Not leap year.")
      