# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:19:07 2024

@author: Student
bai53
"""
def tong_1(n):
    tong=0
    for i in range(1,n+1):
        tong+=i
    return tong

# ddeef laf binh phuong
def tong_2(n):
    tong=0
    for i in range(1,n+1):
        tong+=i**2
    return tong
        
def tong_3(n):
    tong=0
    for i in range(1,n+1):
        tong+=1/i
    return tong

def tong_4(n):
    tong=0
    giaithua=1
    for i in range(1,n+1):
        giaithua*=i
        tong+= giaithua
    return tong


def tong_5(n):
    giaithua=1
    for i in range(1,n+1):
        giaithua*=i
    return giaithua

if __name__=="__main__":
    print(tong_1(5))    
    print(tong_2(5))
    print(tong_3(5))
    print(tong_4(5))
    print(tong_5(5))