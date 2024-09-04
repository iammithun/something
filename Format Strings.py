# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 13:59:54 2023

@author: mithun sai 
"""
#This code about Format Strings in python
#This code by mithun sai

#Strings Format 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

