class Solution:
    def twoSum(self, nums, target):
        value_index_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in value_index_dict:
                return [value_index_dict[target - nums[i]],i]
            value_index_dict[nums[i]] = i