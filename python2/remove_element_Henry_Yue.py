class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """
        This question is more like moving the elements == val to the end of the list and return total number of values != val.
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                end -= 1
            else:
                start += 1
        
        return start