# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:56:48 2024

@author: DELL
"""
ngay=-1
while ngay <1 or ngay >31:
    ngay=int(input("nhập ngày:"))
    if ngay <1 or ngay >31:
        print("vui lòng nhập ngày từ 1 đến 31")
thang=-1
while thang <1 or thang >12:
    thang=int(input("nhập tháng:"))
    if thang <1 or thang >12:
        print("vui lòng nhập tháng từ 1 đến 12")
nam=int(input("nhâp năm:"))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    songay = 31
elif thang in [4, 6, 9, 11]:
    songay = 30
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        ngay = 29
    else:
        ngay = 28
while ngay > songay:
    ngay=int(input("nhập ngày:"))
    print("nhập ngày hợp lệ")
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")

    