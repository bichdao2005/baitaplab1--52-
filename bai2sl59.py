# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:41:44 2024

@author: Bich Dao

"""
#
ds=[("Tiền Giang",63),("Long An",62),("Vĩnh Long",64),("Bình Dương",60)]
print(sorted(ds))
#số
print(sorted(ds,key= lambda x: x[1]))
