# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:44:16 2024

@author: DELL
"""

n=int(input("nhập n:"))
if n>0:
    tong=0
    for i in range (1,n+1):
        tong += 1 / (2*i - 1)
    print(f"tổng là: {tong}")
else:
    print("vui lòng nhập lại")    
    