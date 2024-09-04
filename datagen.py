# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:46:12 2023

@author: iamrs
"""

import csv
import random
import time

x_value = 0
CE = 100
PE = 100

fieldnames = ["x_value", "CE", "PE"]


with open("C:\\Learning\\data.csv", 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('C:\\Learning\\data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "CE": CE,
            "PE": PE
        }

        csv_writer.writerow(info)
        print(x_value, CE, PE)

        x_value += 1
        CE = CE + random.randint(-6, 8)
        PE = PE + random.randint(-5, 6)

    time.sleep(1)