# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:39:09 2024

@author: Student
bai co trong thi ck  coi lai ham dao choi dao so vv
"""
import random
def kt_random(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
n = random.randint(1,99)
print(n)
print(kt_random(n))

