# leetcode 7
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        if is_negative:
            x = x * -1
        num_list = list(str(x))
        num_list.reverse()
        reversed_x = int(''.join(num_list))
        if is_negative:
            reversed_x *= -1
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x