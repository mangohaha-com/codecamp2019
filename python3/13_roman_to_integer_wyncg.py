class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_num_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(s):
            if i == 0:
                continue
            else:
                if roman_num_map[s[i-1]] < roman_num_map[c]:
                    result -= roman_num_map[s[i-1]]
                else:
                    result += roman_num_map[s[i-1]]
        result += roman_num_map[s[-1]]
        return result