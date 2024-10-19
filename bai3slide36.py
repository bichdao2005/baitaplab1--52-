# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:54:35 2024

@author: Bich Dao
bai3 slide 36 lm ddc bai 56
"""

import math
def chuvi_dientich(hinh,pheptinh,*args,**kwargs):
    if hinh=="hinhvuong":
        canh=args[0]
        return 4*canh if pheptinh =="chuvi"else canh **2
    #tacg cau return
    #if pheptinh=="chuvi"
        #return 4*canh
    # else:
        #return canh**2
    elif hinh=="chunhat":
        dai= args[0]
        rong= args[1]
        return 2*(dai+rong) if pheptinh=="chuvi"else dai*rong
    elif hinh=="hinhtron":
        bk=args[0]
        return 2*math.pi*bk if pheptinh=="chuvi" else math.pi*(bk**2)
    else:
        return "hinh khoong hop le"
if __name__=="__main__":
    print("chu vi hinh vuong:", chuvi_dientich("hinhvuong"," chuvi",4))
    print("chu vi hinh vuong:", chuvi_dientich("hinhvuong"," dientich",4))
    print("chu vi hinh chu nhat:", chuvi_dientich("chunhat","chuvi",4,3))
    print("chu vi hinh chu nhat:", chuvi_dientich("chunhat","dientich",4,3))
    print("chu vi hinh tron:", chuvi_dientich("hinhtron","chuvi",4))
    print("chu vi hinh tron:", chuvi_dientich("hinhtron","dientich",4))