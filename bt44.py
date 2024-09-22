# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:02:31 2024

@author: DELL
"""

n=int(input("nhập n:"))
if n>0:
    tong=0
    for i in range(1, n+1):
        tong+= (2*i+1)/(2*i+2)
    print(f"kết quả là: {tong}")
else:
    print("vui lòng nhập lại")
        