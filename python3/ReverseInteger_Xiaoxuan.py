class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nums = list(str(abs(x)))[::-1]
        while nums[0] == 0:
            nums.remove(nums[0])
        y = ""
        for i in nums:
            y += i
        y = int(y) if x>=0 else -int(y)

        if -2**31<= y <= 2**31 - 1:
            return y
        else:
            return 0




