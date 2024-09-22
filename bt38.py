# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:19:08 2024

@author: DELL
"""

n=int(input("nhập số lẻ lớn hơn 0:"))
if n>0 and n%2 !=0 :
    tich= 1
    for i in range (1,n+1,2):
        tich= tich*i
    print(f"tích là: {tich}")
else:
    print("vui lòng nhập số lẻ lớn hơn 0")