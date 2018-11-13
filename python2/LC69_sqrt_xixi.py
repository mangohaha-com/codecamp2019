class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lower = 0
        upper = x
        if x == 1: return 1
        while upper > lower + 1:
            middle = (upper+lower)/2
            if middle * middle == x:
                return middle
            elif middle * middle > x:
                upper = middle
            else:
                lower = middle
        result = lower
        return result