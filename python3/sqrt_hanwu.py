#!/bin/python3
# sqrt(x)
# by hanwu 

from math import sqrt
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = int(sqrt(int(x)))
        return ans