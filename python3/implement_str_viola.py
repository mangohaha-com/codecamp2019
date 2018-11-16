"""
week 2

code has passed on leetcode.com
"""
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle in haystack:
            return -1
        else:
            for i in range(len(haystack) - len(needle)):
                if needle in haystack[0+i:len(needle)+i]:
                    return i

        return -1
