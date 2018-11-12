"""
week 2

code has passed on leetcode.com
"""

class Solution:
    def get_list(self, num):
        """
        :type num: int
        :type nlist: list
        """
        nlist = []
        while abs(num) >= 1:
            nlist.append(int(num % 10))
            num /= 10
        # nlist.reverse()
        
        return nlist
        
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tlist = self.get_list(x)
        tlen = len(tlist)
        r = 0
        for i in range(tlen):
            r += tlist[i] * pow(10, tlen - i - 1)
            
        return r
