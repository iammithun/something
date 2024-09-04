# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 07:27:41 2024

@author: iamrs
"""

def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == ""or l_name == "":
        return""
    format_name_f_name = f_name.title()
    format_name_l_name = l_name.title()
  
    return f" {format_name_f_name} {format_name_l_name}"

print(format_name(input("What is your first name?"),
input("What is your last name?")))



