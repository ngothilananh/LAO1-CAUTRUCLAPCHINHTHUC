# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:57:36 2024

@author: DELL
"""


a=int(input("nhập cạnh a:"))
b=int(input("nhập cạnh b:"))
c=int(input("nhập cạnh c:"))
while a+b<=c and b+c<=a and a+c<b:
    print("Vui lòng nhập lại")
    a=int(input("nhập cạnh a:"))
    b=int(input("nhập cạnh b:"))
    c=int(input("nhập cạnh c:"))
if a==b==c:
    print("tam giác đều")
elif a==b or a==c or b==c:
    print("tam giác cân")
elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2== a**2+b**2:
    print("tam giác cân")
else:
    print("tam giác thường")
    
    