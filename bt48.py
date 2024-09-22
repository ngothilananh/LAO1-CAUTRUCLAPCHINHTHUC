# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:57:54 2024

@author: DELL
"""

tongnhonhat=1000
count=0
for x in range (1,979//2+1):
    for y in range (1, (979-2*x)//7+1):
        for z in range (1,(979-2*x-7*y)//9+1):
            if 2*x +7*y+9*z==979:
                print(f"x= {x}  y= {y}  z= {z}")
                count+=1
                tong=x+y+z
                if tong< tongnhonhat:
                    tongnhonhat=tong
                    nghiem= (x,y,z)
if nghiem:
    print(f"Bộ nghiệm có tổng nhỏ nhất là: x= {nghiem[0]}, y= {nghiem[1]}, z= {nghiem[2]} ")
    print(f"Tổng nghiệm nhỏ nhất là: {tongnhonhat}")
else:
    print("Không tìm thấy bộ nghiệm nào")
