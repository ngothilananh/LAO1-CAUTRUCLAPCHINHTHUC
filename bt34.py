# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:35:23 2024

@author: DELL
"""
n=int(input("nhập số nguyên dương:"))
if n<2:
    print("không là số nguyên tố")
for i in range  (2, int(n**(1/2))+1):
    if n% i==0:
        print("không là số nguyên tố")
        break
else:
    print("đây là số nguyên tố")    