def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j+1
        return j
        
       
nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))


def removeElement2(self, nums, val):
        for ele in nums[:]:
            if ele == val:
                nums.remove(val)
        return len(nums)

