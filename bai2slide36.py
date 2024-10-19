# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:32:49 2024

@author: Bich Dao
bai2 sl36
"""
import math
def chuvi(hinh,*args,**kwargs):
    if hinh=="hinhvuong":
        canh=args[0]
        return 4*canh
    elif hinh=="chunhat":
        dai= args[0]
        rong= args[1]
        return 2*(dai+rong)
    elif hinh=="hinhtron":
        bk=args[0]
        return 2*math.pi*bk
    else:
        return "hinh khoong hop le"
if __name__=="__main__":
    print("chu vi hinh vuong:", chuvi("hinhvuong",4))
    print("chu vi hinh chu nhat:", chuvi("chunhat",4,3))
    print("chu vi hinh tron:", chuvi("hinhtron",4))