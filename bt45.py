# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:15:08 2024

@author: DELL
"""
#k*(k+1)/2
n=int(input("nhập số nguyên n:"))
x=int(input("nhập x:"))
if n>0:
    tong=0
    for i in range (1, n+1):
        mauso=i*(i+1)//2
        tuso= x**i/mauso
        tong+= tuso
    print(f"kết quả phép tính:{tong} ")
else:
    print("vui lòng nhập số hợp lệ")
        
        