# -*- coding: utf-8 -*-
a= """
Created on Sat Jun 17 11:11:42 2023

@author: mithun sai
"""
print(a)
x = "mithun"
print(type(x))
print(x)
x = 10
print(type(x))
print(x)

print(float(x))
print(str(x)+str(x))
print(x+x)
list1 = ["A","B","C"]
print(list1)

b = "Hello, World!"
print(b[2:5])
print(b[5:])
print(b[-5:-2])
a = "Hello, World!"
print(a.upper())
v = "HELLO WORLD"
print(v.lower())
a = " Hello, World! "

print(a.strip())

a = "Hello, World!"
print(a.replace("Hello", "Horse"))
print(a.split(","))
aa = a.split(",")
print(aa[1])

age = 36
txt = "My name is John, I am " + str(age)
print(txt)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "hello, and welcome to my world."

x = txt.count("e")

print (x)