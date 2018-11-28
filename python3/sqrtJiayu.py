class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return None
        return int(x**0.5)
