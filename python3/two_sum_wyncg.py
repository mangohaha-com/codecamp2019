# Assignment1   Two Sum

# Leetcode #1

# Week1   11/3 ~

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index_hash = {}
        for i in range(len(nums)):
            current_num = nums[i]
            num_needed = target - current_num
            if num_needed in num_index_hash:
                return [i, num_index_hash[num_needed]]
            else:
                num_index_hash[current_num] = i