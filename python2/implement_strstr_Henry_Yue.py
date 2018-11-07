class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        l_haystack = len(haystack)
        l_needle = len(needle)
        
        for i in range(l_haystack):
            if i + l_needle <= l_haystack and haystack[i:i+l_needle] == needle:
                return i
            
        return -1