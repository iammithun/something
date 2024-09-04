# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:23:22 2024

@author: iamrs
"""


student_dict = {
    "students": ["Mithun", "omkar", "jack"],  # Added comma here
    "score": [100, 99, 98]  # Corrected the format
}

#loop through dictionaries 
for key, value in student_dict.items():  # Removed unnecessary parentheses
    print(key)
    print(value)
    

import pandas

pandas.DataFrame(student_dict)
