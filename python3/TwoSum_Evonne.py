#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 10:18:35 2018

@author: congwen
"""
import random
        
def twoSum(nums, target):
    for x_index in range (len(nums)):
        for y_index in range(x_index+1, len(nums)):
#            print (y_index)
            if nums[x_index] + nums[y_index] == target:
                return [x_index,y_index ]

length = random.randint(1,10000)
print (length)

nums = range(length) 

a = random.randint(1,length-1) 
print (a)
b = random.randint(a+1,length) 
print (b)

target = nums[a] +nums[b]
print (target)

print (twoSum(nums, target))






