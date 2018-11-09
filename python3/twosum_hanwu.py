#!/bin/python3
#11/08/2018
#by Han Wu
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {};
        for i in range(0, len(nums)):
            if (target - nums[i]) in table:
                return [table[(target - nums[i])], i]
            else:
                table[nums[i]] = i
