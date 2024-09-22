# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:12:42 2024

@author: DELL
"""

km= int(input("nhập quãng đường đã đi:"))
sotien=0
for i in range (1, km+1):
    if i<=1:
        sotien+=15000
        print("số tiền là:", sotien, "đồng")
    if 2<=i<=5:
        sotien+=13500
        print("sotienla:", sotien, "đồng")
    else:
        sotien+=11000
        print("so tiền là:", sotien, "đồng")
if km>120:
    sotien= sotien*0.9
    print("số tiền là:", sotien, "đồng")