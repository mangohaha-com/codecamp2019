class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<1:
            return 0

        l = 0
        r = x+1
        while r-l>1:
            temp = (r-l)//2+l
            if temp*temp == x:
                return temp
            elif temp*temp <x:
                if (temp+1)*(temp+1)>x:
                    return temp
                l = temp
            else:
                
                r = temp
        
        if l*l>x:
            return l-1
        elif r*r>x:
            return r-1
            