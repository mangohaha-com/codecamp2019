class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
           
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        l = len(s)
        result = dic[s[l-1]]

        for i in range(l-1):
            if dic[s[i]] < dic[s[i+1]]:
                result -= dic[s[i]]
            else:
                result += dic[s[i]]
        return result