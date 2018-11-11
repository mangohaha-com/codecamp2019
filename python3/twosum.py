class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        expected = dict()
        for idx, i in enumerate(nums):
            if i in expected:
                return [idx, expected[i]]
            else:
                expected[target-i] = idx