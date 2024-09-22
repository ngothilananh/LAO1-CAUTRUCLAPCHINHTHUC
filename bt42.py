# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:53:15 2024

@author: DELL
"""

n=int(input("nhập số nguyên dương:"))
if n>0:
    bieuthuc=0
    for i in range (1,n+1):
        bieuthuc= bieuthuc+ 1/(i*(i+1))
    print(f"giá trị của biểu thức là: {bieuthuc}")
else:
    print("vui lòng nhập số hợp lệ")
        