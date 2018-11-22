"""
week 3

code has passed on leetcode.com
"""
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        r_int = roman[s[len(s)-1]]
        for i in range(len(s)-1, 0, -1):
            if roman[s[i]] > roman[s[i-1]]:
                r_int -= roman[s[i-1]]
            else:
                r_int += roman[s[i-1]]
                
        return r_int
