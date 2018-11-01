#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None:
            return []
        dic ={}
        for i in range(len(nums)):
            # if target - num is a key in map
            if target - nums[i] in dic:
                return[dic[target-nums[i]],i] # return value of that key, which is a index, and i
            dic[nums[i]]=i # else add target-num as key and i as value in map
        return []