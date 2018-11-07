class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        Important techenique to learn from this:
            popping the least significant digit of a int: use int % 10
            the remaining int after pop is int / 10
            to push to a target: target * 10 + pop
        """
        if x is None:
            return None
        
        negative = False
        if x < 0:
            negative = True
        
        x_abs = abs(x)
        
        MAX = 2 ** 31 -1
        MIN = - (2 ** 31)
        
        digit_count = 0
        result = 0

        while x_abs > 0:
            pop = x_abs % 10
            x_abs = x_abs / 10
            digit_count += 1
            if digit_count > 10:
                return 0
            result = result * 10 + pop
            
        if negative:
            result = -result
        if result < MIN or result > MAX:
            return 0
        
        return result
        