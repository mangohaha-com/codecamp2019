class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        is_neg = False
        if x < 0:
            is_neg = True
            
        x = abs(x)
        stack = []
        while x>0:
            reminder = x%10
            x = x//10
            stack.append(reminder)
        
        counter = 0
        result = 0
        while stack:    
            result += 10 ** counter * stack.pop()
            counter += 1
        if result >= 2**31 - 1 or result < -2**31:
            return 0
        return result if not is_neg else -result
    