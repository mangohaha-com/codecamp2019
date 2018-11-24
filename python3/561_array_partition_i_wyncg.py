class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort and then sacrifice in pair the bigger one.
        nums.sort()
        result = 0
        i = 0
        while i < len(nums):
            result += nums[i]
            i += 2
            
        return result