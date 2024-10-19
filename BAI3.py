# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:53:49 2024

@author: Bich Dao
"""
import random 

#1a
def tao_seqA():
    n=random.randint(30,80)
    seqA=[]
    for i in range(n+1):   
         if random.randint(0,1):
             seqA.append(round(random.uniform(-79,39),2))
             
         else:
            seqA.append(round(random.uniform(-79,39),2))
         return seqA
    
 #2
def ktra_dulieu(seqA):
    return[type(i).__name__ for i in seqA]

#3
def thongke(seqA):
    return len(seqA)
#4
def sapxep_seqB(seqA):
    return sorted(seqA)

#5
def trungbinh(seqA):
    return sum(seqA)/len(seqA)
#6
def trungbinh(seqB):
    #ví dụ chẵn =[1,2,3,4]>(2+3)/2
    #ví dụ lẻ =[1,2,3]>2
    n= len(seqB)
     return (seqB[n//2-1 +seqB[n//2])/2  if n%2==0 else seqB[n//2]
#7
def khoangcach(seq):
 return  max(seq)-min(seq)
 #8
def sosanh(seqA,seqB):
    return (trungbinh(seqA,trungbinh_seqB(seqB),))
              
    
    
if __name__=="__main__":
 seqA = tao_seqA()
print(seqA)
print(ktra_dulieu(seqA))
print(thongke(seqA))
print(sapxep_seqB(seqA))
print(trungbinh(seqA))
print(trungbinh(seqB))
print(khoangcach(seq))
trungbinh(seqA),trungbinh_seqB(seqB)
sosanh=sosanh(seqA,seqB)
print(sosanhAB)
           
             