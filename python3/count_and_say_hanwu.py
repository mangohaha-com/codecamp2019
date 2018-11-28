#!/bin/python3
#count and say
#by hanwu

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        assert (n> 0)
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        prev_read = self.countAndSay(n-1)
        counter = 1
        prev_ch = prev_read[0]
        res = ''
        for ch in prev_read[1:]:
            if ch == prev_ch:
                counter += 1
            else:
                res += str(counter) + prev_ch
                prev_ch = ch
                counter = 1
        res += str(counter) + prev_ch
        return res
