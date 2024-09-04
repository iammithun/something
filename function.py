# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:09:15 2024

@author: iamrs
"""

def prime_checker(number):
    is_prime=Ture
    for i in range(2, number):
      if number % i==0:
        is_prime=Flase
    
n=int(input())
prime_checker(nummber=n)