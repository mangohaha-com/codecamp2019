class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        Binary search approach
        """
        if x <= 1: return x
        
        lo = 1
        hi = x
        while True:
            mid = lo + (hi - lo) / 2
            if mid > x / mid:
                hi = mid - 1
            else:
                if (mid + 1) > (x / (mid + 1)):
                    return mid
                lo = mid + 1