# -*- coding: utf-8 -*-
"""
Created on Tue OCT 11 22:54:19 2021

@author: pankaj
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('E:\skilledge\PYTHON/stud_reg_2.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('E:\skilledge\PYTHON/stud_reg_2.csv)

# Reading Excel Files with Pandas
df1 = pandas.read_excel('E:\skilledge\PYTHON/stud_reg_2.xlsx')

df1 = pandas.read_excel('stud_reg_2.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('stud_reg_2.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)