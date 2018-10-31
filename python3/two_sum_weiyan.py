class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Use dictionary key/value pair to quick search two sum
        # Use subtraction of target with each num as key, and their index as value
        sub_dict = {}
        for i in range(len(nums)):
            temp_sub = target - nums[i]
            sub_dict[temp_sub] = i
        
        # Go for one loop to find whether the subtraction and the nums have the same value
        for i in range(len(nums)):
            if sub_dict.get(nums[i]) and i!=sub_dict[nums[i]]:
                return [i,sub_dict[nums[i]]]