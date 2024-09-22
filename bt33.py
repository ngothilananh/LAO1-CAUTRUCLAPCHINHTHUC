# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:23:07 2024

@author: DELL
"""
import math 
n = int(input("Nhập số nguyên dương n: "))
while n<=0:
    print("vui lòng nhập số nguyên dương")
canhain= math.sqrt(n)
if canhain.is_integer():
    print(f"{n} là số chính phương")
else:
    print(f"{n} không là số chính phương")
    
    