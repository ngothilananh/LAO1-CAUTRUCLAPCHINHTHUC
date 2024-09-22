# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:57:25 2024

@author: DELL
"""

n=int(input("nhập n:"))
if n>0:
    tong=0
    for i in range (1,n+1):
        tong += i / (i + 1)
    print(f"kết quả biểu thức là : {tong}")
else:
    print("vui lòng nhập lại số tương ứng")