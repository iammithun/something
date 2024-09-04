# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:24:11 2024

@author: iamrs
"""

target=int(input())
for number in range(1, target+1):
    if number % 3==0 and number % 5==0:
        print("FizzBuzz")
    elif number % 3==0:
        print("Fizz")
    elif number % 5==0:
        print("Buzz")
    else:
        print([number])
        