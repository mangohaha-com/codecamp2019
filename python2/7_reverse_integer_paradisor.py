class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = False
        if x < 0:
            x = -x
            flag = True
        while x != 0:
            mod = x % 10
            x /= 10
            res *= 10
            res += mod
            #print x
        if flag:
            res = -res
        return res