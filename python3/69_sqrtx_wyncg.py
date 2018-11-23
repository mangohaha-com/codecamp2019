class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        while True:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                elif (mid + 1) * (mid + 1) == x:
                    return mid + 1
                else:
                    start = mid + 1