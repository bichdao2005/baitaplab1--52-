# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
baif 52
"""
import math
#1a 
def canbac(x,n):
    return x**(1/n)

#1b
def sodao(n):
    #return str(n)[::-1]
    return int(str(n)[::-1])
#1c
def ktra_chinhphuong(n):
    return int(math.sqrt(n))**2==n

#1d
def ktr_nguyento(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#1e
def tich_le(n):
    tich=1 
    for i in str(n):
        if int(i)%2 !=0:
            tich*=int(i)
    return tich
#1f
def tong_nt(n):
    tong=0
    for i in range(2,n):
        if ktr_nguyento(i):
            tong+=i
    return tong

#1g
def tong_cp(n):
    tong=0
    for i in range(1,n):
        if ktra_chinhphuong(i):
            tong+=i
    return tong

#1h
def tonguoc(n):
    tong=0
    for i in range(1,n+1):
        if n%i ==0:
            tong+=i
    return tong


if __name__=="__main__":
    print(canbac(8,3))
    print(sodao(123450))
    print(sodao(123450))
    print(ktra_chinhphuong(16))
    print(ktr_nguyento(7))
    print(tich_le(135))
    print(tong_nt(9))
    print(tong_cp(17))
    print(tonguoc(4))

                  
