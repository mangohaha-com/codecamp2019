class Solution:
    def reverse(self, x):
        x=int(x)
        if x <0:
            s=-1
        else:
            s=1
        r=int(str(x*s)[::-1])
        
        return s*r * (r < 2**31)
        
