class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums)-1
        
        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            if nums[left] != val and left <= right:
                left += 1
            if nums[right] == val and left <= right:
                right -= 1
        return left 