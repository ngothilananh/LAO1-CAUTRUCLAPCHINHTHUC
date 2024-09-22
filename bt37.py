# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:10:12 2024

@author: DELL
"""

n=int(input("nhập số nguyên dương chẵn lớn hơn 0:"))
if n>0 and n%2==0:
    tong=0
    for i in range (2,n+1,2):
        tong= tong+i
    print(f"tổng là: {tong}")
else:
    print("vui lòng nhập số nguyên dương chẵn lớn hơn 0")
        