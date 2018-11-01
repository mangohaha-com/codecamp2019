class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_up_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in look_up_dict:
                return [look_up_dict[complement], i]
            look_up_dict[nums[i]] = i