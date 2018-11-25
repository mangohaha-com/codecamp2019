class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0 
        if x < 0:
            flag = -1
        else:
            flag  = 1
   
        result = 0
        x = x * flag# 很重要
        while x:
            result = result * 10 + x % 10
            x /= 10
        if result > 2147483647:
            return 0 
        else:
            return result * flag
    
