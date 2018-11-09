"""
Week2 11/14 Due
Given a 32-bit signed integer, reverse digits of an integer.

"""



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        m = 0
        if x > 0:
            while x > 0:
                m = 10*m + x % 10
                x = x / 10
            if m > 2**31-1: m = 0
            return m

        if x < 0:
            a = -x
            while a > 0:
                m = 10 * m + a % 10
                a = a / 10
            if m > 2**31: m = 0
            return -m
        return m