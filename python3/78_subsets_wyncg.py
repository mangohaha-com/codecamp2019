class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        for num in nums:
            newCombo = []
            for result in results:
                dup = result[:]
                dup.append(num)
                newCombo.append(dup)
            results.extend(newCombo)
        return results

        """
        #iterate
        self.res = []
        def dfs(nums, temp, i):
            self.res.append(temp[:])
            for i in range(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()
        dfs(nums, [], 0)
        return self.res
        """

        """
        bits manipulation
        """