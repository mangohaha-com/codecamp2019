class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=0
        if abs(x)
        if x<0:
            signal = -1
            x*=-1
        else:
            signal = 1
        while x!=0:
            y=y*10+x%10
            x=x//10
        y = signal*y
        if y >2**31-1 or y<-(2**31):
            return 0
        return y