# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:42:47 2024

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

students_data_frame=pandas.DataFrame(student_dict)

print(students_data_frame)

#loop through the data frame 

for (index, row) in students_data_frame.interrows():
    print(index)
    print(row)