class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i in xrange(len(nums)):
            dif = target - nums[i] 
            if dif in res:
                return [res[dif], i]
            else:
                res[nums[i]] = i