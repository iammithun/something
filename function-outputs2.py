# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 07:05:54 2024

@author: iamrs
"""

def format_name(f_name, l_name):
    format_name_f_name = f_name.title()
    format_name_l_name = l_name.title()
  
    return f"Result: {format_name_f_name} {format_name_l_name}"

print(format_name(input("What is your first name?"),
input("What is your last name?")))


def format_name(f_name, l_name):
    if f_name == ""or l_name == "":
        return""
    format_name_f_name = f_name.title()
    format_name_l_name = l_name.title()
  
    return f" {format_name_f_name} {format_name_l_name}"

print(format_name(input("What is your first name?"),
input("What is your last name?")))



