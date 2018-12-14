# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:11:30 2018

@author: dingchen

给定一个随机生成器，把一个数组顺序打乱
"""
import numpy as np
import random

def search_position(num, search_list):
    '''
    give a number, return the position of the search_list
    '''
    for i,j in enumerate(search_list):
        if j == num:
            return i
    print ('This number is not in the list of %s' %(search_list))
    raise AssertionError()

def random_array(array):
    random_list = []
    for i in range(len(array)):
        random_list.append(random.random())
    random_sort = sorted(random_list)
    result = np.zeros_like(array)
    for i,j in enumerate(random_list):
        result[search_position(j, random_sort)] = array[i]
    
    return result

#%%
#for test
a = np.array([1,2,3,4,5])
b = random_array(a)
print ('The original is %s, and the result is %s' %(a,b))
