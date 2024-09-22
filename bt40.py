# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:31:36 2024

@author: DELL
"""

n=int(input("nhập n:"))
if n>0:
    tong=0
    for i in range (2, n+1,2):
        tong+=1/(2*i)
    print(f"tổng là: {tong}")
else:
    print("vui lòng nhập lại")