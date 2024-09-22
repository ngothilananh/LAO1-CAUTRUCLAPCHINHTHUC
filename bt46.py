# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:31:26 2024

@author: DELL
"""
#2x+7y+9z=979
#x=979/2
#y= 979-2x/7
#z= 979-2x-7y/9

count = 0 
for x in range (1,482):
    for y in range (1,(979- 2*x)//7+1):
        for z in range (1,(979 - 2 * x - 7 * y) // 9+1):
            if 2*x+7*y+9*z==979:
                print(f"x= {x}  y={y}  z={z}")
                count += 1
print(f"Tổng số nghiệm tìm được: {count}")
    
    
    