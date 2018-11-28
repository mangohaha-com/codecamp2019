#!/bin/python3
#remove element
#by hanwu

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numLen = len(nums)
        
        i = 0
        for j in range(numLen):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i
