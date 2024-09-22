# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:47:53 2024

@author: DELL
"""

tonglonnhat= 0
count = 0 
for x in range (1,482):
    for y in range (1,(979- 2*x)//7+1):
        for z in range (1,(979 - 2 * x - 7 * y) // 9+1):
            if 2*x+7*y+9*z==979:
                print(f"x= {x}  y={y}  z={z}")
                count += 1
                tong= x+y+z
                if tong>tonglonnhat:
                    tonglonnhat=tong
                    nghiem=(x,y,z)
if nghiem:
    print(f"Bộ nghiệm có tổng x + y + z lớn nhất là: x = {nghiem[0]}, y = {nghiem[1]}, z = {nghiem[2]}")
    print("tổng nghiệm lớn nhất:", tonglonnhat)
else:
    print("không tìm thấy bộ nghiệm nào")