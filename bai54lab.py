# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:35:16 2024

@author: Bich Dao
"""

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()
if __name__=="__main__":
    print(fib(100))