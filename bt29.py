# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:47:21 2024

@author: DELL
"""

n=int(input("nhập số N (vd:6789) : "))
tong=0
while n>0:
    tong+= n%10
    n= n//10
print(f"tổng các chữ số :{tong}")
    