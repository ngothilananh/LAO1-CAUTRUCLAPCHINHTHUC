# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:54:15 2024

@author: DELL
"""
n=int(input("nhập số nguyên lớn hơn 0:"))
if n>0:
    tong=0
    for i in range (1,n+1):
        tong+=i
    print(f"tổng là: {tong}")
else:
    print("vui lòng nhập số nguyên dương lớn hơn 0")