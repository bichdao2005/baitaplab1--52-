# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:06:42 2024
bai1 slide 36
@author: Bich Dao
"""

def tinhtong(*args,**kwangs):
        return sum(args)
def  tinhtich(*args, **kwargs):
    tich=1
    for i in args:
        tich*=i  
        return tich  
#def tinhtong(*args,**kwargs):
#tong =0
#for i in args:
  #   tong+=i
  #return tong
if __name__=="__main__":
    ds=[1,2,3,4,5]
    print(tinhtong(*ds))    
    print(tinhtich(*ds))