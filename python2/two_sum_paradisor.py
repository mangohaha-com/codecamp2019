class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [visited[target-nums[i]], i]
            else:
                visited[nums[i]] = i
        return []
