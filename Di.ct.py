# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:56:42 2024

@author: iamrs
"""

import pandas as pd  # Import pandas with alias pd

student_dict = {
    "students": ["Mithun", "Omkar", "Jack"],  # Corrected the student name "omkar" to "Omkar"
    "score": [100, 99, 98]
}

students_data_frame = pd.DataFrame(student_dict)  # Use pd.DataFrame() instead of pandas.DataFrame()

print(students_data_frame)

# Loop through the DataFrame
for index, row in students_data_frame.iterrows():  # Corrected the method name to iterrows()
    if row['students'] == "Mithun":  # Access student name using row['students']
        print(row['score'])  # Access score using row['score']
