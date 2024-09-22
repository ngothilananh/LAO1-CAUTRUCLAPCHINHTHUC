# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:31:03 2024

@author: DELL
"""
n=-1
while n<=0:
    n=int(input("nhập số nguyên:"))
    if n<=0:
        print("nhập số nguyên dương")
print("ước các số là:")
for i in range(1, n+1):
    if n%i ==0:
        print(i)
    