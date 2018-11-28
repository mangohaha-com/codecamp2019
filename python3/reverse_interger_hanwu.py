#!/bin/python3
# reverse integer
# by hanwu

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_num = 2**31-1
        min_num = -(2**31)
        
        if x>0:
            y = int(str(x)[::-1])
        else:
            y = -(int(str(-x)[::-1]))
        if y>max_num or y<min_num:
            return 0
        else:
            return y