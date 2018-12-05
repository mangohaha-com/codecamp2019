class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        char = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        result = dict[s[-1]]
        for i in range(len(s) - 1):
            symbol = 1
            if s[i] in ['I', 'X', 'C'] and dict[s[i + 1]] > dict[s[i]]:
                symbol = -1
            result += dict[s[i]] * symbol

        return result
